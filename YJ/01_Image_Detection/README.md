# 🚀 차량 파손 탐지 (Car Damage Detection)

- 차량 이미지에서 **파손 부위 자동 탐지 Object Detection 모델 구축**
- 차량 detection → 차량 crop → 파손 detection 흐름의 **2-stage detection pipeline 설계**
<br>

## 📂 Dataset

### Dataset Summary

| Item | Value |
|-----|------|
| Total Images | 1,357 |
| Normal Images | 157 |
| Damaged Images | 1,200 |
| Annotation Type | Bounding Box |

- **Normal:** 차량 파손이 없는 이미지
- **Damaged:** 차량 파손 부위 annotation이 포함된 이미지

<br>

### Annotation Structure (Damaged Images)

Damaged 데이터는 **COCO-style JSON 구조 기반 annotation**으로 구성됨.

```json
{
  "info": {
    "name": "socar",
    "date_created": "03/08/2022"
  },
  "images": {
    "id": 1,
    "width": 960,
    "height": 720,
    "file_name": "0000459_sc-226797.jpg"
  },
  "annotations": [
    {
      "id": 2,
      "image_id": 1,
      "category_id": "sc-226797",
      "segmentation": [...],
      "bbox": [3, 360, 957, 39],
      "area": 19507.0,
      "damage": "Separated",
      "part": null,
      "year": 2018,
      "color": "White"
    }
  ],
  "categories": {
    "id": "sc-226797",
    "supercategory_name": "Full-size car"
  }
}
```
<br>

## ⚙️ Experiment Setup

- **Model:** YOLOv8
- **Environment:** Google Colab Pro
- **GPU:** NVIDIA T4
- **Framework:** Ultralytics YOLOv8
- **train/val/test:** 70% / 15% / 15%
<br>

## 🛠 Workflow

```
Raw Vehicle Image
↓
Stage 1 : Vehicle Detection (COCO pretrained)
↓
Vehicle Crop
↓
Stage 2 : Damage Detection ( 사전 학습 모델 파인튜닝)
↓
Evaluation
```
<br>

## 🚗 Stage 1 : Vehicle Detection

### 0. 목적
 
| Item | Description |
|------|-------------|
| 🎯 **배경** | Stage1 모델에서, 전체 이미지 대비 차량 영역이 작은 경우 파손 탐지 성능 저하 |
| ⚠️ **문제점** | 차량 bbox annotation 부재로 detection 모델 직접 학습 어려움 |
| 🔧 **해결책** | COCO pretrained detection 모델 활용하여 차량 bbox inference |
| 📈 **기대효과** | 차량 ROI crop 기반 Stage 2 damage detection 데이터 품질 개선 |

<br>

### 1. pretrained model inference

- COCO dataset으로 pretrained된 모델을 이용해 차량 bbox inference

<br>

**⚙️ Hyperparameters**
| Parameter | Value | Note |
| :--- | :--- | :--- |
| **model** | yolov8m | COCO pretrained YOLOv8 medium 모델 |
| **conf** | 0.2 | detection confidence threshold (0.2 이상 prediction만 유지) |
| **Img Size** | 640 | YOLOv8 기본 입력 이미지 크기 |
| **classes** | [2,3,5,7] | COCO vehicle classes (car, motorcycle, bus, truck) |

<br>

### 2. inference 결과 정성평가

**1️⃣ Vehicle Miss Rate 측정**

- 차량이 존재하는 이미지 중 detection 실패 비율 측정

**Evaluation 기준**
- damaged 차량의 경우, 모든 이미지에 차량이 존재하므로
  * <5% → 매우 우수
  * 5~10% → borderline
  * 10% → fine-tune 필요

**Detection Result**

|  | Count | Detected | Miss | Miss Rate | 
| :--- | :--- | :--- | :--- | :--- |
| **damaged** | 1200 | 922 | 278 | 0.231 |
| **normal** | 157 | 154 | 3 | 0.02 |

**Overall Vehicle Miss Rate : 0.23 (23%)**

<br>

**vehicle miss samples**
 
<table>
<tr>
<td><img src="https://github.com/user-attachments/assets/d3c58ea1-a816-4b6d-8569-3116c3685b8d" width="220"></td>
<td><img src="https://github.com/user-attachments/assets/be670170-ba7d-4265-87de-eab7a664684a" width="220"></td>
<td><img src="https://github.com/user-attachments/assets/425280fb-c015-46a7-b8fd-65352b18a220" width="220"></td>
</tr>

<tr>
<td><img src="https://github.com/user-attachments/assets/3c5a469f-75e7-413a-a2a1-ee67dd5eecfa" width="220"></td>
<td><img src="https://github.com/user-attachments/assets/49fcbaff-beb4-441e-b7c4-b6550b001845" width="220"></td>
<td><img src="https://github.com/user-attachments/assets/43341d07-0c1f-4cfd-a0d9-cc2aa89b899f" width="220"></td>
</tr>
</table>


**Insight**

- **Normal 이미지:** 약 **99% 차량 detection 성공**
- **Damaged 이미지:** 약 **77% 차량 detection 성공**
- 차량이 **파손 부위 중심으로 매우 근접 촬영된 경우 detection 실패**
- 차량 전체 형태가 드러나지 않는 이미지에서 detection 어려움 발생

<br>

**Decision**

- 차량 detection 성공 이미지 → **bbox 기반 crop 적용**
- 차량 detection 실패 이미지 (약 23%) → **원본 이미지 그대로 Stage2 입력**

→ Stage2 damage detection 학습 시 **vehicle ROI 기반 데이터 구성**

<br><br>


**2️⃣ BBox Quality 분석**

- 확인 사항
  - 차량 전체 포함 여부
  - bbox가 너무 타이트해서 파손 부위가 잘리는지
  - bbox가 너무 커서 배경이 많이 들어가 있는지
  - 다양한 차량 각도 detection 가능 여부
  - bbox_area/image_area 분포 확인


<img width="740" height="499" alt="image" src="https://github.com/user-attachments/assets/6161b31a-52f8-4b68-92fb-971e171d99dd" />

<br>

**Decision**

→ 대부분 차량 bbox가 차량 전체 영역을 안정적으로 포함  
→ Stage2 crop에 활용 가능한 수준의 bbox quality 확인

<br><br>

## 🔧 Stage 2 : Damage Detection

### Vehicle Crop Dataset 생성

Stage1에서 추출한 **vehicle bbox 기반으로 ROI crop dataset 생성**

<br>

**Crop Strategy**

| Item | Description |
|---|---|
| **Padding** | bbox 가장자리 기준 **20% padding 적용** |
| **Multiple Vehicles** | 여러 bbox 존재 시 **가장 큰 bbox 기준 crop** |
| **Dataset Split** | crop 결과를 **normal / damaged 폴더로 분리 저장** |
| **Damage Preservation** | crop 과정에서 **damage bbox가 잘리는 경우 crop 미수행** |

<br>

**damage bbox annotation 위치 변환**

- crop 이후 **damage bbox 좌표 재계산**
- crop된 이미지 기준으로 **bbox coordinate 변환**

<br>

**Crop Example**

| Original | Crop |
|---|---|
| <img src="https://github.com/user-attachments/assets/c6cc951d-7092-4637-b9dc-d89f2f4bdc85" width="320"> | <img src="https://github.com/user-attachments/assets/11de9671-043a-46b2-bf90-3ad040adeeaf" width="320"> |
| <img src="https://github.com/user-attachments/assets/84a98c65-e3a1-4145-845f-1a1642fc8394" width="320"> | <img src="https://github.com/user-attachments/assets/45319db6-778d-4c5e-acfc-6a1d0afa3dc2" width="320"> |

<br>

## 🤖 Model Experiments
* Stage2 damage detection 성능 비교를 위해 다양한 detection architecture 실험

**⚙️ Training Settings**

| Item | Value | Note |
|---|---|---|
| **Dataset** | Vehicle Damage Dataset | Stage1에서 차량 영역 crop 후 사용 |
| **Image Size** | 640 | 모든 모델 동일 입력 크기 |
| **Batch Size** | 16 | GPU 메모리 고려 설정 |
| **Epochs** | 100 | 동일 학습 조건 유지 |
| **Optimizer** | AdamW | detection 모델 학습 안정성 고려 |
| **Augmentation** | Mosaic, Flip, HSV | YOLO 기본 augmentation 사용 |
| **Hardware** | NVIDIA GPU T4 | 동일 환경에서 학습 수행 |

<br>

**⚙️ Models**

| Model | Type | Key 특징 | Experiment 목적 |
|---|---|---|---|
| **YOLOv8n** | One-stage | 경량 모델, 빠른 inference 속도 | baseline 성능 확인 |
| **RT-DETR** | Transformer-based | NMS-free detection, global attention 기반 object detection | transformer 기반 detector 성능 비교 |
| **Faster R-CNN** | Two-stage | region proposal 기반 detection, 높은 localization accuracy | 전통적인 two-stage detector 성능 비교 |

<br>

## 📊 Performance Summary

| Model | mAP@50-95 | mAP@50 | Pixel IoU | Pixel Recall | Damage Recall | Train Time(s) | Inference Time(s) |
|------|------|------|------|------|------|------|------|
| YOLOv8n | 0.18 | 0.28 | 0.41 | 0.51 | 0.86 | 3545.6 | 35.37 |
| RT-DETR | 0.23 | 0.34 | 0.46 | 0.71 | 1.0 | 8674.3 | 21.97 |
| Faster R-CNN | 0.03 | 0.01 | 0.31 | 0.57 | 0.96 | 399.07 | 17.62 |

<br>

## 📈 Evaluation Metrics

**1️⃣ mAP@0.5**

- Object Detection 표준 성능 지표

<br>

**2️⃣ Pixel-level IoU ⭐**

**배경**
- EDA 과정에서 **GT bounding box 간 중복(overlap)** 문제 확인
- 하나의 예측 bbox가 **여러 GT bbox를 포함하는 경우** 발생
- 이 경우 **bbox 개수 mismatch**로 인해 기존 IoU 기반 평가지표가 실제 성능보다 **과도하게 낮게 평가**

**Approach**

- GT bbox → **binary mask 변환**
- Pred bbox → **binary mask 변환**
- bbox matching 없이 **pixel 단위 IoU 계산**

**Metric**

```
Pixel IoU = (GT_mask ∩ Pred_mask) / (GT_mask ∪ Pred_mask)
```

**Characteristics**

- bbox matching 과정 불필요
- multiple bbox overlap 자동 처리
- 파손 위치 중심 detection 성능 평가 가능

<br>

**3️⃣ Image-level Damage Recall**

| Item | Description |
|---|---|
| **Definition** | GT에 파손이 존재하는 이미지 중 모델이 **하나라도 파손을 탐지한 비율** |
| **Purpose** | 실제 서비스 환경에서 **파손 차량 필터링 능력 평가** |
| **Key Point** | bbox 정확도보다 **파손 존재 여부 탐지 성능** 확인 |

<br>

**4️⃣ Training Time**

- 모델 학습 시간

<br>

**5️⃣ Inference Time**

- 모델 추론 속도

<br>

## 🧾 Conclusion

### Key Findings

- **RT-DETR 모델이 가장 높은 전반적 성능 달성**
   - Transformer 기반 모델임에도 **비교적 적은 데이터에서 안정적인 detection 성능 확인**
- **Pixel-level IoU 및 Image-level Recall 지표를 통해 파손 위치 탐지 성능 효과적으로 평가**

<br>

### Limitations

- **Faster R-CNN의 낮은 confidence threshold로 인한 과도한 bbox 예측**
  - bbox 과다 예측으로 **precision 및 mAP 성능 저하**
- **YOLOv8 baseline 모델의 tuning 적용 상태로 공정한 baseline 비교 한계**

<br>

### Future Work

- Faster R-CNN confidence 및 NMS 파라미터 튜닝
- RT-DETR 추가 데이터 확보 및 hyperparameter tuning
- YOLOv8 모델의 tuning 전 baseline 성능 비교 실험
- Stage2 damage detection 데이터셋 확장 및 augmentation 전략 개선

<br>

# 1. EDA
- 우리 데이터셋(aihub 차량파손이미지데이터)의 damaged/images, damaged/labels 정보
![aihubeda](./images/image(data_description_01).png)
![aihubeda](./images/image(data_description_02).png)

- 전체 데이터셋의 손상종류별 수량 및 비율
![aihubeda](./images/week3_손상종류.png)

- 우리 데이터셋(샘플 1200)의 손상종류별 수량\
○ Scratched(스크래치)  : 2405(63.3%)\
○ Crushed(찌그러짐)    : 312(8.2%)\
○ Breakage(파손)       : 529(13.9%)\
○ Separated(이격)      : 552(14.5%)

**시각화**
  
**[Case1]**
![aihubeda1](./images/image(week3_01).png)

**[Case2]**
![aihubeda1](./images/image(week3_02).png)

**[Case3]**
![aihubeda1](./images/image(week3_03).png)

# 2. 데이터셋 분리
- 전체 DATA 1200개 중 train/val/test를 8:1:1로 분리
- Train: 960 / Val: 120 / Test: 120

# 3. 모델링 및 테스트
- MODEL = "yolov8s.pt"
- IMGSZ = 640
- EPOCHS = 100
- BATCH = 16

## 가. 전체 성능

### Micro Average (전체 객체 기준)

| Metric | Value |
|------|------|
| Precision | **0.5304** |
| Recall | **0.3503** |
| F1-score | **0.4219** |
| TP / FP / FN | 131 / 116 / 243 |

- 실제 파손 객체 중 **약 35%만 탐지**
- 탐지된 객체의 절반 정도만 정확한 예측
- **FN(미탐지)이 매우 많음 → Recall이 핵심 병목**

### Bounding Box 품질 (TP 기준)

| Metric | Value |
|------|------|
| Mean IoU (TP only) | **0.8456** |

- 탐지에 성공한 객체에 대해서는 **박스 위치 정확도 매우 우수**
- 위치 회귀(Box Regression) 문제는 거의 없음

### Macro Average (클래스 동일 가중)

| Metric | Value |
|------|------|
| Precision | **0.5706** |
| Recall | **0.3546** |
| F1-score | **0.4350** |

- 클래스 간 성능 편차는 크지 않음
- 전반적으로 **모든 클래스에서 Recall 부족**

## 나. 클래스별 성능

| Class | TP | FP | FN | Precision | Recall | F1 |
|------|---:|---:|---:|----------:|-------:|----:|
| Crushed | 12 | 7 | 25 | 0.6316 | 0.3243 | 0.4286 |
| Scratched | 75 | 77 | 142 | 0.4934 | 0.3456 | 0.4065 |
| Breakage | 21 | 16 | 29 | 0.5676 | 0.4200 | 0.4828 |
| Separated | 23 | 16 | 47 | 0.5897 | 0.3286 | 0.4220 |

### 클래스별 해석 요약
- **Breakage**: 가장 안정적인 성능 (Recall/F1 최고)
- **Scratched**: 가장 어려운 클래스  
(경계 불명확, 면적 작음, 배경과 혼합)
- 모든 클래스에서 **미탐지(FN)가 FP보다 많음**

## 다. 종합 해석

**[강점]**
- 탐지에 성공한 객체의 박스 정확도(IoU)는 매우 높음
- 특정 클래스에 국한된 실패는 아님

**[한계]**
- 전체적으로 파손 객체를 충분히 찾아내지 못함
- Recall 저하로 인해 F1 및 체감 성능이 제한됨

**[요약]**
> - “잡으면 정확하지만, 많이 놓치는 YOLO 모델”
> - 현 단계의 핵심 개선 포인트는 **Recall 향상**

## 라. 향후 개선 방향 (요약)

- Confidence threshold 조정 (↓)
- 작은 파손 객체 대응을 위한 이미지 해상도 및 증강 전략
- Scratched 클래스 중심 데이터 보강
- mAP(@0.5 / @0.5:0.95) 기반 추가 평가 권장

# 4.시각화
**[BEST CASE]**
![visualization](./images/best_01.jpg)
![visualization](./images/best_02.jpg)
![visualization](./images/best_03.jpg)
![visualization](./images/best_04.jpg)
![visualization](./images/best_05.jpg)
![visualization](./images/best_06.jpg)
![visualization](./images/best_07.jpg)
![visualization](./images/best_08.jpg)
![visualization](./images/best_09.jpg)
![visualization](./images/best_10.jpg)

**[WORST CASE]**
![visualization](./images/worst_01.jpg)
![visualization](./images/worst_02.jpg)
![visualization](./images/worst_03.jpg)
![visualization](./images/worst_04.jpg)
![visualization](./images/worst_05.jpg)
![visualization](./images/worst_06.jpg)
![visualization](./images/worst_07.jpg)
![visualization](./images/worst_08.jpg)
![visualization](./images/worst_09.jpg)
![visualization](./images/worst_10.jpg)

# 5.모델 추가학습(epoch 100 → 200)

- 테스트 이미지 수: **120**
- 비교 모델
  - **Model 1**: yolo_v3 / yolo_v1.pt ← 100 epoch
  - **Model 2**: yolo_v4 / yolo_v1.pt ← 200 epoch
- 클래스: `Crushed`, `Scratched`, `breakage`, `Separated`

YOLO_MODEL = "yolov8s.pt"
IMGSZ = 640
EPOCHS = 100 → 200 --- epoch만 2배로..
BATCH = 16
DEVICE = 0  # GPU:0(L4 사용)
---

## 5-1.전체 성능 비교 (Overall Metrics)

### 가.Micro / Macro 평균 성능

| Metric | Model 1 | Model 2 | 비교 |
|------|--------|--------|------|
| **Micro Precision** | 0.5304 | **0.6142** | ▲ Model 2 |
| **Micro Recall** | **0.3503** | 0.3235 | ▲ Model 1 |
| **Micro F1-score** | 0.4219 | **0.4238** | ≈ 유사 |
| **Micro mean IoU (TP)** | 0.8456 | **0.8837** | ▲ Model 2 |
| **Macro Precision** | 0.5706 | **0.6814** | ▲ Model 2 |
| **Macro Recall** | **0.3546** | 0.3476 | ▲ Model 1 |
| **Macro F1-score** | 0.4350 | **0.4599** | ▲ Model 2 |

---

### 나.Error 관점 비교 (Micro 기준)

| 항목 | Model 1 | Model 2 | 해석 |
|----|--------|--------|------|
| TP | **131** | 121 | Model 1이 더 많이 탐지 |
| FP | 116 | **76** | Model 2가 오탐 감소 |
| FN | **243** | 253 | Model 2가 더 보수적 |

📌 **Model 2는 Precision 중심 (보수적 탐지)**  
📌 **Model 1은 Recall 중심 (더 많이 잡지만 오탐 증가)**

---

## 5-2. 클래스별 성능 비교 (Per-class)

### 가. F1-score 기준 비교

| Class | Model 1 F1 | Model 2 F1 | 변화 |
|-----|-----------|-----------|------|
| **Crushed** | 0.4286 | **0.5185** | ▲ 개선 |
| **Scratched** | **0.4065** | 0.3844 | ▼ 악화 |
| **breakage** | **0.4828** | 0.4737 | ≈ 유사 |
| **Separated** | 0.4220 | **0.4630** | ▲ 개선 |

---

### 나. Precision / Recall 상세

| Class | Model | Precision | Recall |
|-----|------|----------|--------|
| Crushed | Model 1 | 0.6316 | 0.3243 |
|  | Model 2 | **0.8235** | **0.3784** |
| Scratched | Model 1 | 0.4934 | **0.3456** |
|  | Model 2 | **0.5517** | 0.2949 |
| breakage | Model 1 | 0.5676 | **0.4200** |
|  | Model 2 | **0.6923** | 0.3600 |
| Separated | Model 1 | 0.5897 | 0.3286 |
|  | Model 2 | **0.6579** | **0.3571** |

---

## 5-3 종합 해석 (결론)

### ✔ Model 2 (yolo_v4)의 특징
- Precision, IoU, Macro F1 전반적 우수
- FP가 크게 감소 → **오탐 억제에 강함**
- 클래스 불균형 상황에서 더 안정적

### ✔ Model 1 (yolo_v3)의 특징
- Recall이 전반적으로 높음
- FN이 적음 → **놓치면 안 되는 탐지에 유리**
- Scratched 클래스에서는 더 나은 성능

---

## 5-4. 요약 비교

| 목적 | 추천 모델 |
|----|----------|
| 보험/법률 증빙용 (오탐 최소화) | **Model 2** |
| 파손 후보 최대 수집 (1차 필터) | **Model 1** |
| 2-stage 파이프라인 | Model 1 → Model 2 |
| 클래스별 파손 정밀 분석 | Model 2 |

> **Model 2는 더 정확하고 보수적이며,  
Model 1은 더 많이 찾지만 실수가 많은 모델이다.**

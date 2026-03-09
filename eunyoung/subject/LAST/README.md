# 🚗 자동차 파손 탐지 모델 성능 비교 분석 (Vehicle Damage Detection)

본 문서는 **YOLOv8m**과 **RT-DETR-L** 모델을 활용한 차량 파손 탐지 성능 비교 및 삼성화재 자동차 보험 언더라이팅 프로젝트 적용을 위한 분석 리포트입니다.

---

## 1. 실험 개요 (Experimental Setup)
* **데이터셋:** AI HUB 자동차 파손 이미지 데이터셋
* **검증 데이터 규모:** 이미지 2,000장 / 인스턴스 6,798개
* **학습 설정:** 100 Epochs, `imgsz=640`, `batch=16`, `close_mosaic=10`
* **대상 클래스:** `scratch`(스크래치), `dent`(함몰), `crushed`(파손), `separated`(이격)

---

## 2. 모델별 성능 비교 (Performance Summary)

| Model | Class | Precision | Recall | mAP50 | mAP50-95 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **YOLOv8m** | **all** | 0.392 | 0.300 | 0.258 | 0.119 |
| **RT-DETR-L** | **all** | 0.389 | **0.307** | **0.262** | **0.123** |

### 📊 클래스별 mAP50 상세 결과
| Class | Instances | YOLOv8m | RT-DETR | 변동폭 |
| :--- | :---: | :---: | :---: | :---: |
| **scratch** | 3,648 | 0.250 | **0.262** | <span style="color:red">▲ 0.012</span> |
| **dent** | 1,295 | 0.313 | **0.322** | <span style="color:red">▲ 0.009</span> |
| **crushed** | 918 | **0.250** | 0.234 | <span style="color:blue">▼ 0.016</span> |
| **separated** | 937 | 0.219 | **0.230** | <span style="color:red">▲ 0.011</span> |

---

## 3. 핵심 분석 결과 (Key Insights)

### **1) 모델 구조 변경 효과**
* CNN 기반의 **YOLOv8m**에서 Transformer 기반의 **RT-DETR-L**로 변경 시, 전체 mAP50이 **0.258 → 0.262**로 소폭 향상되었습니다.
* 특히 전역적 문맥(Context) 파악이 중요한 `scratch`와 `separated` 클래스에서 Transformer의 장점이 발휘되어 성능 개선이 확인되었습니다.

### **2) Recall(재현율) 정체 현상**
* 두 모델 모두 Recall이 0.3 수준에 머물러 있습니다. 이는 실제 파손 부위의 **약 70%를 놓치고 있음**을 의미하며, 언더라이팅 자동화 시스템 도입을 위해 가장 시급히 개선해야 할 지표입니다.

### **3) 데이터의 질과 성능의 상관관계**
* `scratch` 데이터량이 가장 많음에도 성능은 `dent`보다 낮습니다. 이는 미세 파손 탐지에 있어 **데이터의 양보다 이미지 해상도 및 특징 추출 난이도**가 더 큰 영향을 미치고 있음을 보여줍니다.

---

## 4. 향후 개선 전략 (Next Steps)

### **✅ 데이터 증강 및 학습 튜닝**
* **Resolution Up:** 미세 스크래치 탐지를 위해 `imgsz`를 640에서 **1024 이상**으로 상향 조정.
* **Mosaic Strategy:** 현재 적용된 `close_mosaic=10` 옵션의 시점을 조정(예: 15~20)하여 정교한 튜닝 기간을 최적화.
* **Class Weighting:** 성능이 낮은 `separated`와 `crushed` 클래스에 학습 가중치를 부여.

### **✅ 추론 기법 고도화**
* **SAHI (Slicing Aided Hyper Inference):** 고해상도 이미지를 조각(Tiling) 내어 추론함으로써 소형 객체 탐지율 극대화.
* **Ensemble:** YOLOv8의 정밀도(Precision)와 RT-DETR의 문맥 파악 능력을 결합한 **Weighted Boxes Fusion(WBF)** 기법 검토.

---
> **Note:** 본 결과는 `close_mosaic=10` 설정이 포함된 최종 100에폭 결과이며, 이후 하이퍼파라미터 튜닝을 통해 Recall 개선을 목표로 함.

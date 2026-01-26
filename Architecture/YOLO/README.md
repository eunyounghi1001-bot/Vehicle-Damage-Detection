# YOLO (You Only Look Once): Real-Time Object Detection as a Single Regression Problem  
*(Joseph Redmon et al., 2016 ~)*

---

## 1. 연구 배경 (Motivation)

기존 객체 탐지(Object Detection) 모델들은 대부분 **2-Stage 구조**를 사용했다.

### 기존 접근 방식 (R-CNN 계열)
- **Region Proposal → Classification**
- 높은 정확도
- ❌ 추론 속도가 매우 느림
- ❌ 실시간 서비스에 부적합
- ❌ 파이프라인 복잡

👉 논문의 질문:
> “객체 탐지를 **단일 네트워크, 단일 단계**로 해결할 수 없을까?”

---

## 2. YOLO의 핵심 아이디어

YOLO는 객체 탐지를 **하나의 회귀(Regression) 문제**로 정의한다.

### 핵심 개념
- 이미지를 **한 번만(You Only Look Once)** 본다
- Bounding Box + Class Probability를 **동시에 예측**
- End-to-End 단일 CNN 구조

👉 결과:
- 🚀 매우 빠른 추론 속도
- ⚡ 실시간 객체 탐지 가능

---

## 3. YOLO의 기본 구조 (Overall Architecture)

<img src="./images/yolo_architecture.png" width="600"/>

### 전체 파이프라인
1. 입력 이미지를 **S × S grid**로 분할
2. 각 grid cell이 다음을 예측:
   - B개의 Bounding Box
   - Confidence Score
   - Class Probability

### 예측 값 구성
- `(x, y, w, h)` : Bounding Box 좌표
- `confidence = Pr(object) × IoU`
- `Pr(class | object)`

👉 **Non-Max Suppression (NMS)** 으로 최종 박스 결정

---

## 4. 핵심 아이디어 ①: Single-Stage Detection

### 기존 Two-Stage 방식
- RPN → ROI Pooling → Classifier
- 느리고 복잡

### YOLO 방식
- **단일 CNN**
- **단일 Forward Pass**
- Detection = Regression

| 구분 | Two-Stage | YOLO |
|---|---|---|
| 구조 | 복잡 | 단순 |
| 속도 | 느림 | **매우 빠름** |
| 실시간 | 불가 | **가능** |

---

## 5. 핵심 아이디어 ②: Global Context 활용

<img src="./images/yolo_global_context.png" width="600"/>

YOLO는 이미지 전체를 한 번에 보기 때문에  
local feature에만 의존하지 않는다.

### 효과
- 배경 정보를 함께 고려
- False Positive 감소
- 객체 간 위치 관계 학습 가능

👉 R-CNN 계열 대비 **배경 오탐지 감소**

---

## 6. YOLO 버전 진화 (YOLOv1 → YOLOv8)

<img src="./images/yolo_evolution.png" width="700"/>

| 버전 | 주요 특징 |
|---|---|
| YOLOv1 | 단일 회귀 기반 Detection |
| YOLOv2 | Anchor Box, Batch Normalization |
| YOLOv3 | Multi-Scale Detection |
| YOLOv4 | CSPDarknet, Bag of Freebies |
| YOLOv5 | PyTorch 기반, 실무 표준 |
| YOLOv7 | 속도·정확도 최적화 |
| YOLOv8 | Anchor-Free, 분리된 Detection Head |

👉 최신 YOLO는 초기 버전과 **완전히 다른 수준의 완성도**

---

## 7. YOLOv8 기준 아키텍처 구성

<img src="./images/yolov8_architecture.png" width="700"/>

### 구성 요소
1. **Backbone**
   - CSP 계열 구조
   - Feature Extraction
2. **Neck**
   - FPN + PAN
   - Multi-Scale Feature Fusion
3. **Head**
   - Anchor-Free 구조
   - Box / Class 분리 예측

---

## 8. 성능 특성 및 실험 결과 요약

### 장점
- ⚡ 매우 높은 FPS
- 📦 다양한 크기의 모델 제공 (n, s, m, l, x)
- 🧩 실무 환경에서 높은 활용도

### 한계
- 작은 객체(Small Object) 탐지 상대적 약점
- 극고정밀 작업에서는 Two-Stage 대비 열세

---

## 9. YOLO의 주요 기여 (Contributions)

1. Object Detection을 **Regression 문제로 재정의**
2. **Real-Time Detection** 가능성 제시
3. 단순하면서 확장 가능한 구조
4. 산업·서비스 환경에서 폭넓은 채택

👉 객체 탐지 역사에서 **전환점이 된 모델**

---

## 10. YOLO vs Faster R-CNN vs SSD

| 항목 | YOLO | Faster R-CNN | SSD |
|---|---|---|---|
| 구조 | Single-Stage | Two-Stage | Single-Stage |
| 속도 | **매우 빠름** | 느림 | 빠름 |
| 정확도 | 높음 | 매우 높음 | 보통 |
| 실무 활용 | **최고** | 연구 중심 | 제한적 |

---

## 11. 한 문장 요약

> **YOLO는 “객체 탐지를 실시간 서비스가 가능한 문제로 바꿔버린 모델”이다.**

---

## 12. 참고 자료

- YOLOv1 논문  
  https://arxiv.org/pdf/1506.02640.pdf
- YOLOv3 논문  
  https://arxiv.org/pdf/1804.02767.pdf
- Ultralytics YOLO 공식 문서  
  https://docs.ultralytics.com

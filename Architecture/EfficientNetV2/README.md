**EfficientNetV2: Smaller Models and Faster Training**  
(Mingxing Tan, Quoc V. Le, Google, 2021)

---

## 1. 연구 배경 (Motivation)
EfficientNet(V1)은 **추론 효율(FLOPs 대비 정확도)** 은 매우 뛰어났지만,  
모델이 커질수록 **학습 속도가 느려지는 문제**가 있었다.

### V1의 한계
- MBConv 구조는 **메모리 접근 비용이 커서 학습이 느림**
- 고해상도 입력 + 깊은 네트워크 → **훈련 시간 급증**
- 대규모 데이터/대형 모델 학습에 비효율적

👉 논문의 질문:
> “추론뿐 아니라 **학습까지 빠른 EfficientNet**을 만들 수 없을까?”

---

## 2. EfficientNetV2의 핵심 목표
EfficientNetV2는 다음을 동시에 달성하는 것을 목표로 한다.

- ✅ **더 빠른 학습(training speed)**
- ✅ **더 작은 모델 크기**
- ✅ **기존 EfficientNet 수준 또는 그 이상의 정확도**

---

## 3. 핵심 개선 아이디어 ①: Fused-MBConv

### 기존 MBConv (V1)
- 1×1 Conv → Depthwise Conv → 1×1 Conv
- 파라미터는 적지만 **메모리 접근이 잦음**

### Fused-MBConv (V2)
- 초기 stage에서
  - **1×1 + Depthwise 구조를 하나의 일반 Conv로 결합**
- 결과:
  - GPU/TPU에서 **학습 속도 대폭 개선**
  - 초기 feature 학습에 더 적합

👉 전략:
- **초기 stage**: Fused-MBConv
- **후반 stage**: 기존 MBConv 유지

<img src="./images/mbc_vs_fused_mbc.png" width="400"/>

---

## 4. 핵심 개선 아이디어 ②: Progressive Learning

EfficientNetV2는 학습 과정에서  
**한 번에 큰 모델을 쓰지 않고 점진적으로 키우는 방식**을 제안한다.

### Progressive Learning이란?
학습이 진행되면서 점진적으로:
- 입력 해상도 ↑
- Regularization 강도 ↓ (Dropout 등)
- 네트워크 복잡도 ↑

### 효과
- 초기 학습 안정성 ↑
- 전체 학습 시간 ↓
- 대규모 데이터셋에서 수렴 속도 개선

<img src = "./images/progressive_learning.png" width="500"/>

---

## 5. EfficientNetV2 모델 패밀리

| 모델 | 특징 | 사용 목적 |
|---|---|---|
| EfficientNetV2-S | 작고 빠름 | 모바일/경량 분류 |
| EfficientNetV2-M | 균형형 | 실무 표준 |
| EfficientNetV2-L | 대형 모델 | 최고 성능 추구 |

👉 V1(B0~B7)보다 **모델 수는 줄이고 실용성 강화**

---

## 6. 실험 결과 (Results)

### ImageNet 기준 주요 성과
- **같은 정확도에서**
  - 학습 속도 **최대 11× 빠름**
- **같은 학습 시간에서**
  - 더 높은 정확도 달성

### 정리
- V2는 단순히 “더 정확한 모델”이 아니라
- **“더 빨리 학습되는 모델”**

<img src = "./images/efficientnetv2_result1.png" width="400"/>

<img src = "./images/efficientnetv2_result2.png" width="700"/>

---

## 7. 논문의 주요 기여 (Contributions)

1. **Fused-MBConv**로 학습 병목 해결
2. **Progressive Learning**이라는 실용적 학습 전략 제안
3. 추론 + 학습 효율을 모두 고려한 CNN 설계
4. 대규모 학습 환경에 적합한 EfficientNet 진화형 제시

---

## 8. EfficientNet(V1) vs EfficientNetV2 비교

| 구분 | EfficientNet | EfficientNetV2 |
|---|---|---|
| 주 목표 | 추론 효율 | **학습 + 추론 효율** |
| 블록 | MBConv | **Fused-MBConv + MBConv** |
| 학습 속도 | 느림 | **빠름** |
| 대규모 학습 | 비효율 | **효율적** |
| 실무 적합성 | 보통 | **높음** |

---

## 9. 한계 및 이후 흐름
- Transformer 계열(ViT, Swin) 등장으로
  - SOTA 경쟁은 점차 Transformer 중심으로 이동
- 하지만 EfficientNetV2는 여전히:
  - 경량·고효율 CNN 영역의 **강력한 기준 모델**

---

## 10. 한 문장 요약
> **EfficientNetV2는 “EfficientNet을 실제 대규모 학습 환경에 맞게 완성시킨 모델”이다.**

---

## 11. 참고 링크

※ 논문 원문
https://arxiv.org/pdf/2104.00298.pdf

※ 논문 소개 블로그
https://deep-learning-study.tistory.com/567

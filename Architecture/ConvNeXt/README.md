# ConvNeXt: A ConvNet for the 2020s  
*(Zhuang Liu et al., Meta AI, 2022)*

---

## 1. 연구 배경 (Motivation)

2020년 이후 Vision Transformer(ViT) 계열 모델이  
ImageNet 및 다양한 Vision Task에서 SOTA를 달성하였다.

그러나 질문이 생긴다:

> “ConvNet은 정말 Transformer에 밀려서 끝난 것인가?”

논문의 핵심 문제의식:

- ViT의 성능은 구조 때문인가?
- 아니면 학습 전략과 설계 현대화 때문인가?
- ConvNet을 Transformer 설계 철학에 맞게 업데이트하면 어떻게 될까?

👉 목표:
**ResNet을 현대화하여 Transformer 수준의 성능을 내는 CNN을 만들자**

---

## 2. 핵심 아이디어

ConvNeXt는 다음을 수행했다:

- ResNet을 기반으로
- Transformer에서 사용된 설계 요소를 점진적으로 도입
- ConvNet을 "2020년대 스타일"로 재설계

결론:

> ConvNet도 충분히 Transformer 수준의 성능을 낼 수 있다.

---

## 3. 전체 아키텍처 구조

### 📍 논문 기준 이미지
- Figure 3 (논문 Page 5)

<img src="./images/convnext_architecture.png" width="700"/>

### 구조 개요

- Stem (4×4 Conv, stride 4)
- 4-stage hierarchical structure
- 각 stage는 ConvNeXt Block 반복
- Global Average Pooling + Linear Head

ResNet과 유사한 Stage 구조지만 내부 Block이 다름

---

## 4. ConvNeXt Block 구조

### 📍 논문 기준 이미지
- Figure 4 (논문 Page 6)

<img src="./images/convnext_block.png" width="600"/>

### Block 구성

1. Depthwise Conv (7×7)
2. LayerNorm (BatchNorm 제거)
3. 1×1 Conv (Expansion)
4. GELU
5. 1×1 Conv (Projection)
6. Residual Connection

### 주요 변화

| 항목 | ResNet | ConvNeXt |
|------|--------|----------|
| Conv Kernel | 3×3 | **7×7 depthwise** |
| Norm | BatchNorm | **LayerNorm** |
| Activation | ReLU | **GELU** |
| Structure | Bottleneck | Transformer 유사 |

---

## 5. Transformer에서 차용한 설계 요소

ConvNeXt는 다음 Transformer 요소를 도입했다:

- Large Kernel (7×7)
- LayerNorm
- GELU
- Inverted Bottleneck 스타일 확장
- Separate Downsampling Layer

👉 CNN을 Transformer 철학으로 재해석

---

## 6. 모델 패밀리

| 모델 | Params | FLOPs | 특징 |
|------|--------|-------|------|
| ConvNeXt-T | ~29M | ~4.5G | 경량 |
| ConvNeXt-S | ~50M | ~8.7G | 표준 |
| ConvNeXt-B | ~89M | ~15G | 고성능 |
| ConvNeXt-L | ~198M | ~34G | 대형 |
| ConvNeXt-XL | ~350M | ~60G | 최고성능 |

---

## 7. ImageNet 성능 결과

### 📍 논문 기준 이미지
- Table 1 / Figure 5 (논문 Page 7~8)

<img src="./images/convnext_results.png" width="700"/>

### 주요 결과

- ConvNeXt-B:
  - ImageNet-1K Top-1: 83.8%
- Swin Transformer와 동급
- EfficientNet 대비 경쟁력 있음

👉 ConvNet의 재부활

---

## 8. ConvNeXt의 의의

1. ConvNet이 여전히 강력함을 증명
2. Transformer와 CNN의 경계를 흐림
3. Backbone으로 매우 우수
   - Detection
   - Segmentation
   - Self-Supervised Learning

---

## 9. ConvNeXt vs ResNet vs Swin

| 항목 | ResNet | Swin Transformer | ConvNeXt |
|------|--------|-----------------|-----------|
| 구조 | 전통 CNN | Transformer | Modernized CNN |
| Locality | 강함 | 상대적 약함 | 강함 |
| Global Modeling | 제한적 | 강함 | 간접적 |
| 실무 활용 | 높음 | 높음 | **매우 높음** |

---

## 10. 한 문장 요약

> ConvNeXt는 "Transformer 시대에도 살아남은 현대화된 CNN"이다.

---

## 11. 참고 링크

- 논문 원문  
  https://arxiv.org/pdf/2201.03545.pdf

- 공식 GitHub  
  https://github.com/facebookresearch/ConvNeXt


# RegNet: Designing Network Design Spaces  
*(Ilija Radosavovic et al., Meta(Facebook AI), 2020)*

---

## 1. 연구 배경 (Motivation)

CNN 아키텍처 설계는 오랫동안 **사람의 직관 + 시행착오**에 의존해 왔다.

### 기존 흐름의 문제점
- ResNet, DenseNet, EfficientNet 등:
  - 구조가 점점 **복잡해짐**
  - 하이퍼파라미터가 많아 **이해·재현 어려움**
- NAS (Neural Architecture Search):
  - 성능은 좋지만
  - ❌ 탐색 비용이 매우 큼
  - ❌ 실무 적용 어려움

👉 논문의 질문:
> “**단순하면서도 일반화 가능한 CNN 설계 법칙**은 없을까?”

---

## 2. RegNet의 핵심 아이디어

**RegNet**은  
> “좋은 네트워크는 **규칙적인 구조(regulated structure)** 를 가진다”

라는 가설에서 출발한다.

### 핵심 개념
- 임의의 복잡한 구조 ❌
- **수식으로 정의 가능한 Network Design Space** ✅
- 깊이, 채널 수 변화가 **연속적이고 규칙적**

👉 결과:
- 단순하지만 강력한 CNN 패밀리 생성
- NAS 없이도 SOTA 근접 성능

---

## 3. Network Design Space 개념

<img src="./images/regnet_design_space.png" width="700"/>

### 기존 방식
- 네트워크 하나하나를 “개별 설계”

### RegNet 방식
- **네트워크의 ‘공간(space)’ 자체를 설계**
- 그 공간에서 다양한 모델을 자동 생성

👉 “모델을 설계”가 아니라  
👉 **“설계 법칙을 설계”**

---

## 4. RegNet의 핵심 구조 아이디어

### Stage-wise Channel Design

<img src="./images/regnet_stage_structure.png" width="600"/>

RegNet은 각 stage의 채널 수를  
다음과 같은 **단순한 선형 수식**으로 정의한다.

```
w_i = w_0 + k · i
```

- `w_i`: i번째 stage의 채널 수
- `w_0`: 초기 채널 수
- `k`: 증가 기울기

👉 복잡한 튜닝 없이 **규칙적 확장**

---

## 5. RegNet 아키텍처 구성

<img src="./images/regnet_architecture.png" width="700"/>

### 전체 구조
- Backbone은 **ResNet 계열과 유사**
- 구성 요소:
  - Stem
  - Stages (각 stage는 여러 Bottleneck block)
  - Head (Global Avg Pool + FC)

👉 구조는 단순하지만 **채널 분포가 다름**

---

## 6. RegNetX vs RegNetY

<img src="./images/regnetx_regnety.png" width="600"/>

| 구분 | RegNetX | RegNetY |
|---|---|---|
| SE Block | ❌ | ✅ |
| 정확도 | 높음 | **더 높음** |
| 연산량 | 적음 | 증가 |
| 실무 사용 | 빠른 모델 | 성능 중시 |

👉 RegNetY = RegNetX + Squeeze-and-Excitation

---

## 7. 모델 패밀리 예시

| 모델 | FLOPs | Params | 특징 |
|---|---|---|---|
| RegNetX-400MF | ~0.4G | ~5M | 초경량 |
| RegNetX-4.0GF | ~4G | ~22M | 표준 |
| RegNetY-16GF | ~16G | ~84M | 고성능 |

👉 모바일부터 서버까지 **일관된 스케일링**

---

## 8. 실험 결과 (ImageNet)

<img src="./images/regnet_results.png" width="700"/>

### 주요 성과
- NAS 기반 모델 대비:
  - **유사하거나 더 좋은 정확도**
- ResNet / EfficientNet 대비:
  - **구조 단순**
  - **재현성 높음**

👉 “복잡하지 않아도 강하다”

---

## 9. RegNet의 주요 기여 (Contributions)

1. **Network Design Space** 개념 정립
2. 수식 기반 CNN 설계 가능성 제시
3. NAS 의존도 감소
4. 단순·규칙·확장 가능한 CNN 패밀리 제안

---

## 10. RegNet vs ResNet vs EfficientNet

| 항목 | ResNet | EfficientNet | RegNet |
|---|---|---|---|
| 설계 방식 | 경험 기반 | Compound Scaling | **수식 기반** |
| 구조 복잡도 | 중 | 높음 | **낮음** |
| 재현성 | 높음 | 보통 | **매우 높음** |
| NAS 필요 | ❌ | ❌ | ❌ |

---

## 11. 한 문장 요약

> **RegNet은 “CNN 아키텍처를 ‘설계 대상’이 아니라 ‘설계 공간’으로 끌어올린 모델”이다.**

---

## 12. 참고 링크

- RegNet 원 논문  
  https://arxiv.org/pdf/2003.13678.pdf

- Meta AI RegNet 소개  
  https://ai.facebook.com/blog/designing-network-design-spaces/

- PyTorch RegNet 구현  
  https://pytorch.org/vision/stable/models/regnet.html

# CLIP: Learning Transferable Visual Models From Natural Language Supervision

**(Alec Radford et al., OpenAI, 2021)**

## 1. 연구 배경 (Motivation)
기존의 시각 지능 모델은 미리 정해진 카테고리(예: ImageNet의 1,000개 클래스) 내에서만 이미지를 분류할 수 있다는 **폐쇄적인 한계**가 있었습니다.

**당시 한계**
* 새로운 사물을 인식하려면 데이터를 다시 모으고 모델을 새로 학습해야 함 (**High Cost**)
* 텍스트(언어)와 이미지(시각)가 서로 독립적으로 학습됨
* 실제 환경(Out-of-distribution)에서의 적응력이 낮음

👉 **논문의 질문:** "수많은 인터넷 데이터로부터 **글과 그림의 관계를 스스로 학습**하여, 가르쳐주지 않은 사물도 척척 알아맞히는 모델을 만들 수 없을까?"

---

## 2. CLIP의 핵심 아이디어
CLIP은 **대조 학습(Contrastive Learning)**을 통해 이미지와 텍스트를 하나의 공통된 공간(Shared Embedding Space)에 매핑합니다.

**핵심 개념**
* **Dual Encoder:** 이미지 엔코더와 텍스트 엔코더가 각각 존재
* **Contrastive Pre-training:** 올바른 (이미지, 텍스트) 쌍은 가깝게, 틀린 쌍은 멀게 배치하도록 학습
* **Zero-shot Transfer:** 학습 단계에서 본 적 없는 클래스라도 텍스트 설명만 있으면 즉시 분류 가능



---

## 3. CLIP 전체 아키텍처 구조 (openai/clip-vit-base-patch32)
* **Image Encoder:** ViT-B/32 (Vision Transformer Base)
* **Text Encoder:** Transformer 기반 Masked Self-Attention
* **Matching:** 두 엔코더에서 나온 벡터의 **코사인 유사도(Cosine Similarity)**를 계산하여 가장 연관성이 높은 쌍을 찾음

---

## 4. Image Encoder (ViT-B/32) 상세
**역할**
* 이미지를 512차원의 특징 벡터(Embedding)로 변환합니다.

**구성 (Patch32)**
* 이미지를 **32x32 픽셀 크기의 패치**로 나누어 처리합니다.
* **특징:** Patch16 모델에 비해 패치 크기가 커서 세밀함은 다소 낮을 수 있으나, **추론 속도가 매우 빠르고 연산 효율성이 뛰어납니다.** (실시간 서비스에 적합)



---

## 5. 핵심 기법: Contrastive Learning
$N$개의 이미지와 $N$개의 텍스트 배치가 있을 때, $N$개의 진짜 쌍(Positive)의 유사도는 최대화하고, 나머지 $N^2 - N$개의 가짜 쌍(Negative)의 유사도는 최소화하도록 학습합니다. 이를 통해 모델은 단순한 '이름'이 아닌 '의미'를 이해하게 됩니다.

---

## 6. 주요 장점 및 단점
| 장점 | 단점 |
| :--- | :--- |
| **Zero-shot:** 별도 학습 없이 새로운 도메인 적용 가능 | **Fine-grained:** 아주 작은 물체 인식에는 한계가 있음 |
| **Efficient:** Patch32 기반으로 빠른 연산 속도 제공 | **Abstract:** 매우 복잡한 문장의 추상적 의미 파악이 어려울 수 있음 |
| **Robust:** 이미지의 노이즈나 각도 변화에 강인함 | **Bias:** 학습 데이터(인터넷)의 편향성이 포함될 수 있음 |

---

## 7. 활용 분야
* 🔍 **Semantic Search:** "사고 난 붉은색 승용차" 등 문장으로 이미지 검색
* 📸 **Zero-shot Classification:** 학습 데이터에 없던 새로운 차량 모델 분류
* 🎨 **Multimodal Embedding:** 이미지와 텍스트의 유사도를 이용한 추천 시스템 구축
* 🚗 **Insurance Tech:** 차량 파손 부위 설명과 이미지의 일치 여부 확인 (Underwriting 활용)

---

## 8. 참고 링크
* **Paper:** [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
* **Model Card:** [Hugging Face - clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32)
* **Official Repo:** [OpenAI CLIP GitHub](https://github.com/openai/CLIP)

---
### Citation
```bibtex
@inproceedings{radford2021learning,
  title={Learning Transferable Visual Models from Natural Language Supervision},
  author={Radford, Alec and others},
  booktitle={International conference on machine learning},
  year={2021}
}

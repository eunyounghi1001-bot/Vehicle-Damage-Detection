# ResNet(Residual Network)

ResNet(Residual Network)은 2015년 Microsoft Research에서 발표한 딥러닝 CNN(합성곱 신경망) 구조로, 층이 깊어질수록 학습이 어려워지는 문제를 해결하여 현대 컴퓨터 비전 모델의 기반이 되었습니다. 

### 1. 연구 배경
   - CNN 문제점: 네트워크가 깊어지면 '기울기 소실(Gradient Vanishing)' 문제로 인해 오히려 성능이 떨어지는 'Degradation Problem'이 발생
   - 원인: 기울기 소실/폭주, 최적화 난이도 증가
<img src="./images/cnn_error_20&56_layer.png" width="700"/>

### 2. ResNet 핵심 개념
   - 잔차 학습 (Residual Learning) ResNet의 가장 큰 특징은 Skip Connection(Shortcut Connection)
   - 입력값 \(x\)를 출력값에 직접 더해주는 \(H(x)=F(x)+x\) 구조를 사용.
     
<img src="./images/residual_learning_concept.png" width="400"/>

   - shortcut connection을 사용하여 입력과 출력을 이어줌(residual mapping)으로써 더 쉽게 최적화

<img src="./images/plain_vs_resnet_concept.png" width="600"/>

   - 모델은 입력과 출력의 차이(잔차, Residual)인 \(F(x)\)만 학습하면 되므로, 층이 매우 깊어져도 안정적인 학습이 가능

<img src="./images/plain_vs_resnet_error.png" width="800"/>

### 3. 주요 성과
   - ILSVRC 2015 우승: 152개 층을 쌓은 ResNet-152 모델로 **이미지 분류 대회에서 압도적인 성능**을 보임
   - 깊은 층 구성: 이전의 VGG(19층), GoogleNet(22층)을 넘어 수백 개 이상의 층을 쌓을 수 있음을 증명

### 4. 주요 버전 학습 파라미터 수에 따라 다양한 변형이 존재
   - ResNet-18 / 34: 비교적 가벼운 모델로 빠른 추론이 필요할 때 사용
   - ResNet-50 / 101 / 152: 연산 효율을 높이기 위해 Bottleneck 구조(1x1, 3x3, 1x1 합성곱 사용)를 채택하여 성능과 속도를 모두 향상

| 모델 | Depth | Residual Block 타입 | Stage 구성 (conv2_x~conv5_x) | 파라미터(대략) | 연산량 GFLOPs(대략) | 특징 요약 | 추천 사용처 |
|---|---:|---|---|---:|---:|---|---|
| ResNet-18 | 18 | BasicBlock (3×3, 3×3) | [2, 2, 2, 2] | ~11.7M | ~1.8 | 가볍고 빠른 베이스라인 | 데이터 적을 때 |
| ResNet-34 | 34 | BasicBlock (3×3, 3×3) | [3, 4, 6, 3] | ~21.8M | ~3.6 | 18 대비 성능↑, 여전히 비교적 가벼움 | 중간 규모 데이터 |
| ResNet-50 | 50 | Bottleneck (1×1, 3×3, 1×1) | [3, 4, 6, 3] | ~25.6M | ~4.1 | “표준”급 backbone, 전이학습 활용도 높음 | 실무 기본 선택지 |
| ResNet-101 | 101 | Bottleneck (1×1, 3×3, 1×1) | [3, 4, 23, 3] | ~44.5M | ~7.8 | 더 깊고 강력(정확도 상한↑) | 성능 우선(서버) |
| ResNet-152 | 152 | Bottleneck (1×1, 3×3, 1×1) | [3, 8, 36, 3] | ~60.2M | ~11.6 | 매우 무겁지만 깊이 상한 | 성능 극대화(추론 비용 감수) |

**※ 빠른 선택 가이드**

- **속도/가벼움 최우선**: ResNet-18
- **가성비(속도·성능 균형)**: ResNet-34 또는 **ResNet-50**
- **성능 최우선(서버/시간 여유)**: ResNet-101
- **특수하게 매우 깊은 모델이 필요**: ResNet-152

### 5. 참고
   - 논문 원문: Deep Residual Learning for Image Recognition
   - 코드 구현: PyTorch ResNet 가이드 또는 TensorFlow ResNet API를 통해 사전 학습된 모델 사용


※ 논문 원문

https://arxiv.org/pdf/1512.03385.pdf  

※ 논문 소개 블로그

https://wjunsea.tistory.com/99#google_vignette  
https://devs0n.tistory.com/185

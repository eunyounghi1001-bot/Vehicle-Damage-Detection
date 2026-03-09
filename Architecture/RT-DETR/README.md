🚀 RT-DETR: DETRs Beat YOLOs on Real-time Object Detection
(Wenyu Lv et al., Baidu, 2023)

1. 연구 배경 (Motivation)
기존의 객체 탐지 시장은 YOLO가 지배하고 있었으나, YOLO는 **NMS(Non-Maximum Suppression)**라는 후처리가 필수적이라 최적화가 어렵고 부정확한 경우가 있었습니다. 반면, DETR은 NMS가 필요 없는 혁신적인 구조였지만 연산량이 너무 많아 '실시간(Real-time)'으로 쓰기엔 너무 느렸습니다.

당시 한계

YOLO: NMS 후처리로 인한 지연 시간 및 하이퍼파라미터 의존성

DETR: 트랜스포머의 높은 연산 비용으로 인해 실시간 추론 불가

👉 질문: "DETR의 정확도를 유지하면서 YOLO보다 빠른 모델은 없을까?"

2. RT-DETR의 핵심 아이디어
RT-DETR은 세계 최초로 실시간 추론이 가능한 End-to-End Object Detector입니다.

핵심 개념

Hybrid Encoder: 연산량이 많은 Self-Attention을 필요한 곳에만 선택적으로 사용하여 속도 개선

Uncertainty-aware Query Selection: 가장 '확실한' 객체 후보군(Query)만 골라내어 디코더의 부담을 줄임

No NMS: 후처리가 필요 없어 지연 시간이 일정하고 전체 시스템이 단순함

👉 결과: 실시간 객체 탐지 SOTA(State-of-the-Art) 달성. "드디어 DETR이 YOLO를 속도와 정확도 모두에서 앞서기 시작함"

3. RT-DETR 전체 아키텍처 구조
구조 개요

Backbone: 특징 추출 (ResNet 또는 HGNetv2 사용)

Hybrid Encoder: 효율적인 다중 스케일 특징 결합 (AIFI + CCFM)

Transformer Decoder: 최종 객체 위치 및 클래스 예측

4. Hybrid Encoder (핵심 기술)
역할
이미지의 여러 크기 특징(Feature Map)을 섞어주되, 계산 속도를 극대화합니다.

구성

AIFI (Attention-based Intra-scale Feature Interaction): 가장 높은 수준의 특징맵(S5)에만 Self-attention을 적용하여 중복 계산 방지

CCFM (CNN-based Cross-scale Feature-fusion Module): 서로 다른 크기의 특징들을 융합할 때 효율적인 CNN 연산 사용

👉 효과: 트랜스포머의 장점(전역 이해)은 챙기고 단점(연산량)은 CNN으로 보완

5. Uncertainty-aware Query Selection
역할
디코더에 들어갈 초기 쿼리(Query)를 선택할 때 '정확도'뿐만 아니라 **'확신도'**를 함께 고려합니다.

효과
모델이 물체라고 확신하는 부분에 집중하게 만들어, 훨씬 적은 쿼리로도 정확한 결과를 도출합니다.

6. 주요 장점 및 단점
7. 활용 분야
🏎️ 자율 주행: 실시간 주변 차량 및 보행자 정밀 탐지

🛡️ 보안 시스템: CCTV 영상 내 침입자 실시간 감시

🚗 차량 파손 정밀 진단: 대량의 차량 사진에서 파손 부위 고속 적중

8. 한 문장 요약
"RT-DETR은 NMS의 굴레를 벗어던지고 트랜스포머의 성능을 실시간의 영역으로 끌어올린 차세대 객체 탐지기이다."

9. 참고 링크
RT-DETR 원 논문 (arXiv)

GitHub Official (Baidu)


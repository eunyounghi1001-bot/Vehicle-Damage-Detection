# Vehicle Damage Inspector

딥러닝을 활용한 차량 파손 탐지 및 분류 프로젝트 스터디

## theory

| Topic | Status | Report |
| :---| :--- | :--- |
| object detection basic | ✅ Done | [상세보기](./theory/01_Object_Detection/README.md) |
| YOLO| ✅ Done | [상세보기](./theory/02_YOLO/README.md) |
| 이미지분석기본개념 | ✅ Done | [상세보기](./theory/이미지분석기본개념.md) |

| 유형 | 명칭 | 발표 연도 | 핵심 아이디어 | 상세설명 |
|---|---|---:|---|---|
| 이미지 분류 | ResNet | 2015 | Skip Connection(Residual Learning)을 도입해 깊은 CNN에서도 학습 안정성 확보, Degradation 문제 해결 | [상세보기](./Architecture/ResNet/README.md) |
| 이미지 분류 | EfficientNet | 2019 | 깊이·너비·해상도를 동시에 균형 있게 확장하는 **Compound Scaling**으로 연산 효율 극대화 | [상세보기](./Architecture/EfficientNet/README.md) |
| 이미지 분류 | RegNet | 2020 | CNN 채널·깊이 설계를 수식으로 정의해 예측 가능한 고효율 backbone 제시 |  |
| 이미지 분류 | Vision Transformer (ViT) | 2020 | 이미지를 패치 단위 토큰으로 변환해 **Transformer Encoder**로 전역 관계를 직접 학습 | [상세보기](./Architecture/Vision_Transformer/README.md) |
| 이미지 분류 / 탐지 / 세그 | Swin Transformer | 2021 | 윈도우 기반 Self-Attention으로 계산량을 줄이고, CNN처럼 계층적(stage) 구조 유지 |  |
| 이미지 분류 | EfficientNetV2 | 2021 | **Fused-MBConv + Progressive Learning**으로 학습 속도와 효율을 동시에 개선 | [상세보기](./Architecture/EfficientNetV2/README.md) |
| 이미지 분류 | DeiT (Data-efficient ViT) | 2021 | 지식 증류를 통해 대규모 데이터 없이 ViT 학습 가능 |  |
| 이미지 분류 | ConvNeXt | 2022 | ResNet 구조를 유지하면서 Transformer 학습 전략을 적용해 CNN SOTA 달성 |  |
| 이미지 분류 | MaxViT | 2022 | CNN과 Window/Global Attention을 결합한 Hybrid Transformer |  |
| 객체 탐지 | YOLO (You Only Look Once) | 2016 | 객체 탐지를 하나의 end-to-end 회귀 문제로 정의해 **실시간 객체 탐지** 달성 |  |
| 객체 탐지 / 세그 | Mask R-CNN | 2017 | 객체 탐지와 픽셀 단위 마스크를 동시에 수행하는 2-stage 구조 |  |
| 세그멘테이션 | U-Net | 2015 | Encoder–Decoder 구조와 Skip Connection으로 위치 정보와 의미 정보를 결합한 픽셀 단위 분할 |  |
| 세그멘테이션 | DeepLabV3+ | 2018 | Atrous Convolution으로 다중 해상도 문맥 정보를 효과적으로 통합 |  |

## Project Roadmap & Study Log

| Subject| WHO | Version | Topic | Model | Data | Report |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Data Set** |DJ| **Ver0** | 데이터셋 구축 | - | Damaged 1,200 | [상세보기](./notebooks/00_Data_Preparation/README.md) |
| **Data Set** |DJ| **Ver1** | 데이터셋 구축 | - | Damaged 12,000  | [상세보기](./notebooks/00_Data_Preparation_ver2/README.md) |
| **Car Detection** |DJ| **Ver2** | 차량 인식 1st | YOLOv8 | Damaged 1,200 |  [상세보기](./notebooks/02_Car_Detection_FineTuning_1st/README.md) | |
| **Car Detection** |DJ| **Ver3** | 차량 인식 2nd | YOLOv8 | Damaged 1,200(hybrid) | [상세보기](./notebooks/03_Car_Detection_FineTuning_2nd/README.md) | |
| **Car Detection** |DJ| **Ver6** | 차량 인식 5th | YOLOv8 | Damaged 12,000 | [상세보기](./notebooks/06_Car_Detection_FineTuning_5th/README.md) | |
| **Damage Detection** |DJ| **Ver3** | 파손 인식 3rd | YOLOv8 | Damaged 12,000 | [상세보기](./notebooks/07_Damage_Detection_FineTuning_3rd/README.md) | |
| **Damage Detection** |JR| **Ver1** | 다양한 데이터셋 활용 | YOLOv8, Resnet18 | ✅ Done | [상세보기](./notebooks/다양한데이터셋활용/README.md) | |
| **Damage Categorization** |JR| **Ver1** | 파손 여부 파인튜닝 | YOLOv8s | ✅ Done | [상세보기](./JR/week_03/README.md) | |
| **Damage Categorization** |DJ| **Ver1** | 파손 유형 1st | YOLOv8 | Damaged 12,000 | [상세보기](./notebooks/08_Damage_Classification_FineTuning_1st/README.md) | |
| **Damage Segmentation** |DJ| **Ver1** | 파손 부위 1st | YOLOv8x_Seg,Unet | Damaged 12,000 | [상세보기](./notebooks/09_Car_Damage_Segmentation_1st/README.md) | |


## Tech Stack
* Python 3.10
* PyTorch
* Ultralytics YOLOv8

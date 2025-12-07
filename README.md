# Vehicle Damage Inspector

딥러닝을 활용한 차량 파손 탐지 및 분류 프로젝트 스터디

## Project Roadmap & Study Log

| Stage | Topic | Model | Status | Report |
| :--- | :--- | :--- | :--- | :--- |
| **Step 0** | 데이터셋 구축 | AI-Hub + COCO | ✅ Done | [상세보기](./notebooks/00_Data_Preparation/README.md) |
| **Step 1** | 차량 인식 베이스라인 | YOLOv8x (Pre-trained) | ✅ Done | [상세보기](./notebooks/01_Baseline_Inference/README.md) |
| **Step 2** | 차량 인식 파인튜닝_1st | YOLOv8 Custom | ✅ Done |  [상세보기](./notebooks/02_Car_Detection_FineTuning_1st/README.md) | |
| **Step 3** | 차량 인식 파인튜닝_2nd | YOLOv8 Custom | ✅ Done | - |
| **Step 4** | 파손 부위 분류 | Segmentation | 📅 Planned | - |

## Tech Stack
* Python 3.10
* PyTorch
* Ultralytics YOLOv8

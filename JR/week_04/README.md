# EDA(Train images)


### [1] BASIC FILE STATS

- Image folder         : ./(share)HDMF_AUTO_SPOKE/DATA/04_DATA/balanced_dataset_split/train/images
- Num images           : 8,412
- Total size           : 1.04 GB (1,114,622,186 bytes)
- Avg file size        : 129.40 KB
- Median file size     : 119.24 KB
- Min/Max file size    : 21.85 KB / 1.24 MB
- Extension distribution:
    .jpg : 8,412


### [2] SAMPLE IMAGES (5x2 grid)










# YOLOv8 Detection Evaluation Summary (test)

## 1) Run / Environment
- **Weight**: `/content/gdrive/MyDrive/01.DS Part/99.Study/01.Vehicle_Damage_Detection/Week_04/yolov8s/_trained_weights/parts32_20260129_035127_best.pt`
- **Ultralytics**: 8.4.8
- **Python / Torch / CUDA**: Python 3.12.12, torch 2.9.0+cu126, CUDA:0
- **GPU**: NVIDIA A100-SXM4-80GB (81222MiB)
- **Model**: 73 layers, 11,137,968 params, 28.5 GFLOPs

---

## 2) Dataset (test) Overview
- **Dataset path**: `/content/dataset_local/test`
- **Images**: 1,800
- **Instances (GT boxes)**: 2,617
- **Cache created**: `/content/dataset_local/test/labels.cache`
- **I/O**: Fast image access ✅ (read ~1511.7 MB/s, avg size ~117.3 KB)

---

## 3) Overall Metrics (All Classes)
| Metric | Value |
|---|---:|
| Precision (P) | 0.493 |
| Recall (R) | 0.476 |
| mAP@0.5 | 0.407 |
| mAP@0.5:0.95 | 0.364 |
| Fitness | 0.364 |

---

## 4) Per-Class Metrics
> Columns: **Images**(=class images), **Instances**, **P**, **R**, **mAP50**, **mAP50-95**

| Class | Images | Instances | P | R | mAP50 | mAP50-95 |
|---|---:|---:|---:|---:|---:|---:|
| all | 1800 | 2617 | 0.493 | 0.476 | 0.407 | 0.364 |
| part_0 | 175 | 175 | 0.568 | 0.709 | 0.639 | 0.577 |
| part_1 | 477 | 477 | 0.827 | 0.916 | 0.919 | 0.859 |
| part_2 | 56 | 56 | 0.407 | 0.661 | 0.474 | 0.437 |
| part_3 | 109 | 109 | 0.500 | 0.560 | 0.574 | 0.550 |
| part_4 | 36 | 36 | 0.274 | 0.278 | 0.298 | 0.252 |
| part_5 | 167 | 168 | 0.595 | 0.649 | 0.685 | 0.629 |
| part_6 | 707 | 707 | 0.848 | 0.958 | 0.930 | 0.880 |
| part_7 | 83 | 83 | 0.541 | 0.752 | 0.707 | 0.661 |
| part_8 | 16 | 16 | 0.367 | 0.544 | 0.459 | 0.454 |
| part_9 | 70 | 70 | 0.534 | 0.686 | 0.618 | 0.578 |
| part_10 | 53 | 53 | 0.459 | 0.641 | 0.513 | 0.471 |
| part_11 | 62 | 62 | 0.390 | 0.475 | 0.345 | 0.265 |
| part_12 | 114 | 114 | 0.571 | 0.712 | 0.644 | 0.541 |
| part_13 | 102 | 102 | 0.525 | 0.657 | 0.633 | 0.531 |
| part_14 | 43 | 43 | 0.303 | 0.651 | 0.431 | 0.365 |
| part_15 | 37 | 37 | 0.311 | 0.351 | 0.232 | 0.193 |
| part_16 | 32 | 32 | 0.369 | 0.625 | 0.407 | 0.351 |
| part_17 | 6 | 6 | 0.142 | 0.306 | 0.109 | 0.108 |
| part_18 | 45 | 46 | 0.409 | 0.587 | 0.507 | 0.473 |
| part_19 | 40 | 40 | 0.438 | 0.525 | 0.408 | 0.335 |
| part_20 | 68 | 68 | 0.346 | 0.529 | 0.428 | 0.372 |
| part_21 | 32 | 32 | 0.246 | 0.375 | 0.230 | 0.211 |
| part_22 | 49 | 49 | 0.422 | 0.633 | 0.413 | 0.366 |
| part_23 | 24 | 24 | 0.384 | 0.495 | 0.416 | 0.379 |
| part_24 | 3 | 3 | 0.000 | 0.000 | 0.036 | 0.022 |
| part_26 | 2 | 2 | 1.000 | 0.000 | 0.000 | 0.000 |
| part_27 | 1 | 1 | 0.000 | 0.000 | 0.142 | 0.057 |
| part_29 | 1 | 1 | 1.000 | 0.000 | 0.000 | 0.000 |
| part_30 | 1 | 1 | 1.000 | 0.000 | 0.000 | 0.000 |
| part_31 | 4 | 4 | 1.000 | 0.000 | 0.000 | 0.000 |

---

## 5) Speed (per image)
| Stage | Time |
|---|---:|
| preprocess | 0.5 ms |
| inference | 1.2 ms |
| postprocess | 0.8 ms |

---

## 6) Quick Notes
- Strong classes: **part_6**, **part_1** (high P/R and high mAP)
- Very low-sample classes (e.g., part_24/26/27/29/30/31) show unstable metrics (often R=0).
- Results saved to: `/content/runs/detect/val`

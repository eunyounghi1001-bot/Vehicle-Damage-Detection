import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import os

# --- 설정 및 모델 로드 (캐싱을 통해 속도 향상) ---
@st.cache_resource
def load_models():
    # YOLO 로드
    car_model = YOLO('yolov8l.pt') 
    
    # CLIP 로드 (경로가 없을 경우를 대비해 예외처리나 기본 모델 설정 필요)
    model_path = "./fine_tuned_car_clip"
    if os.path.exists(model_path):
        clip_model = CLIPModel.from_pretrained(model_path)
        clip_processor = CLIPProcessor.from_pretrained(model_path)
    else:
        # 학습된 모델이 없을 경우 기본 모델 사용
        clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        
    device = "cuda" if torch.cuda.is_available() else "cpu"
    clip_model.to(device)
    return car_model, clip_model, clip_processor, device

car_model, clip_model, clip_processor, device = load_models()

DIRECTION_LABELS = [
    "front", "rear", "left", "right",
    "front_driver", "front_passenger", "rear_driver", "rear_passenger"
]
PROMPT_LABELS = [f"a photo of the {label} of a car" for label in DIRECTION_LABELS]

# --- UI 레이아웃 ---
st.title("🚗 차량 부위 및 구도 판별기")
st.write("이미지를 업로드하면 차량의 방향과 촬영 상태를 분석합니다.")

uploaded_file = st.file_uploader("차량 사진을 업로드하세요", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # 이미지 읽기
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img.shape

    # [Step 1] YOLO 탐지
    results = car_model(img, conf=0.15, imgsz=640)
    annotated_img = results[0].plot()
    annotated_img_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)

    found_car = False
    for result in results:
        target_boxes = [box for box in result.boxes if box.cls in [0, 2, 5, 7]] # 0: person인데 car는 보통 2번임 (모델에 따라 확인 필요)

        if not target_boxes:
            continue
        
        found_car = True
        # [Step 2] 메인 차량 추출
        main_box = max(target_boxes, key=lambda b: (b.xyxy[0][2] - b.xyxy[0][0]) * (b.xyxy[0][3] - b.xyxy[0][1]))
        x1, y1, x2, y2 = map(int, main_box.xyxy[0].tolist())
        
        # [Step 3] CLIP 방향 판별
        cropped_car = img_rgb[max(0, y1):min(h, y2), max(0, x1):min(w, x2)]
        pil_img = Image.fromarray(cropped_car)
        
        inputs = clip_processor(text=PROMPT_LABELS, images=pil_img, return_tensors="pt", padding=True).to(device)
        with torch.no_grad():
            outputs = clip_model(**inputs)
        
        probs = outputs.logits_per_image.softmax(dim=1)
        best_idx = probs.argmax().item()
        detected_direction = DIRECTION_LABELS[best_idx]

        # [Step 4] 프레임 판정
        is_cropped = x1 < 15 or y1 < 15 or x2 > w - 15 or y2 > h - 15
        area_ratio = ((x2 - x1) * (y2 - y1)) / (w * h)
        status = "✅ SUCCESS" if not is_cropped and 0.25 < area_ratio < 0.85 else "⚠️ REJECT"

        # --- 결과 표시 ---
        col1, col2 = st.columns(2)
        with col1:
            st.image(annotated_img_rgb, caption="Detection Result", use_column_width=True)
        
        with col2:
            st.subheader(f"판정 결과: {status}")
            st.write(f"**방향:** {detected_direction}")
            st.write(f"**영역 비율:** {area_ratio:.3f}")
            st.write(f"**잘림 여부:** {'Yes' if is_cropped else 'No'}")
            
            if status == "⚠️ REJECT":
                st.warning("프레임이 잘렸거나 구도가 부적절합니다. 다시 촬영해주세요.")
            else:
                st.success(f"이 사진은 차량의 {detected_direction} 부위입니다.")
        break # 메인 차량 하나만 처리

    if not found_car:
        st.error("차량을 찾을 수 없습니다.")
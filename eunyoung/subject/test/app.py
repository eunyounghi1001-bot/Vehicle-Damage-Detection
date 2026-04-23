import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import os

# 페이지 설정
st.set_page_config(page_title="차량 외관 분석기", layout="centered")
st.title("🚗 차량 방향 및 프레임 분석")
st.write("사진을 업로드하면 AI가 차량의 방향과 구도를 분석합니다.")

# 모델 로드 (캐싱을 통해 속도 향상)
@st.cache_resource
def load_models():
    car_model = YOLO('yolov8m.pt')
    clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    return car_model, clip_model, clip_processor

car_model, clip_model, clip_processor = load_models()

DIRECTION_LABELS = ["front", "rear", "left side", "right side", "front-left corner", "front-right corner", "rear-left corner", "rear-right corner"]
PROMPT_LABELS = [f"a photo of the {label} of a car" for label in DIRECTION_LABELS]

uploaded_file = st.file_uploader("차량 사진을 업로드하세요", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # 이미지 변환
    image = Image.open(uploaded_file)
    img = np.array(image.convert('RGB'))
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    h, w, _ = img_bgr.shape

    with st.spinner('AI 분석 중...'):
        results = car_model(img_bgr, conf=0.15, imgsz=640)
        
        if results[0].boxes:
            # 메인 차량 추출 및 방향 판별
            main_box = max(results[0].boxes, key=lambda b: (b.xyxy[0][2] - b.xyxy[0][0]) * (b.xyxy[0][3] - b.xyxy[0][1]))
            x1, y1, x2, y2 = map(int, main_box.xyxy[0].tolist())
            
            cropped_car = image.crop((x1, y1, x2, y2))
            inputs = clip_processor(text=PROMPT_LABELS, images=cropped_car, return_tensors="pt", padding=True)
            
            with torch.no_grad():
                outputs = clip_model(**inputs)
            
            probs = outputs.logits_per_image.softmax(dim=1)
            detected_direction = DIRECTION_LABELS[probs.argmax().item()]

            # 프레임 판정
            is_cropped = x1 < 15 or y1 < 15 or x2 > w - 15 or y2 > h - 15
            area_ratio = ((x2 - x1) * (y2 - y1)) / (w * h)
            status = "✅ 성공" if not is_cropped and 0.25 < area_ratio < 0.85 else "⚠️ 주의"

            # 결과 화면 출력
            st.image(results[0].plot()[:, :, ::-1], caption="AI 분석 결과")
            
            col1, col2 = st.columns(2)
            col1.metric("판정 결과", status)
            col1.metric("감지된 방향", detected_direction)
            
            col2.write(f"**상세 메시지:** \n이 사진은 차량의 {detected_direction} 부위입니다.")
            if is_cropped:
                col2.error("차량이 프레임 밖으로 잘렸습니다.")
        else:
            st.error("차량을 찾을 수 없습니다. 다시 촬영해 주세요.")
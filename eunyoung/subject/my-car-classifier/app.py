import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os

# 1. 페이지 설정
st.set_page_config(page_title="차량 8면 자동 분류기", layout="wide")
st.title("🚗 차량 외관 부위 자동 분류 시스템")
st.write("사진을 올리면 YOLOv8 모델이 8개 부위로 자동 분류합니다. (최대 20장)")

# 2. 모델 로드 (캐싱하여 속도 향상)
@st.cache_resource
def load_model():
    # 학습한 best.pt 파일 경로를 지정하세요
    return YOLO('train_result/weights/best.pt')

model = load_model()
class_names = ['front', 'front_left', 'front_right', 'left', 'rear', 'rear_left', 'rear_right', 'right']

# 3. 파일 업로드 (최대 20장)
uploaded_files = st.sidebar.file_uploader(
    "차량 사진을 업로드하세요", 
    type=['jpg', 'jpeg', 'png'], 
    accept_multiple_files=True
)

if uploaded_files:
    if len(uploaded_files) > 20:
        st.warning("최대 20장까지만 가능합니다. 상위 20장만 처리합니다.")
        uploaded_files = uploaded_files[:20]

    # 결과를 담을 딕셔너리 초기화
    classified_results = {name: [] for name in class_names}

    # 4. 추론 수행
    with st.spinner('AI가 부위를 분석 중입니다...'):
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            results = model.predict(source=img, save=False)
            
            # 예측 결과 가져오기
            probs = results[0].probs
            top1_idx = probs.top1
            label = class_names[top1_idx]
            conf = probs.top1conf.item()
            
            # 결과 저장 (이미지, 파일명, 신뢰도)
            classified_results[label].append({
                "image": img,
                "name": uploaded_file.name,
                "conf": conf
            })

    # 5. 화면에 8면 분리해서 뿌려주기
    st.divider()
    
    # 8개 클래스를 2행 4열 혹은 섹션별로 배치
    for i in range(0, len(class_names), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(class_names):
                label = class_names[i + j]
                with cols[j]:
                    st.subheader(f"📍 {label.upper()}")
                    images_in_class = classified_results[label]
                    
                    if not images_in_class:
                        st.info("해당 없음")
                    else:
                        for item in images_in_class:
                            st.image(item["image"], caption=f"{item['name']} ({item['conf']:.2%})", use_container_width=True)
                            st.divider()

else:
    st.info("왼쪽 사이드바에서 사진을 업로드해 주세요.")

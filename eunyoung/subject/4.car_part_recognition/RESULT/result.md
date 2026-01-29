👉 한 문장 요약



&nbsp;	“이 모델은 전체 차량 부위를 평균적으로 절반 정도는 맞춘다고 볼 수 있다.”



조금 더 풀면:



\* Images 1800

→ 검증에 사용된 이미지 수



\* Instances 2640

→ 실제 정답 박스(부위 개수)



\* Precision (P) = 0.533

&nbsp;	모델이 맞다고 예측한 것 중 53.3%가 진짜

&nbsp;	👉 오탐(false positive)이 꽤 있음



\* Recall (R) = 0.522

&nbsp;	실제 부위 중 52.2%를 찾아냄

&nbsp;	👉 절반 정도는 놓침



\* mAP@50 = 0.469

&nbsp;	IoU 0.5 기준 평균 정확도

&nbsp;	👉 PoC·초기 모델로는 이해 가능한 수준



\* mAP@50–95 = 0.427

&nbsp;	IoU를 0.5~0.95까지 엄격하게 본 평균

&nbsp;	👉 박스 위치 정밀도는 아직 부족



📌 결론 (전체 기준)

“실무에 바로 자동화 투입은 어렵고, 보조 판단용 / 필터링용 AI 수준”



**우선순위 제안**

1\. ❌ Instances 10 미만 클래스 → 과감히 제거 or 통합

2\. 🔄 좌/우 통합 (Headlight, Wheel, Mirror 등)

3\. 🎯 “UW 의사결정에 필요한 핵심 부위만 남기기”

&nbsp;	Front / Rear bumper

&nbsp;	Fender

&nbsp;	Door

&nbsp;	Bonnet / Trunk


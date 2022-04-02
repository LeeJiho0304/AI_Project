# 인공지능 기반 식단 관리 서비스 앱 sixsense (프론트엔드)

## 1. Project 소개
### 사용자의 한 끼 식사 이미지를 분석하여 건강한 식사를 돕는 식단 관리 인공지능 서비스 입니다
<p align="center">
<img src="https://user-images.githubusercontent.com/68880847/133614135-21254dc5-731a-4b82-b1b9-875ed5b53c7e.png" width="75%">
</p>

----------------
### - 식단 기록  
- 카메라로 사진을 찍거나 앨범에서 사진을 불러온 후 식사 시간과 날짜 입력

<img height="550" src="https://user-images.githubusercontent.com/68880847/133618265-64becb37-7b10-4ebd-8fca-d0a613aa0366.png"> <img height="550" src="https://user-images.githubusercontent.com/68880847/133618294-e9808a64-064d-4501-84d6-a6681098ca38.png">  

### - 음식 검출 검출  
- yolov4 모델을 사용하여 입력 이미지에 대해 객체 검출 후 검출 된 음식에 대한 영양정보 반환  
- 1인분을 기준으로 칼로리 측정

<img height="380" width="400" src="https://user-images.githubusercontent.com/68880847/133620673-463a507e-950b-4ac6-91b2-5dbc5a370e76.jpg"> <img height="380" src="https://user-images.githubusercontent.com/68880847/133618987-ff9d1336-ba5e-489d-bb9c-2f79f533dbd4.png">


### - 식단 추천
- 부족한 영양 정보를 토대로 새로운 식단 추천
<img height="550" src="https://user-images.githubusercontent.com/68880847/133621381-bebe61ac-1392-44c5-b8ba-6e81d6f03e5e.png">

### - 영양정보 통계
- 사용자가 지정한 기간 동안 섭취한 식단의 영양정보 시각화

<img height="550" src="https://user-images.githubusercontent.com/68880847/133622060-3b75c61a-31a8-4905-a9a3-b8046f1b09b5.png"> <img height="550" src="https://user-images.githubusercontent.com/68880847/133622078-5b64d30d-7b43-4c7b-bae4-874830ea570b.png">

<!-- ---------------- -->

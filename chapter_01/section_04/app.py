import streamlit as st
import numpy as np
from PIL import Image


# 위젯 출력
def myFunc(*args):
    res = 0
    for x in args:
        res += x
    st.write(f"계산 결과 = {res}")


# 1. 버튼 위젯 출력
st.write("### 버튼 위젯 출력")
st.button("클릭", key=1)
st.button("클릭", key=2, help="클릭하면 :blue[메시지]가 출력됩니다.")
st.button("클릭", key=3, on_click=myFunc, args=[1, 2, 3, 4, 5])
x = st.button("클릭~", key=4)

st.write(f"`{x}`")

# 2. 체크박스 위젯 출력
st.write("### 체크박스 위젯 출력")
x = st.checkbox("위 내용에 동의합니다!")

st.write(f"`{x}`")

# 3. 라디오 위젯 출력
st.write("### 라디오 위젯 출력")
x = st.radio("성별을 선택해주세요!", ["남자", "여자"])

st.write(f"`{x}`")

# 4. 선택박스 위젯 출력
st.write("### 선택박스 위젯 출력")
x = st.selectbox("성별을 선택해주세요!", ["남자", "여자"])

st.write(f"`{x}`")

# 5. 다중선택 위젯 출력
st.write("### 다중선택 위젯 출력")
x = st.multiselect("취미를 선택해주세요!", ["축구", "농구", "배구", "탁구"])
st.write(x)

# 6. 컬럼 선택 위젯 출력
st.write("### 컬럼 선택 위젯 출력")
c = st.color_picker("색상을 선택해주세요!", "#000000")
st.write(f"`{c}`")

# 7. 슬라이더 위젯 출력
st.write("### 슬라이더 위젯 출력")
x = st.slider("나이를 선택해주세요!", 0, 100, 25)
st.write(x)

# 8. 숫자 입력 위젯 출력
z = st.number_input("숫자를 입력해주세요!", min_value=0, max_value=100, value=25)
st.write(f"`시험 점수 = {z}`")

# 9. 텍스트 입력 위젯 출력
n = st.text_input("당신의 이름은?")
d = st.date_input("오늘 날짜는?")
t = st.time_input("현재 시간은?")

st.write(f"이름 = `{n}`, 날짜 = `{d}`, 시간 = `{t}`")

# 10. 카메라 위젯 출력
img_file_buffer = st.camera_input("카메라를 켜주세요!")

if img_file_buffer:
    img = Image.open(img_file_buffer)
    img_array = np.array(img)
    st.image(img_array)

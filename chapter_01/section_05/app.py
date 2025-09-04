import streamlit as st
import time

# 상태 표시 위젯 출력

# 1. 프로그레스 바 출력
st.write("### 프로그레스 바 출력")
st.progress(value=50)

# 2. 풍선, 눈송이등과 같은 특수 효과
st.balloons()
# st.snow()

# 3. 다양한 상태표시 출력
st.write("### 다양한 상태표시 출력")
st.info("정보 메시지", icon="ℹ️")
st.success("성공 메시지", icon="✅")
st.warning("경고 메시지", icon="⚠️")
st.error("오류 메시지", icon="🚨")
st.exception(ValueError("오류 발생"))

# 4. 스피너 출력
st.write("### 스피너 출력")
with st.spinner("잠시 기다려주세요..."):
    time.sleep(5)
    st.success("완료되었습니다!", icon="✅")

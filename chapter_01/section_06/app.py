import streamlit as st
import time

# 레이아웃

# 1. 사이드바 위젯 출력
with st.sidebar:
    st.title("사이드바 출력")
    st.header("사이드바 헤더")
    st.subheader("사이드바 서브헤더")
    x = st.slider("사이드바 슬라이더", 0, 100, 50)
    st.write(f"사이드바 슬라이더 값: {x}")

# 2. 컬럼 위젯 출력
st.write("### 컬럼 출력")
col1, col2, col3 = st.columns(3)
# col1, col2, col3 = st.columns([2, 6, 2])  # 비율 조정
with col1:
    st.write("Column 1")
    st.image("https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg")
with col2:
    st.write("Column 2")
    st.image("https://images.pexels.com/photos/531881/pexels-photo-531881.jpeg")
with col3:
    st.write("Column 3")
    st.image("https://images.pexels.com/photos/531882/pexels-photo-531882.jpeg")

# 3. 탭 위젯 출력
st.write("### 탭 출력")
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.image("https://images.pexels.com/photos/531880/pexels-photo-531880.jpeg")
with tab2:
    st.image("https://images.pexels.com/photos/531881/pexels-photo-531881.jpeg")
with tab3:
    st.image("https://images.pexels.com/photos/531882/pexels-photo-531882.jpeg")

# 4. 확장 위젯 출력
with st.expander("스크린 레이아웃 출력"):
    st.write("사진 출력")
    st.image("https://images.pexels.com/photos/531881/pexels-photo-531881.jpeg")

# 5. 동적 위젯 출력: 동적으로 내용을 업데이트할 수 있는 컨테이너를 만듭니다
c1, c2, c3, _ = st.columns([1, 1, 1, 5])
with c1:
    start = st.button("Start", key=1)
with c2:
    clear = st.button("Clear", key=2)
with c3:
    # 버튼 클릭 시 자동으로 페이지가 새로고침됩니다
    st.button("Reset", key=3)

y = st.empty()

if start:
    with y:
        for i in range(6):
            st.write(f"카운트 다운 {5-i}초")
            time.sleep(1)

if clear:
    y.empty()


# with 문법의 내부 동작 원리
class Sidebar:
    def __init__(self):
        self.current_container = None

    def __enter__(self):
        # 사이드바 모드로 전환
        self.current_container = "sidebar"
        # 모든 위젯이 사이드바에 렌더링되도록 설정
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 메인 영역 모드로 복원
        self.current_container = "main"


# 사용법
with st.sidebar:  # __enter__ 호출: 사이드바 모드로 전환
    st.write("사이드바")  # sidebar 컨테이너에 렌더링
# __exit__ 호출: 메인 영역 모드로 복원

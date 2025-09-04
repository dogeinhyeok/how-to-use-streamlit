import streamlit as st
import pandas as pd

# 텍스트 출력

# 1. 헤더 출력
st.title("Hello, World!")

# 2. 서브헤더 출력
st.subheader("This is a subheader")

# 3. 일반 텍스트 출력
st.text("짧은 길이의 일반 텍스트. *Markdown*")

# 4. 마크다운 출력
st.markdown("""
- 순서 없는 목록 `1`
- 순서 없는 목록 `2`
  - _들여쓰기된 목록_
  - ~또 다른 들여쓰기~

1. 순서 있는 목록 `1`
2. 순서 있는 목록 `2`
3. 순서 있는 목록 `3`
""")

# 5. 텍스트 또는 다양한 Python 변수/객체 출력
st.write("### 다양한 Python 변수/객체 출력")

x = 1
y = 2
df = pd.DataFrame({
    "Column_1": [x, y],
    "Column_2": [y * 2, x * 2],
    "Column_3": [True, False]
})
st.write("x = ", x, ", ", "y = ", y)
st.write(df)

# 6. LaTex 수식 컴파일해서 출력
st.latex(r"Area = \pi r^2")

# 7. 텍스트 중간에 수식 삽입
st.markdown(r"원의 넓이는 $Area = \pi r^2$ 입니다.")

# 8. 코드 출력
myCode = """
def hello():
    print("Hello, World!")
"""
st.code(myCode, language="python")

# 9. 캡션 출력
st.caption("This is a caption")

# 10. 매직 커맨드: st.write()를 대체합니다
x
y
"데이터 프레임", df
"이것은 :blue[파란색]입니다."
"이것은 :red[빨간색]입니다."
"이것은 :green[초록색]입니다."
":100: 점 만점에 :100: 점~ :smile:"

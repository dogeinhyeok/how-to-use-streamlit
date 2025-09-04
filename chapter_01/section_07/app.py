import streamlit as st
import pandas as pd
from io import StringIO

# 파일 올리고 다운로드

# 1. csv 파일 올리기
st.write("### csv 파일 올리기")
uploaded_file = st.file_uploader("파일 올리기", type=["csv", "xlsx", "txt"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)


# 2. py 파일 올리기
st.write("### py 파일 올리기")
uploaded_file = st.file_uploader("파일 올리기", type=["py"])
if uploaded_file:
    code = StringIO(uploaded_file.read().decode("utf-8")).read()
    st.code(code, language="python")

# 3. 여러 파일 올리기
st.write("### 여러 파일 올리기")
uploaded_files = st.file_uploader(
    "파일 올리기",
    type=["csv", "xlsx", "txt"],
    accept_multiple_files=True
)
if uploaded_files:
    names = []
    sizes = []
    for uploaded_file in uploaded_files:
        names.append(uploaded_file.name)
        sizes.append(uploaded_file.size)
    st.write(f"파일 이름: {names}")
    st.write(f"파일 크기: {sizes}")

# 4. 파일 다운로드
st.write("### 파일 다운로드")
df = pd.DataFrame({
    "Column_1": [1, 2, 3, 4, 5],
    "Column_2": [6, 7, 8, 9, 10],
    "Column_3": [11, 12, 13, 14, 15]
})
st.dataframe(df)
st.download_button("파일 다운로드", data=df.to_csv(), file_name="files.csv")

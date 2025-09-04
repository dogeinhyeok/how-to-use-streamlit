import streamlit as st
import pandas as pd

# 데이터 출력

# 1. 데이터 프레임 출력
st.write("### 데이터 프레임 출력")
x = 1
y = 2
df = pd.DataFrame({
    "Column_1": [x, y],
    "Column_2": [y * 2, x * 2],
    "Column_3": [True, False]
})

df
st.write(df)
st.dataframe(df)
st.table(df)

# 2. JSON 형식 출력
st.write("### JSON 형식 출력")
{"name": "홍길동", "age": 25, "gender": "남자"}

# 3. Metric() 함수를 사용한 출력
st.write("### Metric() 함수를 사용한 출력")
st.metric(label="온도", value="10 °C", delta="1.2 °C")
st.metric(label="삼성전자", value="61,900", delta="-300")

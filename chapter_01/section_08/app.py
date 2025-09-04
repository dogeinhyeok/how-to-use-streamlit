import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# NumPy: 데이터 분석의 기반이 되는 수치 계산 라이브러리
# Pandas: 데이터를 테이블 형태로 다루고 분석하는 라이브러리
# Matplotlib: 기본적인 차트를 그리는 시각화 라이브러리
# Seaborn: 고급 차트를 쉽게 그리는 시각화 라이브러리

# 웹앱 시각화 출력하기
st.write("### 웹앱 시각화 출력하기")

# 랜덤 데이터 생성
random_data = np.random.randn(30, 3)  # numpy 기능
ramdom_df = pd.DataFrame(random_data, columns=["a", "b", "c"])
"랜덤 데이터 미리보기", ramdom_df.head()

# 붓꽃 데이터 생성
iris_df = pd.read_csv("data_iris.csv")
"랜덤 데이터 미리보기", iris_df.head()

# 1. 기본 차트 출력
st.write("### 기본 차트 출력")
st.line_chart(ramdom_df)
st.area_chart(ramdom_df)
st.bar_chart(ramdom_df)

# 2. Matplotlib 차트 출력
st.write("### Matplotlib 차트 출력")
counts = iris_df["Species"].value_counts()
fig1 = plt.figure(figsize=(7, 5))
plt.bar(x=counts.index, height=counts.values, color="orange")
plt.ylabel("Counts")
plt.title("Iris Flower Species Counts - 1")
st.pyplot(fig1)

# 2.1. Matplotlib 차트 출력 - 객체 지향
st.write("### Matplotlib 차트 출력 - 객체 지향")
fig2 = plt.figure(figsize=(7, 5))
ax2 = fig2.add_axes([0, 0, 1, 1])
ax2.bar(x=counts.index, height=counts.values, color="green")
ax2.set_ylabel("Counts")
ax2.set_title("Iris Flower Species Counts - 2")
st.pyplot(fig2)

# 3. Seaborn 차트 출력
st.write("### Seaborn 차트 출력")
fig3 = plt.figure(figsize=(7, 5))
sns.countplot(data=iris_df, x="Species", hue="Species")
st.pyplot(fig3)

# 3.1. Seaborn 차트 출력 - 객체 지향
st.write("### Seaborn 차트 출력 - 객체 지향")
fig4, ax4 = plt.subplots()
sns.countplot(data=iris_df, x="Species", hue="Species", ax=ax4)
plt.legend(loc="lower right")
st.pyplot(fig4)

# 4. Map 시각화 출력
st.write("### Map 시각화 출력")
location = {"lat": [37.5665], "lon": [126.9780]}
for _ in range(100):
    location["lat"].append(location["lat"][0] + np.random.randn() * 0.02)
    location["lon"].append(location["lon"][0] + np.random.randn() * 0.02)
st.map(location, zoom=10)
st.button("Reset")

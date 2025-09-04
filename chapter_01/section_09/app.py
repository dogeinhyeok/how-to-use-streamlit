import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# 시각화 대상의 데이터
st.write("### 시각화 대상의 데이터")
iris_df = sns.load_dataset("iris")
colors = {"setosa": "red", "versicolor": "blue", "virginica": "green"}
st.write(iris_df.head())

# Siderbar 입력 위젯
with st.sidebar:
    # 숫자형 컬럼만 선택 (species 제외)
    numeric_columns = iris_df.select_dtypes(include=['number']).columns
    selectX = st.selectbox("X 축 선택", numeric_columns)
    ''
    selectY = st.selectbox("Y 축 선택", numeric_columns)
    ''
    selectSpecies = st.multiselect(
        "붓꽃 유형 선택 (:blue[다중])",
        ["setosa", "versicolor", "virginica"])
    ''
    selectAlpha = st.slider("alpha 설정", 0.1, 1.0, 0.5)

# 선택된 붓꽃 유형별 산점도로 시각화 표현
if selectSpecies:
    fig = plt.figure(figsize=(7, 5))
    for aSpecies in selectSpecies:
        df = iris_df[iris_df.species == aSpecies]
        plt.scatter(
            df[selectX], df[selectY], color=colors[aSpecies],
            alpha=selectAlpha, label=aSpecies)
    plt.xlabel(selectX)
    plt.ylabel(selectY)
    plt.title("Iris Scatter Plot")
    st.pyplot(fig)
else:
    st.warning("붓꽃 유형을 선택해주세요!")

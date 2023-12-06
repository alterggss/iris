import streamlit as st
import joblib

st.title("iris 品種")
knn=joblib.load("knn_model.joblib")
svm=joblib.load("rf_model.joblib")
rf=joblib.load("svm_model.joblib")

clf=st.sidebar.selectbox("### 請選擇分類器:",("knn","svm","randomForest"))
if clf=="knn":
    model=knn
elif clf=="svm":
    model=svm
else:
    model=rf

# 產生預測用的資料
s1 = st.slider("花萼的長度：", 3.0, 8.0, 5.8)
s2 = st.slider("花萼的寛度：", 2.0, 5.0, 3.8)
s3 = st.slider("花瓣的長度：", 1.0, 7.0, 4.8) 
s4 = st.slider("花瓣的寛度：", 0.1, 2.6, 1.8)

ans=st.button("進行預測")
name=['setosa','versicolor','virginica']
if ans:
    y=model.predict([[s1,s2,s3,s4]])
    st.write("### 預測結果"+name[y[0]])

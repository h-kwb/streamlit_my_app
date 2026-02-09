import streamlit as st

st.title("入力の取得")

# テキスト入力
name = st.text_input("お名前を教えてください")
# 数値入力（スライダー）
age = st.slider("年齢を選択", 0, 100, 25)

if name:
    st.write(f"{name}さん（{age}歳）、ようこそ！")
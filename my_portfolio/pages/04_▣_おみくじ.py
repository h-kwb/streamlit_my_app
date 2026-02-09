import streamlit as st

st.title("ボタンの利用")

if st.button("おみくじを引く"):
    # ボタンが押されたときだけ実行
    st.balloons() # お祝いのアニメーション
    st.success("大吉です！")
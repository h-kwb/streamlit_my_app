import streamlit as st

# title view
st.title("Streamlitアプリ")

# text
name = st.text_imput("名前を入力してください")

# button in
if st.button("挨拶する"):
    st.success(f"こんにちは、{name}さん！これはPythonで動いています")
    
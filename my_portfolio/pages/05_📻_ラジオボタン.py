import streamlit as st

st.title("選択UI")

# セレクトボックス
option = st.selectbox(
    "好きなフルーツは？",
    ["りんご", "バナナ", "メロン"]
)

# ラジオボタン
size = st.radio("サイズを選択", ["S", "M", "L"])

st.write(f"選んだのは: {option} の {size} サイズです。")
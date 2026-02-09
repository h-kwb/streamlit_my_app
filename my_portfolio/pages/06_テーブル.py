import streamlit as st
import pandas as pd

st.title("データの表示")

df = pd.DataFrame({
    '名前': ['田中', '佐藤', '鈴木'],
    '得点': [85, 92, 78]
})

# インタラクティブなテーブル
st.dataframe(df)
# 静的なテーブル
st.table(df)
import streamlit as st
import pandas as pd

st.title("ファイルアップロード")

uploaded_file = st.file_uploader("CSVファイルを選択してください", type='csv')

if uploaded_file is not None:
    # アップロードされたファイルを読み込む
    df = pd.read_csv(uploaded_file)
    st.write("プレビュー:")
    st.dataframe(df.head())
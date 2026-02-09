import streamlit as st
import numpy as np
import pandas as pd

st.title("グラフの描画")

# ランダムなデータを生成
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# 折れ線グラフを表示
st.line_chart(chart_data)
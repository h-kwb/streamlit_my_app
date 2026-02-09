import streamlit as st

st.title("カウンター（状態保持）")

# セッション状態を初期化
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('カウントアップ')
if increment:
    st.session_state.count += 1

st.write(f"現在のカウント: {st.session_state.count}")
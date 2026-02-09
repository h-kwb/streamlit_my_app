import streamlit as st

st.set_page_config(page_title="総合ポートフォリオ")
st.title("エンジニア就職用ポートフォリオ")
st.write("このアプリでは、Pythonで作成した様々なツールを公開しています。")
st.info("左側のメニューから各アプリを体験してください。")

# サイドバーにタイトル
st.sidebar.title("設定メニュー")

# サイドバーに入力項目を追加
user_id = st.sidebar.text_input("ID入力")
mode = st.sidebar.selectbox("モード", ["閲覧", "編集"])

st.write(f"メイン画面：現在のモードは {mode} です。")
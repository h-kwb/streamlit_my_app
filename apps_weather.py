import streamlit as st

# サイドバーにメニューを作成
st.sidebar.title("ナビゲーション")
menu = ["ホーム", "BMI計算機", "お天気チェック"]
choice = st.sidebar.radio("機能を選択してください", menu)

if choice == "ホーム":
    st.title("メインページ")
    st.write("左のメニューからツールを選んでください。")

elif choice == "BMI計算機":
    st.title("BMI計算ツール")
    weight = st.number_input("体重(kg)", value=60.0)
    height = st.number_input("身長(cm)", value=170.0)
    if st.button("計算"):
        bmi = weight / ((height/100)**2)
        st.info(f"あなたのBMIは {bmi:.2f} です")

elif choice == "お天気チェック":
    st.title("お天気API連携（デモ）")
    st.write("ここは将来的にAPI連携などを記述するページです。")
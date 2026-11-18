import streamlit as st
import pandas as pd

st.title("Catatan Keuangan Harian")

if "data" not in st.session_state:
    st.session_state.data = []

with st.form("form_transaksi"):
    kategori = st.selectbox("Kategori", ["Makan", "Transport", "Tagihan", "Lainnya"])
    nominal = st.number_input("Nominal (Rp)", min_value=0, step=5000)
    simpan = st.form_submit_button("Tambah")

    if simpan and nominal > 0:
        st.session_state.data.append({"Kategori": kategori, "Nominal": nominal})

if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.groupby("Kategori")["Nominal"].sum())
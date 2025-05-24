import streamlit as st

st.title("Aplikasi Produksi Sederhana")

# Input
jam_kerja = st.number_input("Jam Kerja per Hari", min_value=1, max_value=24, value=8)
produksi_per_jam = st.number_input("Jumlah Unit per Jam", min_value=1, value=10)

# Perhitungan
total_unit = jam_kerja * produksi_per_jam

# Output
st.success(f"Total Produksi per Hari: {total_unit} unit")

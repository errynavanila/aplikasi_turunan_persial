import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Aplikasi Produksi Harian dengan Grafik")

# Input
jam_kerja = st.number_input("Jam Kerja per Hari", min_value=1, max_value=24, value=8)
produksi_per_jam = st.number_input("Jumlah Unit per Jam", min_value=1, value=10)

# Hitung total produksi per hari
total_unit_per_hari = jam_kerja * produksi_per_jam

# Buat data produksi untuk 7 hari (misalnya 7 hari berturut-turut)
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
produksi = [total_unit_per_hari for _ in range(7)]

# Buat DataFrame
df = pd.DataFrame({'Hari': hari, 'Produksi': produksi})

# Tampilkan tabel
st.subheader("Data Produksi Mingguan")
st.dataframe(df)

# Tampilkan grafik
st.subheader("Grafik Produksi per Hari")
fig, ax = plt.subplots()
ax.bar(df['Hari'], df['Produksi'], color='skyblue')
ax.set_ylabel('Jumlah Produksi (unit)')
ax.set_title('Produksi Harian Selama Seminggu')
st.pyplot(fig)


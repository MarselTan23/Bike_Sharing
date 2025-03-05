import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')
st.header('Bike Sharing')

# Read data
day_df = pd.read_csv("all_data.csv")
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
day_df["month"] = day_df["dteday"].dt.month
day_df["year"] = day_df["dteday"].dt.year

# Menambahkan kolom nama bulan
month_names = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni",
               7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
day_df["month_name"] = day_df["month"].map(month_names)

# Menentukan rentang tanggal minimum dan maksimum
min_date_days = day_df["dteday"].min()
max_date_days = day_df["dteday"].max()

# Sidebar untuk memilih rentang waktu
with st.sidebar:
    st.image("https://thumbs.dreamstime.com/z/bike-sharing-system-station-city-street-bike-sharing-system-station-city-street-boy-holding-smartphone-open-mobile-app-135151978.jpg")
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days]
    )

# Mengonversi tanggal dari date ke datetime untuk perbandingan
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Menyaring data berdasarkan rentang waktu yang dipilih
main_df_days = day_df[(day_df["dteday"] >= start_date) & (day_df["dteday"] <= end_date)]


# Pertanyaan 1: Bagaimana performa penyewaan sepeda dalam beberapa Bulan terakhir?

st.subheader("1. Bagaimana performa penyewaan sepeda dalam beberapa Bulan terakhir?")
st.write(" Berikut adalah hasil dari Peforma 12 Bulan ke beleakang ")
# Set ukuran figure menjadi lebar (25, 5) untuk tampilan yang lebih luas
fig, ax = plt.subplots(figsize=(25, 5))

# Hitung nilai jumlah penyewa sepeda per bulan dari kolom 'cnt' di DataFrame 'day_df'
month_counts_day = day_df['cnt'].groupby(day_df['mnth']).sum()

# Buat scatter plot untuk jumlah penyewa sepeda per bulan dari 'day_df'
ax.scatter(month_counts_day.index, month_counts_day.values, c="#90CAF9", s=50, marker='o', label='Jumlah Penyewaan per Bulan (Day)')

# Buat line plot untuk menghubungkan titik-titik pada jumlah penyewa sepeda per bulan dari 'day_df'
ax.plot(month_counts_day.index, month_counts_day.values, color='blue', linewidth=2)

# Menambahkan label untuk sumbu X
ax.set_xlabel('Bulan')

# Menambahkan label untuk sumbu Y
ax.set_ylabel('Jumlah Yang Menyewa')

# Menambahkan judul grafik
ax.set_title('Grafik Jumlah Penyewa Sepeda per Bulan (Day)')

# Menampilkan legenda untuk scatter plot
ax.legend()

# Menambahkan grid dengan gaya garis putus-putus untuk memperjelas tampilan plot
ax.grid(True, linestyle='--', alpha=0.5)

# Menampilkan grafik
st.pyplot(fig)

# 2.  Untuk 1 musim, minimal ada berapa penyewa yang menyewakan sepeda?
st.subheader("2.  Untuk 1 musim, minimal ada berapa penyewa yang menyewakan sepeda?")
st.write(" Berikut hasil dari minimal penyewaan dalam 1 musim ")
# Membuat figure untuk semua plot
fig = plt.figure(figsize=(25, 5))

# Plot pertama untuk day_df
plt.subplot(1, 2, 1)  # 1 baris, 2 kolom, posisi pertama
plt.bar(day_df['season'].unique(), day_df.groupby('season')['cnt'].min(), color='skyblue')
plt.xlabel('Season')
plt.ylabel('Jumlah Penyewa Sepeda')
plt.title('Jumlah Minimal Penyewa Sepeda berdasarkan Season')
plt.grid(True, linestyle='--', alpha=0.5)

# Menyusun layout agar lebih rapi
plt.tight_layout()

# Menampilkan grafik di Streamlit
st.pyplot(fig)

# 3. Musim dengan Penyewaan Sepeda Tersedikit
st.subheader("3.  Penyewa apa yang paling banyak antara Registered dan Casual di tahun 2011 dan 2012?")
st.write(" Berikut hasil dari yang paling banyak antara Registered dan Casual")
# Menghitung jumlah penyewaan untuk registered dan casual per tahun
registered_counts = day_df.groupby("yr")["registered"].sum()
casual_counts = day_df.groupby("yr")["casual"].sum()

# Membuat data tahun sebagai kategori
years = ["2011", "2012"]

# Mengatur ukuran figure
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat bar plot untuk registered dan casual
bar_width = 0.35
index = range(len(years))

# Plot untuk penyewa registered
ax.bar([i - bar_width/2 for i in index], registered_counts, width=bar_width, color="skyblue", label="Registered")

# Plot untuk penyewa casual
ax.bar([i + bar_width/2 for i in index], casual_counts, width=bar_width, color="orange", label="Casual")

# Mengatur judul dan label
ax.set_title("Perbandingan Penyewa Registered dan Casual di 2011 dan 2012", fontsize=16)
ax.set_xlabel("Tahun", fontsize=14)
ax.set_ylabel("Jumlah Penyewaan", fontsize=14)
ax.set_xticks(index)
ax.set_xticklabels(years, fontsize=12)

# Mengatur format tampilan sumbu y agar menampilkan angka asli
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Menampilkan legenda
ax.legend()

# Menampilkan grafik di Streamlit
st.pyplot(fig)

# 4. Pada Hari apa yang lebih banyak menyewa sepeda?

st.subheader("4. Pada Hari apa yang lebih banyak menyewa sepeda?")
st.write("Berikut hasil dari hari yang paling banyak menyewa sepeda")
# Menghitung total penyewaan untuk setiap kategori hari (Holiday dan Not on holiday)
total_rentals_by_holiday = day_df.groupby('holiday')['cnt'].sum()

# Membuat pie chart
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(
    total_rentals_by_holiday, 
    labels=["Not on Holiday", "Holiday"],  # Ubah label agar lebih deskriptif
    autopct='%1.1f%%', 
    colors=['skyblue', 'orange']
)

# Mengatur judul
ax.set_title("Persentase Penyewaan Sepeda pada Hari Libur dan Hari Biasa", fontsize=16)

# Menampilkan pie chart di Streamlit
st.pyplot(fig)
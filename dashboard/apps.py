import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
import datetime
import time
import pytz

st.title('🤖 Dashboard Visualisasi Data App')
st.info('Dashboard Streamlit - Andrian Syah')

github_repo = "https://github.com/andriansyah2501/appslaskarai"
linkedln = "https://www.linkedin.com/in/andriansyah2501/"
creation_date = "2025-03-18"
st.sidebar.header("Informasi Aplikasi")
st.sidebar.markdown(f"**Repository GitHub:** [Klik di sini]({github_repo})")
st.sidebar.markdown(f"**Linkedln:** [Let's Connect Now]({linkedln})")
st.sidebar.markdown(f"**Tanggal Pembuatan:** {creation_date}")


profile_image_url = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/data/profile.jpg"
st.sidebar.image(profile_image_url, caption="Andrian Syah", width=250)

# Load data
github_url_day = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/day.csv"
github_url_hour = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/hour.csv"
day_df = pd.read_csv(github_url_day)
hour_df = pd.read_csv(github_url_hour)

# Data Wrangling
# Mengonversi tanggal menjadi format datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Mengubah nama kolom untuk lebih mudah dipahami
day_df.rename(columns={'cnt': 'total_peminjaman', 'temp': 'suhu'}, inplace=True)
hour_df.rename(columns={'cnt': 'total_peminjaman', 'temp': 'suhu'}, inplace=True)

# Menambahkan kolom baru untuk analisis
day_df['year'] = day_df['dteday'].dt.year
day_df['month'] = day_df['dteday'].dt.month
day_df['day'] = day_df['dteday'].dt.day

# Teknik Binning untuk mengelompokkan peminjaman
bins = [0, 500, 1500, 3000, 5000, day_df['total_peminjaman'].max()]
labels = ['Sangat Rendah', 'Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi']
day_df['Kategori Peminjaman'] = pd.cut(day_df['total_peminjaman'], bins=bins, labels=labels, include_lowest=True)



st.title('Data - Dicoding Laskar AI')
tab1, tab2 = st.tabs(["Data Hari", "Data Jam"])
 
with tab1:
    st.header("Data Harian")
    st.dataframe(day_df)
 
with tab2:
    st.header("Data Per Jam")
    st.dataframe(hour_df)


# Data processing
season_avg = day_df.groupby("season")["cnt"].mean()
hour_avg = hour_df.groupby("hr")["cnt"].mean()

# Pertanyaan 1: Penggunaan sepeda berdasarkan musim
st.header("1. Bagaimana pola penggunaan sepeda berubah berdasarkan musim?")
fig, ax = plt.subplots()
season_avg.plot(kind='bar', ax=ax, color=['blue', 'green', 'orange', 'red'])
ax.set_xticklabels(['Semi', 'Panas', 'Gugur', 'Dingin'], rotation=0)
ax.set_ylabel("Rata-rata peminjaman")
st.pyplot(fig)

# Pertanyaan 2: Jam dengan peminjaman tertinggi
st.header("2. Pada jam berapa jumlah peminjaman sepeda paling tinggi dalam sehari?")
fig, ax = plt.subplots()
hour_avg.plot(kind='line', ax=ax, marker='o', color='purple')
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata peminjaman")
st.pyplot(fig)

# Korelasi suhu dengan peminjaman
correlation_temp_cnt = day_df["suhu"].corr(day_df["total_peminjaman"])
st.write(f"Korelasi antara suhu dan jumlah peminjaman sepeda: {correlation_temp_cnt:.2f}")

# Hari dengan peminjaman tertinggi dan terendah
max_rent_day = day_df.loc[day_df["total_peminjaman"].idxmax(), ["dteday", "total_peminjaman"]]
min_rent_day = day_df.loc[day_df["total_peminjaman"].idxmin(), ["dteday", "total_peminjaman"]]

st.write(f"Hari dengan peminjaman terbanyak: {max_rent_day['dteday']} dengan {max_rent_day['total_peminjaman']} peminjaman.")
st.write(f"Hari dengan peminjaman tersedikit: {min_rent_day['dteday']} dengan {min_rent_day['total_peminjaman']} peminjaman.")

# Analisis Binning
st.header("3. Distribusi Kategori Peminjaman Sepeda")
category_counts = day_df['Kategori Peminjaman'].value_counts()
fig, ax = plt.subplots()
category_counts.plot(kind='bar', ax=ax, color=['blue', 'green', 'orange', 'red', 'purple'])
ax.set_ylabel("Jumlah Hari")
ax.set_xlabel("Kategori Peminjaman")
ax.set_title("Distribusi Kategori Peminjaman Sepeda")
st.pyplot(fig)

# Analisis Proporsi Peminjaman antara Hari Kerja dan Akhir Pekan
st.header("4. Bagaimana proporsi peminjaman sepeda pada hari kerja vs akhir pekan?")
weekend_count = day_df[day_df['weekday'].isin([0, 6])]['total_peminjaman'].sum()
weekday_count = day_df[~day_df['weekday'].isin([0, 6])]['total_peminjaman'].sum()

labels = ["Hari Kerja", "Akhir Pekan"]
values = [weekday_count, weekend_count]

fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%', colors=["blue", "orange"])
ax.set_title("Distribusi Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
st.pyplot(fig)

 

st.caption('Copyright (c) 2025')

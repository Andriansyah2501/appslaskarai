import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# URL dataset di GitHub
day_url = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/day.csv"
hour_url = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/hour.csv"

github_repo = "https://github.com/andriansyah2501/appslaskarai"
linkedln = "https://www.linkedin.com/in/andriansyah2501/"
creation_date = "2025-03-18"
st.sidebar.header("Informasi Aplikasi")
st.sidebar.markdown(f"**Repository GitHub:** [Klik di sini]({github_repo})")
st.sidebar.markdown(f"**Linkedln:** [Let's Connect Now]({linkedln})")
st.sidebar.markdown(f"**Tanggal Pembuatan:** {creation_date}")

profile_image_url = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/data/profile.jpg"
st.sidebar.image(profile_image_url, caption="Andrian Syah", width=250)


# Muat data dari GitHub
day_df = pd.read_csv(day_url)
hour_df = pd.read_csv(hour_url)

# Konversi kolom tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Judul
st.title("Dashboard Penyewaan Sepeda")

# Metrik
# st.metric("Total Penyewaan (Harian)", day_df['cnt'].sum())
# st.metric("Rata-rata Penyewaan per Hari", round(day_df['cnt'].mean(), 2))
# st.metric("Total Penyewaan (Per Jam)", hour_df['cnt'].sum())
# st.metric("Rata-rata Penyewaan per Jam", round(hour_df['cnt'].mean(), 2))

st.header("Data Laskar AI")
# Tab untuk menampilkan dataset
data_tab1, data_tab2 = st.tabs(["Dataset Penyewaan Harian", "Dataset Penyewaan Per Jam"])

with data_tab1:
    st.subheader("Dataset Penyewaan Harian")
    st.dataframe(day_df)

with data_tab2:
    st.subheader("Dataset Penyewaan Per Jam")
    st.dataframe(hour_df)


# Pertanyaan 1: Bagaimana pengaruh musim terhadap jumlah peminjaman sepeda?
season_mapping = {1: "Musim Dingin", 2: "Musim Semi", 3: "Musim Panas", 4: "Musim Gugur"}
day_df["season_label"] = day_df["season"].map(season_mapping)
season_trend = day_df.groupby("season_label")["cnt"].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x=season_trend["season_label"], y=season_trend["cnt"], palette="coolwarm")
plt.title("Pengaruh Musim terhadap Peminjaman Sepeda")
plt.xlabel("Musim")
plt.ylabel("Rata-rata Peminjaman")
plt.grid(axis="y")
plt.tight_layout()
plt.show()


# Pertanyaan 2:  Pada jam berapa peminjaman sepeda tertinggi?
plt.figure(figsize=(10, 5))
sns.barplot(x=hour_df["hr"], y=hour_df["cnt"], estimator=sum, palette="viridis")
plt.title("Distribusi Peminjaman Sepeda per Jam (Hour Dataset)")
plt.xlabel("Jam")
plt.ylabel("Total Peminjaman")
plt.xticks(range(0, 24))
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Tab untuk Analisis Pertanyaan
st.subheader("Analisis Penyewaan Sepeda")
tab1, tab2 = st.tabs(["Pengaruh Cuaca", "Distribusi Penyewaan Berdasarkan Jam"])

with tab1:
    st.subheader("Bagaimana cuaca mempengaruhi penyewaan sepeda?")
    weather_avg = day_df.groupby('weathersit')['cnt'].mean()
    fig, ax = plt.subplots()
    ax.bar(weather_avg.index.astype(str), weather_avg.values, color=['green', 'orange', 'red', 'blue'])
    ax.set_xlabel("Jenis Cuaca")
    ax.set_ylabel("Rata-rata Penyewaan")
    ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    st.pyplot(fig)
    st.write("Cuaca cerah (1) memiliki tingkat penyewaan lebih tinggi dibandingkan cuaca mendung (2) dan hujan/salju (3 & 4).")

with tab2:
    st.subheader("Pada jam berapa penyewaan sepeda paling banyak terjadi?")
    hourly_total = hour_df.groupby('hr')['cnt'].sum()
    fig, ax = plt.subplots()
    ax.bar(hourly_total.index, hourly_total.values, color='blue')
    ax.set_xlabel("Jam")
    ax.set_ylabel("Total Penyewaan")
    ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Jam")
    st.pyplot(fig)
    st.write("Penyewaan sepeda paling banyak terjadi pada jam sibuk pagi (07:00 - 09:00) dan sore (17:00 - 19:00).")


st.subheader("Kesimpulan")
k_tab1, k_tab2 = st.tabs(["Ringkasan Kesimpulan", "Data Kesimpulan Lengkap"])

with k_tab1:
    st.subheader("Ringkasan Kesimpulan")
    kategori = ['Cuaca Cerah', 'Jam Sibuk Pagi', 'Jam Sibuk Sore']
    nilai = [weather_avg[1], hourly_total[8], hourly_total[18]]
    fig, ax = plt.subplots()
    ax.bar(kategori, nilai, color=['green', 'orange', 'red'])
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Kesimpulan dari Analisis Penyewaan Sepeda")
    st.pyplot(fig)
    st.write("Dari analisis ini, kita dapat menyimpulkan bahwa penyewaan sepeda meningkat pada cuaca cerah serta pada jam sibuk pagi dan sore hari.")

with k_tab2:
    st.subheader("Data Kesimpulan Lengkap")
    summary_df = pd.DataFrame({
        "Faktor": ["Cuaca Cerah", "Jam Sibuk Pagi (07:00 - 09:00)", "Jam Sibuk Sore (17:00 - 19:00)"],
        "Jumlah Penyewaan": [weather_avg[1], hourly_total[8], hourly_total[18]]
    })

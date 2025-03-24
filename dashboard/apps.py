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
st.subheader("📊 Bagaimana pengaruh musim terhadap jumlah peminjaman sepeda?")
season_mapping = {1: "Musim Dingin", 2: "Musim Semi", 3: "Musim Panas", 4: "Musim Gugur"}
day_df["season_label"] = day_df["season"].map(season_mapping)
season_trend = day_df.groupby("season_label")["cnt"].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=season_trend["season_label"], y=season_trend["cnt"], palette="coolwarm", ax=ax)
ax.set_title("Pengaruh Musim terhadap Peminjaman Sepeda")
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Peminjaman")
ax.grid(axis="y")

# Tampilkan di Streamlit
st.pyplot(fig)


# Pertanyaan 2:  Pada jam berapa peminjaman sepeda tertinggi?
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=hour_df["hr"], y=hour_df["cnt"], estimator=sum, palette="viridis", ax=ax)
ax.set_title("Distribusi Peminjaman Sepeda per Jam (Hour Dataset)")
ax.set_xlabel("Jam")
ax.set_ylabel("Total Peminjaman")
ax.set_xticks(range(0, 24))
ax.grid(axis="y")

# Tampilkan di Streamlit
st.pyplot(fig)


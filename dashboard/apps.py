import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load Dataset
day_url = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/day.csv"
hour_url = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/hour.csv"

day_df = pd.read_csv(day_url)
hour_df = pd.read_csv(hour_url)

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

season_mapping = {1: "Musim Dingin", 2: "Musim Semi", 3: "Musim Panas", 4: "Musim Gugur"}
day_df["season_label"] = day_df["season"].map(season_mapping)

# Sidebar untuk filter data
st.sidebar.header("🔍 Filter Data")
selected_season = st.sidebar.multiselect("Pilih Musim", day_df["season_label"].unique(), default=day_df["season_label"].unique())

date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [day_df['dteday'].min(), day_df['dteday'].max()])

filtered_df = day_df[(day_df["season_label"].isin(selected_season)) & (day_df["dteday"].between(date_range[0], date_range[1]))]

# Pilihan metrik
st.sidebar.header("📊 Pilih Metrik Statistik")
show_total = st.sidebar.checkbox("Total Penyewaan")
show_avg = st.sidebar.checkbox("Rata-rata Penyewaan")

st.title("🚴‍♂️ Dashboard Penyewaan Sepeda")

if show_total:
    st.metric("Total Penyewaan (Harian)", filtered_df['cnt'].sum())
if show_avg:
    st.metric("Rata-rata Penyewaan per Hari", round(filtered_df['cnt'].mean(), 2))

st.subheader("📊 Pengaruh Musim terhadap Peminjaman Sepeda")
season_trend = filtered_df.groupby("season_label")["cnt"].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=season_trend["season_label"], y=season_trend["cnt"], palette="coolwarm", ax=ax)
ax.set_title("Pengaruh Musim terhadap Peminjaman Sepeda")
st.pyplot(fig)

st.subheader("⏰ Distribusi Peminjaman Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=hour_df["hr"], y=hour_df["cnt"], estimator=sum, palette="viridis", ax=ax)
ax.set_title("Distribusi Peminjaman Sepeda per Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Total Peminjaman")
ax.set_xticks(range(0, 24))
ax.grid(axis="y")
st.pyplot(fig)

st.write("### 📊 Analisis Peminjaman Sepeda")
st.write("Peminjaman sepeda cenderung lebih tinggi pada musim panas dan semi. Pengguna lebih sering menyewa sepeda saat jam sibuk (pagi dan sore).")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URL dataset di GitHub
day_url = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/day.csv"
hour_url = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/hour.csv"

# Muat data dari GitHub
day_df = pd.read_csv(day_url)
hour_df = pd.read_csv(hour_url)

# Konversi kolom tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Judul
st.title("Dashboard Penyewaan Sepeda")

# Metrik
st.metric("Total Penyewaan (Harian)", day_df['cnt'].sum())
st.metric("Rata-rata Penyewaan per Hari", round(day_df['cnt'].mean(), 2))
st.metric("Total Penyewaan (Per Jam)", hour_df['cnt'].sum())
st.metric("Rata-rata Penyewaan per Jam", round(hour_df['cnt'].mean(), 2))

# Grafik garis: Penyewaan dari waktu ke waktu
st.subheader("Total Penyewaan dari Waktu ke Waktu")
fig, ax = plt.subplots()
ax.plot(day_df['dteday'], day_df['cnt'], label="Total Penyewaan Harian", color='blue')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Penyewaan")
ax.legend()
st.pyplot(fig)

# Grafik garis: Penyewaan per jam
st.subheader("Total Penyewaan Sepeda Per Jam")
hourly_avg = hour_df.groupby('hr')['cnt'].mean()
st.line_chart(hourly_avg)

# Pertanyaan 1: Bagaimana musim mempengaruhi penyewaan sepeda?
st.subheader("Penyewaan Sepeda Berdasarkan Musim")
season_avg = day_df.groupby('season')['cnt'].mean()
st.bar_chart(season_avg)
st.write("Musim dingin (4) dan musim panas (2) cenderung memiliki penyewaan sepeda lebih tinggi dibandingkan musim semi (1) dan musim gugur (3).")

# Pertanyaan 2: Bagaimana hari kerja mempengaruhi penyewaan?
st.subheader("Penyewaan Sepeda: Hari Kerja vs. Hari Libur")
working_avg = day_df.groupby('workingday')['cnt'].mean()
st.bar_chart(working_avg)
st.write("Penyewaan sepeda umumnya lebih tinggi pada hari kerja dibandingkan hari libur.")

# Analisis RFM
st.subheader("Analisis RFM (Recency, Frequency, Monetary)")
latest_date = day_df['dteday'].max()
rfm_df = day_df.groupby('weekday').agg(
    Recency=('dteday', lambda x: (latest_date - x.max()).days),
    Frequency=('cnt', 'count'),
    Monetary=('cnt', 'sum')
).reset_index()

st.write("Recency: Seberapa baru penyewaan terakhir dilakukan.")
st.write("Frequency: Seberapa sering penyewaan dilakukan.")
st.write("Monetary: Total penyewaan dalam periode tertentu.")

st.dataframe(rfm_df)

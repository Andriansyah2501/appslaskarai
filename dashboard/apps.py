import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.title('🤖 Dashboard Visualisasi Data App')
st.info('Hello Word')
st.info('Dashboard Streamlit Andrian Syah')
st.title("Analisis Data Bike Sharing")


 
# Load data
github_url_day = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/day.csv"
github_url_hour = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/hour.csv"
day_df = pd.read_csv(github_url_day)
hour_df = pd.read_csv(github_url_hour)

# Data processing
season_avg = day_df.groupby("season")["cnt"].mean()
hour_avg = hour_df.groupby("hr")["cnt"].mean()

# Streamlit UI


st.header("1. Bagaimana pola penggunaan sepeda berubah berdasarkan musim?")
fig, ax = plt.subplots()
season_avg.plot(kind='bar', ax=ax, color=['blue', 'green', 'orange', 'red'])
ax.set_xticklabels(['Semi', 'Panas', 'Gugur', 'Dingin'], rotation=0)
ax.set_ylabel("Rata-rata peminjaman")
st.pyplot(fig)


st.header("2. Pada jam berapa jumlah peminjaman sepeda paling tinggi dalam sehari?")
fig, ax = plt.subplots()
hour_avg.plot(kind='line', ax=ax, marker='o', color='purple')
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata peminjaman")
st.pyplot(fig)


correlation_temp_cnt = day_df["temp"].corr(day_df["cnt"])
st.write(f"Korelasi antara suhu dan jumlah peminjaman sepeda: {correlation_temp_cnt:.2f}")


max_rent_day = day_df.loc[day_df["cnt"].idxmax(), ["dteday", "cnt"]]
min_rent_day = day_df.loc[day_df["cnt"].idxmin(), ["dteday", "cnt"]]

st.write(f"Hari dengan peminjaman terbanyak: {max_rent_day['dteday']} dengan {max_rent_day['cnt']} peminjaman.")
st.write(f"Hari dengan peminjaman tersedikit: {min_rent_day['dteday']} dengan {min_rent_day['cnt']} peminjaman.")

 

st.caption('Copyright (c) 2025')

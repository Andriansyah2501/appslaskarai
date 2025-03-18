import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.title('🤖 Dashboard Visualisasi Data App')
st.info('Hello Word')
st.info('Dashboard Streamlit Andrian Syah')


import streamlit as st
 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Data processing
season_avg = day_df.groupby("season")["cnt"].mean()
hour_avg = hour_df.groupby("hr")["cnt"].mean()

# Streamlit UI
st.title("Analisis Data Bike Sharing")

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
correlation_temp_cnt = day_df["temp"].corr(day_df["cnt"])
st.write(f"Korelasi antara suhu dan jumlah peminjaman sepeda: {correlation_temp_cnt:.2f}")

# Hari dengan peminjaman tertinggi dan terendah
max_rent_day = day_df.loc[day_df["cnt"].idxmax(), ["dteday", "cnt"]]
min_rent_day = day_df.loc[day_df["cnt"].idxmin(), ["dteday", "cnt"]]

st.write(f"Hari dengan peminjaman terbanyak: {max_rent_day['dteday']} dengan {max_rent_day['cnt']} peminjaman.")
st.write(f"Hari dengan peminjaman tersedikit: {min_rent_day['dteday']} dengan {min_rent_day['cnt']} peminjaman.")

 

st.caption('Copyright (c) 2025')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.title('🤖 Dashboard Visualisasi Data App')
st.info('Hello Word')
st.info('Dashboard Streamlit Andrian Syah')

# Load data
github_url_day = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/day.csv"
github_url_hour = "https://raw.githubusercontent.com/andriansyah2501/appslaskarai/main/dashboard/hour.csv"
day_df = pd.read_csv(github_url_day)
hour_df = pd.read_csv(github_url_hour)

# Tampilkan data mentah

st.title('Data Mentah - Dicoding Laskar AI')
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

# Streamlit UI
st.header("pertanyaan analisis data")
st.write("1. Bagaimana pola penggunaan sepeda berubah berdasarkan musim?")
fig, ax = plt.subplots()
season_avg.plot(kind='bar', ax=ax, color=['blue', 'green', 'orange', 'red'])
ax.set_xticklabels(['Semi', 'Panas', 'Gugur', 'Dingin'], rotation=0)
ax.set_ylabel("Rata-rata peminjaman")
st.pyplot(fig)


st.write("2. Pada jam berapa jumlah peminjaman sepeda paling tinggi dalam sehari?")
fig, ax = plt.subplots()
hour_avg.plot(kind='line', ax=ax, marker='o', color='purple')
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata peminjaman")
st.pyplot(fig)



max_rent_day = day_df.loc[day_df["cnt"].idxmax(), ["dteday", "cnt"]]
min_rent_day = day_df.loc[day_df["cnt"].idxmin(), ["dteday", "cnt"]]

st.write(f"Hari dengan peminjaman terbanyak: {max_rent_day['dteday']} dengan {max_rent_day['cnt']} peminjaman.")
st.write(f"Hari dengan peminjaman tersedikit: {min_rent_day['dteday']} dengan {min_rent_day['cnt']} peminjaman.")


#no 3

# Analisis Proporsi Peminjaman antara Hari Kerja dan Akhir Pekan
st.wite("3. Bagaimana proporsi peminjaman sepeda pada hari kerja vs akhir pekan?")
weekend_count = day_df[day_df['weekday'].isin([0, 6])]['cnt'].sum()
weekday_count = day_df[~day_df['weekday'].isin([0, 6])]['cnt'].sum()

labels = ["Hari Kerja", "Akhir Pekan"]
values = [weekday_count, weekend_count]

fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%', colors=["blue", "orange"])
ax.set_title("Distribusi Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
st.pyplot(fig)
 

st.caption('Copyright (c) 2025')

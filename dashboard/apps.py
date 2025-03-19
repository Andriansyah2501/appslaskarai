import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
# Load dataset
st.write("🔄 Memuat dataset...")
day_df = pd.read_csv(day_url)
hour_df = pd.read_csv(hour_url)
st.success("✅ Dataset berhasil dimuat!")

# Cek missing values
st.write("🔍 Mengecek missing values...")
missing_day = day_df.isnull().sum().sum()
missing_hour = hour_df.isnull().sum().sum()

if missing_day > 0 or missing_hour > 0:
    day_df.fillna(method='ffill', inplace=True)
    hour_df.fillna(method='ffill', inplace=True)
    st.warning(f"⚠️ Missing values ditemukan dan telah diperbaiki ({missing_day} di day.csv, {missing_hour} di hour.csv)")
else:
    st.success("✅ Tidak ada missing values!")

# Cek duplikasi
st.write("🔍 Mengecek duplikasi...")
duplicates_day = day_df.duplicated().sum()
duplicates_hour = hour_df.duplicated().sum()

if duplicates_day > 0 or duplicates_hour > 0:
    day_df.drop_duplicates(inplace=True)
    hour_df.drop_duplicates(inplace=True)
    st.warning(f"⚠️ {duplicates_day} duplikasi dihapus dari day.csv dan {duplicates_hour} dari hour.csv")
else:
    st.success("✅ Tidak ada duplikasi!")

# Konversi format tanggal
st.write("🔄 Mengonversi format tanggal...")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
st.success("✅ Format tanggal sudah benar!")

# Cek outliers
st.write("📊 Mengecek outliers...")
Q1 = day_df['cnt'].quantile(0.25)
Q3 = day_df['cnt'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_count = ((day_df['cnt'] < lower_bound) | (day_df['cnt'] > upper_bound)).sum()
if outliers_count > 0:
    day_df = day_df[(day_df['cnt'] >= lower_bound) & (day_df['cnt'] <= upper_bound)]
    st.warning(f"⚠️ {outliers_count} outliers telah dihapus!")
else:
    st.success("✅ Tidak ada outliers yang ditemukan!")

st.balloons()
st.success("🎉 Data cleaning selesai! Data siap digunakan untuk analisis!")

# Tabs
data_tab1, data_tab2, data_tab3 = st.tabs(["Dataset Penyewaan Harian", "Dataset Penyewaan Per Jam", "Cleaning Notification"])

with data_tab1:
    st.subheader("Dataset Penyewaan Harian")
    st.dataframe(day_df)

with data_tab2:
    st.subheader("Dataset Penyewaan Per Jam")
    st.dataframe(hour_df)

with data_tab3:
    st.subheader("Cleaning Notification")
    st.write("🔍 Proses pembersihan data telah dilakukan.")
    st.write(f"✅ Missing values diperbaiki: {missing_day} di day.csv, {missing_hour} di hour.csv")
    st.write(f"✅ Duplikasi dihapus: {duplicates_day} di day.csv, {duplicates_hour} di hour.csv")
    st.write(f"✅ Outliers dihapus: {outliers_count}")
    st.success("🎉 Data siap digunakan untuk analisis!")



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
    st.dataframe(summary_df)

import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from streamlit_folium import st_folium
import folium

# Koordinat wilayah Jakarta
koordinat_wilayah = {
    "Jakarta Pusat": [-6.1862, 106.8340],
    "Jakarta Utara": [-6.1214, 106.8650],
    "Jakarta Barat": [-6.1745, 106.7890],
    "Jakarta Selatan": [-6.2700, 106.8200],
    "Jakarta Timur": [-6.2100, 106.9000]
}

wilayah = list(koordinat_wilayah.keys())

@st.cache_resource
def latih_model():
    df = pd.read_csv("dataset_pollution_jakarta.csv")
    X = df[["Suhu", "Kelembaban", "Tanggal_Ordinal"]]
    y = df["Polusi_Udara"]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def warna_marker(aqi):
    if aqi < 50:
        return "green"
    elif aqi < 100:
        return "orange"
    else:
        return "red"

def kategori_dan_rekomendasi(aqi):
    if aqi < 50:
        return "Baik", "Udara bersih dan aman untuk aktivitas luar ruangan."
    elif aqi < 100:
        return "Sedang", "Hati-hati jika memiliki gangguan pernapasan."
    elif aqi < 150:
        return "Tidak Sehat untuk Kelompok Sensitif", "Batasi aktivitas luar ruangan jika Anda sensitif terhadap polusi."
    elif aqi < 200:
        return "Tidak Sehat", "Disarankan untuk mengurangi aktivitas luar ruangan."
    else:
        return "Sangat Tidak Sehat", "Hindari aktivitas luar ruangan dan gunakan masker jika keluar rumah."

st.title("Prediksi Polusi Udara Wilayah Jakarta dengan Forecasting Beberapa Hari ke Depan")

min_date = datetime.today().date()
max_date = min_date + timedelta(days=7)
selected_date = st.date_input("Pilih tanggal untuk prediksi polusi udara:", value=min_date, min_value=min_date, max_value=max_date)

# Inisialisasi session_state untuk menyimpan hasil prediksi
if "hasil_prediksi" not in st.session_state:
    st.session_state.hasil_prediksi = None

if st.button("Prediksi Polusi Udara"):
    with st.spinner("Memproses prediksi..."):
        model = latih_model()
        tanggal_ordinal = selected_date.toordinal()
        data_prediksi = []
        for w in wilayah:
            suhu = random.uniform(25, 35)
            kelembaban = random.uniform(40, 90)
            fitur = pd.DataFrame([[suhu, kelembaban, tanggal_ordinal]], columns=["Suhu", "Kelembaban", "Tanggal_Ordinal"])
            prediksi = model.predict(fitur)[0]
            kategori, rekomendasi = kategori_dan_rekomendasi(prediksi)
            data_prediksi.append([w, suhu, kelembaban, selected_date, prediksi, kategori, rekomendasi])
        df_prediksi = pd.DataFrame(data_prediksi, columns=["Wilayah", "Suhu", "Kelembaban", "Tanggal", "Polusi_Udara", "Kategori", "Rekomendasi"])
        st.session_state.hasil_prediksi = df_prediksi

# Tampilkan hasil prediksi jika ada di session_state
if st.session_state.hasil_prediksi is not None:
    df_prediksi = st.session_state.hasil_prediksi
    st.subheader(f"Prediksi Polusi Udara pada {df_prediksi.iloc[0]['Tanggal'].strftime('%Y-%m-%d')}")
    st.dataframe(df_prediksi[["Wilayah", "Polusi_Udara", "Kategori", "Rekomendasi"]])

    # Buat peta dengan marker polusi udara
    m = folium.Map(location=[-6.2, 106.85], zoom_start=11)
    for idx, row in df_prediksi.iterrows():
        folium.CircleMarker(
            location=koordinat_wilayah[row["Wilayah"]],
            radius=10,
            popup=(f"{row['Wilayah']}: {row['Polusi_Udara']:.2f} AQI\n"
                   f"Kategori: {row['Kategori']}\n"
                   f"Rekomendasi: {row['Rekomendasi']}"),
            color=warna_marker(row["Polusi_Udara"]),
            fill=True,
            fill_color=warna_marker(row["Polusi_Udara"]),
        ).add_to(m)
    st_folium(m, width=700, height=500)



import streamlit as st
import requests

st.set_page_config(page_title="Sensor Dashboard", layout="centered")

st.title("📟 Dashboard Sensor Ultrasonik")

try:
    response = requests.get("http://localhost:5000/data")
    data = response.json()
    distance = data.get("distance", 0)
    st.metric("Jarak Terdeteksi", f"{distance:.2f} cm")
except:
    st.error("⚠️ Gagal mengambil data dari server Flask.")

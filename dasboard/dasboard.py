import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import requests
from io import StringIO

url = 'https://raw.githubusercontent.com/nilatiara/Tugas-Bangkit/main/data/day.csv'
response = requests.get(url)

if response.status_code == 200:
    csv_data = StringIO(response.text)
    df_day = pd.read_csv(csv_data)
    
    st.title("Dashboard Analisis Penyewaan Sepeda")

    st.header("1. Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda")

    if not df_day.empty:

        fig, ax = plt.subplots()
        sns.boxplot(x='weathersit', y='cnt', data=df_day, ax=ax)
        ax.set_title('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
        ax.set_xlabel('Kondisi Cuaca (1 = Clear, 2 = Mist, 3 = Light Snow/Rain)')
        ax.set_ylabel('Jumlah Penyewaan Sepeda')

        st.pyplot(fig)

        st.write("""
        **Insight:** Kode ini membuat boxplot untuk melihat bagaimana kondisi cuaca (weathersit) mempengaruhi jumlah penyewaan sepeda (cnt). 
        Cuaca dikelompokkan menjadi beberapa kategori:  
        - 1 = Clear (Cerah)  
        - 2 = Mist (Berkabut)  
        - 3 = Light Snow/Rain (Salju/Hujan Ringan)  
        """)
    else:
        st.error("DataFrame is empty!")
    
    st.header("2. Pengaruh Suhu terhadap Penyewaan Sepeda di Berbagai Musim")

    fig2, ax2 = plt.subplots()
    if 'season' in df_day.columns and 'temp' in df_day.columns and 'cnt' in df_day.columns:
        sns.scatterplot(x='temp', y='cnt', hue='season', data=df_day, ax=ax2)
        ax2.set_title('Pengaruh Suhu terhadap Penyewaan Sepeda di Berbagai Musim')
        ax2.set_xlabel('Suhu (Normalisasi)')
        ax2.set_ylabel('Jumlah Penyewaan Sepeda')
        ax2.legend(title='Season', labels=['Spring', 'Summer', 'Fall', 'Winter'])
        
        st.pyplot(fig2)

        st.write("""
        **Insight:** Kode ini menggunakan scatterplot untuk memvisualisasikan hubungan antara suhu (temp) dan jumlah penyewaan sepeda (cnt) di berbagai musim (season).  
        Setiap titik pada plot diwarnai berdasarkan musim:
        - 1 = Spring (Musim Semi)
        - 2 = Summer (Musim Panas)
        - 3 = Fall (Musim Gugur)
        - 4 = Winter (Musim Dingin)
        """)
    else:
        st.error("Kolom yang dibutuhkan tidak ditemukan dalam DataFrame!")

    st.write("Dashboard ini dibuat oleh Nila Mahardika Tiara Sari")
else:
    st.error(f"Failed to download file, status code: {response.status_code}")

# Dashboard Analisis Penyewaan Sepeda

Proyek ini bertujuan untuk membuat dashboard interaktif menggunakan Streamlit untuk menganalisis data penyewaan sepeda berdasarkan kondisi cuaca dan suhu. Proyek ini menampilkan dua visualisasi utama: boxplot yang menunjukkan pengaruh cuaca terhadap jumlah penyewaan sepeda, dan scatterplot yang menampilkan pengaruh suhu terhadap jumlah penyewaan sepeda di berbagai musim.

## Fitur

1. **Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda**
   - Boxplot yang menunjukkan bagaimana berbagai kondisi cuaca (Cerah, Berkabut, dan Salju/Hujan Ringan) mempengaruhi jumlah penyewaan sepeda.

2. **Pengaruh Suhu terhadap Penyewaan Sepeda di Berbagai Musim**
   - Scatterplot yang menampilkan hubungan antara suhu dan jumlah penyewaan sepeda dengan warna yang berbeda berdasarkan musim (Spring, Summer, Fall, Winter).

## Struktur Proyek

- `day.csv`: Dataset yang digunakan dalam proyek ini. Dataset ini berisi informasi tentang penyewaan sepeda, cuaca, suhu, musim, dan faktor lain yang terkait.
- `dasboard.py`: File Python yang berisi kode untuk menjalankan dashboard Streamlit dan menampilkan visualisasi.
- `README.md`: File ini yang menjelaskan proyek, cara menjalankannya, dan dependensi yang diperlukan.

## Cara Menjalankan Proyek

1. Clone repositori ini ke mesin lokal kamu:
    ```bash
    git clone https://github.com/nilatiara/Tugas-Bangkit
    ```

2. Masuk ke direktori proyek:
    ```bash
    cd Tugas-Bangkit/dasboard
    ```

3. Install dependensi yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```

4. Jalankan aplikasi Streamlit:
    ```bash
    streamlit run dasboard.py
    ```

5. Buka browser dan akses dashboard di alamat `http://localhost:8501`.
atau bisa mengakses link berikut 'https://dasboardd.streamlit.app/'

## Dependensi

Proyek ini menggunakan beberapa pustaka Python berikut:

- **pandas**: Untuk memuat dan memanipulasi dataset.
- **seaborn**: Untuk membuat visualisasi (boxplot dan scatterplot).
- **matplotlib**: Untuk merender visualisasi pada Streamlit.
- **streamlit**: Untuk membuat dashboard interaktif.

Pastikan kamu menginstall semua pustaka ini sebelum menjalankan proyek.

## Dataset

- Dataset yang digunakan dalam proyek ini adalah `day.csv` yang berisi informasi penyewaan sepeda per hari dengan beberapa variabel seperti:
  - `cnt`: Jumlah penyewaan sepeda.
  - `temp`: Suhu (ternormalisasi).
  - `weathersit`: Kondisi cuaca (1 = Clear, 2 = Mist, 3 = Light Snow/Rain).
  - `season`: Musim (1 = Spring, 2 = Summer, 3 = Fall, 4 = Winter).

## Penulis

Proyek ini dibuat oleh **Nila Mahardika Tiara Sari** sebagai bagian dari analisis data penyewaan sepeda.


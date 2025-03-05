# Submission Dicoding " Belajar Analisis Data dengan Python " ✨
Proyek ini menganalisis data Bike Sharing untuk memahami pola penggunaan, pengaruh cuaca, dan faktor lain yang mempengaruhi penyewaan sepeda. Dataset yang digunakan terdiri dari day.csv dan hour.csv, yang berisi berbagai atribut seperti musim, suhu, kelembaban, kecepatan angin, dan jumlah penyewaan.

## 📂 Dataset
Dataset yang digunakan tersimpan dalam folder data yang berisi:
- day.csv: Data penyewaan sepeda harian yang telah dikumpulkan.
- hour.csv: Data penyewaan sepeda per jam.

## Setup Environment
### Setup anaconda
```plaintext
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
### Setup Shell / Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```
### Menjalankan Dashboard
```
streamlit run dashboard.py

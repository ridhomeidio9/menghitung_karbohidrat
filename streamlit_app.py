import streamlit as st

st.set_page_config(page_title="Kalkulator Karbohidrat Harian", layout="centered")

st.title("🍚 Kalkulator Kebutuhan Karbohidrat Harian")

st.markdown("""
Hitung kebutuhan karbohidrat harian berdasarkan berat badan, tinggi badan, usia, jenis kelamin, dan tingkat aktivitas Anda.

💡 Perhitungan menggunakan standar: **55% dari total kalori harian** dialokasikan untuk karbohidrat.
""")

# --- Input Data Pribadi ---
st.header("📋 Data Pribadi")
gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
age = st.number_input("Usia (tahun)", min_value=10, max_value=100, value=25)
weight = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, value=60.0)
height = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=250.0, value=170.0)

# --- Aktivitas ---
st.header("🏃 Tingkat Aktivitas")
activity_level = st.selectbox("Pilih tingkat aktivitas Anda:", [
    "Rendah (sedentari / jarang olahraga)",
    "Sedang (olahraga ringan 3–5 hari/minggu)",
    "Tinggi (latihan intens / pekerjaan fisik berat)"
])

# --- Hitung BMR ---
if gender == "Laki-laki":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

# Faktor aktivitas
activity_factors = {
    "Rendah (sedentari / jarang olahraga)": 1.2,
    "Sedang (olahraga ringan 3–5 hari/minggu)": 1.55,
    "Tinggi (latihan intens / pekerjaan fisik berat)": 1.9
}
activity_multiplier = activity_factors[activity_level]
total_calories = bmr * activity_multiplier

# --- Karbohidrat ---
carb_percent = 55  # Tetap, tidak bisa diubah
carb_grams = (total_calories * (carb_percent / 100)) / 4

# --- Output ---
st.header("📊 Hasil Perhitungan")
st.write(f"**BMR Anda:** {bmr:.0f} kkal/hari")
st.write(f"**Total kalori (termasuk aktivitas):** {total_calories:.0f} kkal/hari")
st.success(f"🎯 Kebutuhan karbohidrat harian: **{carb_grams:.0f} gram** (berdasarkan 55% dari total kalori)")

# --- Referensi Makanan Tinggi Karbohidrat ---
st.header("🍞 Rekomendasi Makanan Tinggi Karbohidrat")

st.markdown("""
Berikut adalah beberapa makanan tinggi karbohidrat yang bisa membantu memenuhi kebutuhan harian Anda:

| Makanan               | Takaran            | Kandungan Karbohidrat |
|----------------------|--------------------|------------------------|
| Nasi putih           | 1 centong (150 g)  | ~53 gram               |
| Kentang rebus        | 1 buah sedang (150 g) | ~30 gram            |
| Roti tawar           | 2 lembar           | ~30 gram               |
| Oatmeal              | 1 mangkuk (40 g)    | ~27 gram               |
| Pisang               | 1 buah sedang      | ~27 gram               |
| Jagung rebus         | 1 buah sedang      | ~25 gram               |
| Singkong rebus       | 100 gram           | ~38 gram               |
| Ubi jalar            | 100 gram           | ~20–25 gram            |
| Mie instan matang    | 1 porsi (150 g)    | ~40–50 gram            |
| Gula pasir           | 1 sdm              | ~13 gram               |

💡 Tips: Pilih karbohidrat kompleks seperti oat, ubi, dan jagung untuk energi lebih stabil dan tahan lama.
""")

st.markdown("---")
st.caption("Referensi: [Alodokter](https://www.alodokter.com/kebutuhan-karbohidrat-per-hari-dan-cara-memenuhinya) | Data makanan: USDA, FatSecret")


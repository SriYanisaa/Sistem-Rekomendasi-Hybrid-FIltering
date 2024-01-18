import csv

# Membuat data uji
data_uji = [
    {"Skincare": "Cleansing Oil, Toner, Serum, Moisturizer", "Jenis_Kulit": "Normal", "Kandungan_Tidak_Cocok": "AHA, BHA"},
    {"Skincare": "Cleansing Gel, Essence, Sunscreen", "Jenis_Kulit": "Kering", "Kandungan_Tidak_Cocok": "Fragrance"},
    {"Skincare": "Micellar Water, Exfoliating Scrub, Night Cream", "Jenis_Kulit": "Berminyak", "Kandungan_Tidak_Cocok": "Alcohol"},
    {"Skincare": "Foaming Cleanser, Hyaluronic Acid Serum, Eye Cream", "Jenis_Kulit": "Sensitif", "Kandungan_Tidak_Cocok": "Retinol"},
    {"Skincare": "Milk Cleanser, Vitamin C Serum, Gel Moisturizer", "Jenis_Kulit": "Kombinasi", "Kandungan_Tidak_Cocok": "Sulfates"}
]

# Menyimpan data uji dalam file CSV
nama_file = "data_test.csv"

with open(nama_file, mode='w', newline='') as file:
    kolom = ["Skincare", "Jenis_Kulit", "Kandungan_Tidak_Cocok"]
    writer = csv.DictWriter(file, fieldnames=kolom)

    # Menulis header
    writer.writeheader()

    # Menulis data uji
    writer.writerows(data_uji)

print(f"Data uji telah disimpan dalam file {nama_file}.")

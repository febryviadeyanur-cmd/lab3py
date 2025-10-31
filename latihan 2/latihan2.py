# Modal awal
modal_awal = 100000000  # 100 juta

# Inisialisasi total keuntungan
total_keuntungan = 0

# Penghasilan setiap bulan dari 1 sampai 8
for bulan in range(1, 9):
    if bulan <= 2:
        laba_bulanan = 0
    elif bulan <= 4:
        laba_bulanan = 0.01 * modal_awal  # 1%
    elif bulan <= 7:
        laba_bulanan = 0.05 * modal_awal  # 5%
    else:  # bulan 8
        laba_bulanan = 0.03 * modal_awal  # 3%

    total_keuntungan += laba_bulanan
    print(f"Bulan {bulan}: Keuntungan = {laba_bulanan}")

# Tampilkan total keuntungan
print(f"Total keuntungan selama 8 bulan: {total_keuntungan}")

# Simulasi Mesin ATM Sederhana

# Saldo awal
saldo = 1000000

print("Selamat datang di Mesin ATM Sederhana")
print(f"Saldo awal Anda: Rp {saldo}")

# Pilihan utama
while saldo > 0:
    print("\nPilih opsi:")
    print("1. Tarik uang")
    print("2. Keluar")

    pilihan = input("Masukkan pilihan (1 atau 2): ")

    if pilihan == "1":
        try:
            jumlah_tarik = int(input("Masukkan jumlah yang ingin ditarik: Rp "))
            if jumlah_tarik <= 0:
                print("Jumlah penarikan harus lebih dari 0.")
            elif jumlah_tarik > saldo:
                print("Saldo tidak mencukupi.")
            else:
                saldo -= jumlah_tarik
                print(f"Penarikan berhasil. Saldo Anda sekarang: Rp {saldo}")
        except ValueError:
            print("Masukkan jumlah yang valid (angka).")

    elif pilihan == "2":
        print("Terima kasih telah menggunakan Mesin ATM. Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

# Jika saldo habis
if saldo == 0:
    print("\nSaldo Anda telah habis. Terima kasih telah menggunakan Mesin ATM.")

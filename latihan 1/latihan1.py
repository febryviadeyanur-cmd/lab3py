import random

# Input nilai N dari pengguna
N = int(input("Masukkan nilai N : "))

# Menghasilkan N bilangan acak
for i in range(1, N + 1):
    # Untuk menghasilkan bilangan acak sampai kurang dari 0.5
    while True:
        num = random.random()
        if num < 0.5:
            print(f"data ke : {i} => {num}")
            break

print("selesai")

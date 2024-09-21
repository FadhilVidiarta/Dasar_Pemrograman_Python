# Fungsi untuk menampilkan hasil berdasarkan input nilai
def tampilkan_hasil(nilai1, nilai2):
    print(f"Nilai pertama: {nilai1}")
    print(f"Nilai kedua: {nilai2}")

    if nilai1 > nilai2:
        print("Nilai pertama lebih besar daripada nilai kedua")
        print("Urutan bilangan dari 0 sampai nilai pertama:")
        for i in range(nilai1 + 1):
            print(i, end=' ')
    elif nilai2 > nilai1:
        print("Nilai kedua lebih besar daripada nilai pertama")
        print("Urutan bilangan dari 0 sampai nilai kedua:")
        for i in range(nilai2 + 1):
            print(i, end=' ')
    else:
        print("Nilai pertama sama dengan nilai kedua")

# Meminta input dari pengguna
nilai1 = int(input("Masukkan nilai pertama: "))
nilai2 = int(input("Masukkan nilai kedua: "))

# Memanggil fungsi untuk menampilkan hasil
tampilkan_hasil(nilai1, nilai2)

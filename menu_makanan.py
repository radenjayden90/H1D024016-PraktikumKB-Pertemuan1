import random
import datetime

# struktur data
menu = ["Nasi Goreng", "Mie Goreng", "Ayam Bakar", "Sate Ayam", "Gado-Gado"]

while True:
    print("\nMenu Makanan:")
    print("1. Lihat Menu")
    print("2. Rekomendasi Menu")
    print("3. Keluar")
    
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        print("\nDaftar Menu:")
        for makanan in menu:
            print("- " + makanan)
    
    elif pilihan == "2":
        rekomendasi = random.choice(menu)
        waktu = datetime.datetime.now()
        print("Menu rekomendasi:", rekomendasi)
        print("Waktu:", waktu)
    
    elif pilihan == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
from datetime import datetime

# Dictionary untuk akun pengguna
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

# List berisi Tuple
koleksi_parfum = [
    ("Sauvage", "Fresh Spiced", 1800000),
    ("Baccarat Rouge 540", "Woody Amber", 4500000),
    ("Black Opium", "Warm Vanilla", 2100000),
    ("Bleu de Chanel", "Citrus Woody", 2300000)
]


# Function Login
def login():
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and password == users[username]["password"]:
        print("Login berhasil!")
        return username, users[username]["role"]

    print("Username atau password salah!")
    return None, None


# Function menampilkan parfum
def lihat():
    print("\n=== KOLEKSI PARFUM ===")

    for i, parfum in enumerate(koleksi_parfum, 1):
        print(f"{i}. {parfum[0]} | {parfum[1]} | Rp{parfum[2]:,}")


# Function tambah parfum
def tambah():
    print("\n=== TAMBAH PARFUM ===")

    nama = input("Nama parfum: ")
    kategori = input("Kategori: ")
    harga = input("Harga: ")

    if nama == "" or kategori == "":
        print("Data tidak boleh kosong!")

    elif not harga.isdigit():
        print("Harga harus berupa angka!")

    else:
        koleksi_parfum.append(
            (nama, kategori, int(harga))
        )
        print("Parfum berhasil ditambahkan!")
        print("Waktu:", datetime.now().strftime("%d-%m-%Y %H:%M"))


# Function edit parfum
def edit():
    lihat()

    nomor = input("\nNomor parfum yang ingin diedit: ")

    if not nomor.isdigit() or int(nomor) > len(koleksi_parfum):
        print("Nomor tidak valid!")
        return

    nomor = int(nomor) - 1

    nama = input("Nama baru: ")
    kategori = input("Kategori baru: ")
    harga = input("Harga baru: ")

    if nama == "" or kategori == "" or not harga.isdigit():
        print("Input tidak valid!")
        return

    koleksi_parfum[nomor] = (
        nama,
        kategori,
        int(harga)
    )

    print("Parfum berhasil diubah!")


# Function hapus parfum
def hapus():
    lihat()

    nomor = input("\nNomor parfum yang ingin dihapus: ")

    if nomor.isdigit() and 1 <= int(nomor) <= len(koleksi_parfum):
        parfum = koleksi_parfum.pop(int(nomor) - 1)
        print(f"{parfum[0]} berhasil dihapus!")
    else:
        print("Nomor tidak valid!")


# Program utama
while True:

    username, role = login()

    if username is None:
        break

    while True:

        print("\n=== SISTEM KOLEKSI PARFUM ===")

        if role == "admin":
            print("1. Lihat")
            print("2. Tambah")
            print("3. Edit")
            print("4. Hapus")
            print("5. Logout")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                lihat()

            elif pilihan == "2":
                tambah()

            elif pilihan == "3":
                edit()

            elif pilihan == "4":
                hapus()

            elif pilihan == "5":
                print("Logout berhasil!")
                break

            else:
                print("Menu tidak valid!")

        else:
            print("1. Lihat Koleksi")
            print("2. Logout")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                lihat()

            elif pilihan == "2":
                print("Logout berhasil!")
                break

            else:
                print("Menu tidak valid!")
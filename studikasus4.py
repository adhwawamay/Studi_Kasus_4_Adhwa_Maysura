buku = {
    "judul": "One hundred Years of Solitude",
    "penulis": "Gabriel Garcia Marquez",
    "tahun_terbit": 1967
}

while True:
    print("\nDATA BUKU")
    print("1. Tampilkan Data Buku")
    print("2. Tambahkan Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Tampilkan Data Setelah Perubahan")
    print("6. Berhentikan Sistem")

    pilihan = input("Tentukan opsi (1-6): ")

    if pilihan == "1":
        print("\nDATA BUKU")
        print("Judul       :", buku["judul"])
        print("Penulis     :", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])


        if "penerbit" in buku:
            print("Penerbit    :", buku["penerbit"])

    elif pilihan == "2":
        penerbit = input("Ketik nama penerbit: ")
        buku["penerbit"] = penerbit
        print("Nama penerbit berhasil ditambahkan.")

    elif pilihan == "3":
        penulis_baru = input("Ketik nama penulis baru: ")
        buku["penulis"] = penulis_baru
        print("Nama penulis berhasil diubah.")

    elif pilihan == "4":
        if "penerbit" in buku:
            buku.pop("penerbit")
            print("Nama penerbit berhasil dihapus.")
        else:
            print("Nama penerbit belum tersedia.")

    elif pilihan == "5":
        print("\nDATA AKHIR BUKU SETELAH PERUBAHAN")
        print("Judul       :", buku["judul"])
        print("Penulis     :", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])

        if "penerbit" in buku:
            print("Penerbit    :", buku["penerbit"])
        else:
            print("Penerbit    : Tidak ada")

    elif pilihan == "6":
        print("\nSistem telah berhasil dijalankan <Sistem Berhenti>. Terima kasih :D")
        break

    else:
        print("Pilihan tidak tersedia. Silakan memilih kembali opsi 1-6.")
        
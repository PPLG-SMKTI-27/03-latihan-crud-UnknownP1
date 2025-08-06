def bersih():
    import time
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


# data buku
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""}
]

def tampilkan_data():
    if len(books) == 0:
        print("Data tidak di temukan")
    else:
        print("+=+=+=+     Barang      +=+=+=+")
        angka = 1
        for i in books:
            print(f"{angka}.\tIsbn : {i['isbn']} Judul : {i['judul']} || Pengarang : {i['pengarang']}  Jumlah : {i['jumlah']}  Terpinjam : {i['terpinjam']} \n")
            angka = angka + 1
        angka = 1

def tambah_data():
    isbn = int(input("Masukkan ISBN : "))
    judul = str(input("Masukkan Judul : "))
    pengarang = str(input("Masukkan Pengarang : "))
    jumlah = int(input("masukan Jumlah Buku : "))
    terpinjam = int(input("masukan Jumlah Terpinjam : "))
    
    item_baru = {
        "isbn": isbn,
        "judul": judul,
        "pengarang": pengarang,
        "jumlah": jumlah,
        "terpinjam": terpinjam
    }

    books.append(item_baru)
    print("Item berhasil ditambahkan!")


def edit_data():
    if len(books) == 0:
        print("Item Tidak Ditemukan")
    else:
        tampilkan_data()
        index = int(input("Masukkan index : "))
        if index >= 0 and index < len(books):
            isbn = int(input("Masukkan isbn : "))
            while True:
                try:        
                    judul = str(input("Masukkan Judul : "))
                    break
                except ValueError:
                    print("tidak ada index")
            while True:
                try:        
                    pengarang = str(input("Masukkan Pengarang : "))
                    break
                except ValueError:
                    print("tidak ada index")
            while True:
                try:
                    jumlah = int(input("Masukkan Jumlah Stok : "))
                    if jumlah < 0:
                        print("barang tidak boleh kurang dari 0")
                        continue
                    break
                except ValueError:
                    print("inputan anda tidak valid")
            while True:
                try:
                    terpinjam = int(input("Masukkan Terpinjam : "))
                    if terpinjam < 0:
                        print("barang tidak boleh kurang dari 0")
                        continue
                    break
                except ValueError:
                    print("inputan anda tidak valid")
            new_barang = {"isbn" : isbn, "judul": judul, "pengarang": pengarang, "jumlah" : jumlah, "terpinjam" : terpinjam}
            books [index] = new_barang
            print("Barang Berhasil Di Update")
        else:
            print("indeks tidak valid\n")

def hapus_data():
    tampilkan_data()
    index = int(input("Masukan item yang anda ingin hapus : ")) - 1
    if 0 <= index < len(books):
        books.pop(index)
        print("Barang Telah Di hapus")
    else:
        print("item tidak ditemukan")

def tampilkan_peminjaman():
    if len(books) == 0:
        print("Data tidak di temukan")
    else:
        print("+=+=+=+     Buku Yang Dipinjam      +=+=+=+")
        angka = 1
        for l in records:
            print(f"{angka}.\tIsbn : {l['isbn']} Status : {l['status']} || Tanggal Dipinjam : {l['tanggal_pinjam']}  Tanggal Dikembalikan : {l['tanggal_kembali']}\n")
            angka = angka + 1
        angka = 1

def tampilkan_belum():
    if len(books) == 0:
        print("Buku Tidak dikembalikan")
    else:
        angka = 1
    for l in records:
            print(f"{angka}.\tIsbn : {l['isbn']} Status : {l['status']} || Tanggal Dipinjam : {l['tanggal_pinjam']}")
            angka = angka + 1
    angka = 1
                  
def peminjaman():
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")

    for book in books:
        if book['isbn'] == isbn:
            if book['terpinjam'] < book['jumlah']:
                book['terpinjam'] += 1
                records.append({
                    "isbn": isbn,
                    "status": "Belum",
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": ""
                })
                print("Peminjaman berhasil dicatat.\n")
                return
            else:
                print("Semua salinan buku sudah dipinjam.\n")
                return
    print("ISBN buku tidak ditemukan.\n")
def pengembalian():
    isbn = input("Masukkan ISBN buku yang dikembalikan: ")
    tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")

    for record in records:
        if record['isbn'] == isbn and record['status'].lower() == "belum":
            record['status'] = "Selesai"
            record['tanggal_kembali'] = tanggal_kembali

            for book in books:
                if book['isbn'] == isbn:
                    book['terpinjam'] -= 1
                    print("Pengembalian berhasil dicatat.\n")
                    return
    print("Peminjaman yang cocok tidak ditemukan atau sudah dikembalikan.\n")


def menu():
    while True:
        print("---=== MENU ===---")
        print("[1] Tampilkan Data")
        print("[2] Tambah Data")
        print("[3] Edit Data")
        print("[4] Hapus Data")
        print("------------------")
        print("[5] Tampilkan Semua Peminjaman") 
        print("[6] Tampilkan Peminjaman Belum Kembali")
        print("[7] Peminjaman")
        print("[8] Pengembalian")
        print("[X] Keluar")
        pilihan = input("Masukkan pilihan menu (1-8 atau x): ")
     
        if pilihan == "1":
            bersih()
            tampilkan_data()
        
        elif pilihan == "2":
            bersih()
            tambah_data()
        
        elif pilihan == "3":
            bersih()
            edit_data()
        
        elif pilihan == "4":
            bersih()
            hapus_data()
            
            
        elif pilihan == "5":
            bersih()
            tampilkan_peminjaman()
            
        elif pilihan == "6":
            bersih()
            tampilkan_belum()
            
            
        elif pilihan == "7":
            bersih()
            peminjaman()
            
        elif pilihan == "8":
            bersih()
            pengembalian()   

        elif pilihan == "" or "X":
            bersih()
            print("Terima kasih Telah Menggunakan Aplikasinya!")
            return False
        else: 
            bersih()
            print("Pilihan tidak valid, Silahkan coba lagi")
            break

menu()
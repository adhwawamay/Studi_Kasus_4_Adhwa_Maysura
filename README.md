# Studi_Kasus_4_Adhwa_Maysura

Nama : Adhwa Maysura<br>
Nim : 2609116103<br>
Kelas : C

## Penyimpanan Dan Pengelolaan Data Buku


### Data buku Dictionary
<img width="1920" height="258" alt="1 stu 4" src="https://github.com/user-attachments/assets/7148df79-69f1-4804-8955-43694bd9983f" /><br> 

1. Di step awal kita akan membuat data buku terlebih dahulu, pada bagian ini berguna untuk menyimpan data buku dalam bentuk **Dictionary** (key & value).

### While True
<img width="1817" height="309" alt="2 stu 4" src="https://github.com/user-attachments/assets/02f1fd62-fa01-4b1d-adba-abc47f466e70" />

1. Kemudian ada kode **While_True** yang akan mengatur sistem terus berjalan dan menampilkan menu berulang kali sampai pengguna memilih opsi ke-6 untuk memberhentikan sistem.

2. Dibawah nya terdapat opsi **input** agar pengguna dapat menentukkan opsi yang ingin ia jalankan.

### Menu 1
<img width="1838" height="199" alt="3 stu 4" src="https://github.com/user-attachments/assets/8049153c-514e-4cef-a93d-7354bb934040" /><br>

1. Kode **If** digunakan untuk mengecek pilihan pengguna, maka jika pengguna memilih opsi '1' program akan menampilkan keseluruhan data buku sesuai dengan perintah <key & value>.
 
<img width="1453" height="151" alt="4 0" src="https://github.com/user-attachments/assets/50c64cd4-50be-485f-813b-eeafc75c04a5" /><br>

1. Kode tersebut berguna untuk mengecek key 'penerbit' pada data buku (dictionary).

### Menu 2
<img width="1809" height="234" alt="4 4" src="https://github.com/user-attachments/assets/43e12847-00a7-4208-81d2-35ee7978c659" />

1. lalu di opsi '2' digunakan untuk menambahkan data penerbit, yang dimana pengguna dengan bebas dapat mengetik/menambahkan data penerbit.

2. Kode **Elif** digunakan untuk menjalankan perintah lainnya, jika kode 'if' tidak terpenuhi.

### Menu 3
<img width="1590" height="165" alt="5 4" src="https://github.com/user-attachments/assets/d2f528bc-d856-4769-b63b-9469e78d9729" /><br>

1. Lalu pada **elif pilihan == "3"** opsi ini berisikan perintah untuk mengubah nama penulis, pengguna dapat memasukkan nama penulis baru yang nanti nya menjadi pengganti nilai dari key "penulis".

### Menu 4
<img width="1804" height="212" alt="6 4" src="https://github.com/user-attachments/assets/7af38b23-2725-47ed-8377-9dc0cfe3cd8d" /><br>

1. Pada opsi '4' memerintahkan untuk menghapus data penerbit secara otomatis melalui kode **buku.pop("penerbit")**, namun jika 'penerbit' memang belum ada pada data buku maka sistem otomatis akan mengecek & menjalankan ouput "Nama penerbit belum tersedia".

### Menu 5
<img width="1753" height="326" alt="8 4" src="https://github.com/user-attachments/assets/5f645f06-e272-4af7-af44-00188e59f8d6" /><br>

1. Opsi '5' Digunakan untuk menampilkan hasil data buku setelah pengguna melakukan perubahan.

2. lalu pada kode **If "penerbit" in buku** sistem akan mengecek apakah penerbit masih tersedia, namun jika pengguna menjalankan opsi '4' maka output akan seperti ini "Penerbit : Tidak ada".

### Menu 6
<img width="1775" height="258" alt="9 4" src="https://github.com/user-attachments/assets/a4a95fe4-158a-445e-887a-1cb5ab83f441" /><br>

1. Lalu pada opsi ke '6' sesuai dengan perintah untuk menghentikan sistem dari **While_True** melalui kode **break**.

2. Namun jika pengguna ada menjalankan opsi selain yang tertera di sistem maka sistem akan memberi pesan "pilihan tidak tersedia. Silahkan memilih kembali opsi (1-6)".


## Output (Run) Dari Sistem Tersebut

### Run menu 1
<img width="1618" height="375" alt="run 1 4" src="https://github.com/user-attachments/assets/8e1b7983-f3b6-4f5b-b8c7-2d5b98667e1a" />

### Run menu 2
<img width="1646" height="310" alt="run 2 4" src="https://github.com/user-attachments/assets/cd70a7d3-2caf-4528-975f-f2cec4e586a6" />

### Run menu 3
<img width="1855" height="278" alt="run 3 4" src="https://github.com/user-attachments/assets/3b1c9230-f9eb-48af-8d70-bf78f6d611a8" />

### Run menu 4
<img width="911" height="132" alt="run 4 4" src="https://github.com/user-attachments/assets/206ec0cf-2284-49f1-9344-eb61aafa4cef" />

### Run menu 5
<img width="866" height="206" alt="run 5 4" src="https://github.com/user-attachments/assets/5ca46459-0267-4ff2-8c3d-ce28a73ad436" />

### Run menu 6
<img width="885" height="167" alt="run 6 4" src="https://github.com/user-attachments/assets/ff879d4f-3058-48ad-ae59-ca6a3f092b34" />

<img width="1839" height="271" alt="run 7 4" src="https://github.com/user-attachments/assets/80c15265-d913-4844-bbd7-fe33732e20f6" />













# -*- coding: utf-8 -*-
"""Tupple.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oVQfUvu01tDir5OoclsNwn_nk8UZBZf4
"""

# Membuat tuple kosong
kosong = ()

# membuat tuple
satu = ('Isinya',)
siji = "isinya siji",

# membuat tuple
nama = ('petani', 'kode', 'linux')

# mengakses nilai tuple
print(nama[1])

# mula-mula kita punya tuple seperti ini
web = (123, 'Petani Kode', 'https://www.petanikode.com')

# lalu kita ingin potong agar ditampilkan
# dari indeks nomer 1 sampai 2
print(web[1:2])

# Membuat Tuple
hari = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jum\'at', 'Sabtu', 'Minggu')

# Mengambil panjang tuple hari
print("Jumlah hari: %d" % len(hari))

tuple1 = "aku", "cinta", "kamu"
tuple2 = "selama", 3, "tahun"
tuple3 = (tuple1, tuple2) # <- nested tuple
print(tuple3)

# mula-mula kita buat tuple seperti ini
web = 123, "Petani Kode", "https://www.petanikode.com"

# lalu di-unpacking
id_web, nama, url = web

# maka sekarang tiga variabel tersebut akan bernilai
# sesuai yang ada di dalam tuple
#
# mari kita cetak
print(id_web)
print(nama)
print(url)
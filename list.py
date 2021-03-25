# -*- coding: utf-8 -*-
"""List.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fL1ovo7YLZ5GB65rez5WUZuAGyEaosLY
"""

#Membuat List Kosong

warna = []

#membuat list dengan 1 isi
hobi = ["membaca"]

#membuat list dengan lebih dari 1 isi
buah = ["apel", "anggur", "mangga", "jeruk"]

#list dengan beda tipe data
laci = ["buku", 21, True, 34.345]

#mengambil nilai dari list
buah = ["apel", "anggur", "mangga", "jeruk"]
print(buah[2])

#Latihan 1 membuat program sederhana
my_friends = ["zahwa", "hasan", "nisa", "addyat", "arif"]

#menampilkan semua teman
for i in my_friends:
  print(i)

#mengganti nilai list
buah = ["apel", "anggur", "mangga", "jeruk"]
buah[2] = "jambu"
print(buah)

#menambahkan item ke dalam list
#prepend = didepan
#append = dibelakang
#insert(index, item) = menyisipkan 


buah2 = ["apel", "anggur", "mangga", "jeruk"]

#menambahkan diawal
#buah2.prepend("melon")

#menambahkan di akhir
buah2.append("duren")

#menambah di sela
buah2.insert(2, "semangka")

#menampilkan
print(buah2)

hobi = []
stop = False
i = 0

# Mengisi hobi
while(not stop):
    hobi_baru = input("Inputkan hobi yang ke-{}: ".format(i))
    hobi.append(hobi_baru)

    # Increment i
    i += 1
    
    tanya = input("Mau isi lagi? (y/t): ")
    if(tanya == "t"): 
        stop = True


# Cetak Semua Hobi
print("=" * 10) 
print("Kamu memiliki {} hobi".format(len(hobi)))
for hb in hobi:
    print( "- {}".format(hb))

#Menhapus list

# Membuat List
todo_list = [ 
             "Balajar Python", 
             "Belajar Django", 
             "Belajar MongoDB", 
             "Belajar Sulap", 
             "Belajar Flask"] 
# Misalkan kita ingin menghapus "Belajar Sulap"
# yang berada di indeks ke-3
del todo_list[3] 
print(todo_list)

#Menhapus list 2
# mula-mula kita punya list
a = ["a", "b", "c", "d"]
# kemudian kita hapus b
a.remove("b")

print(a)

#memotong list
# Kita punya list warna
warna = ["merah", "hijau", "kuning", "biru", "pink", "ungu"]

# Kita potong dari indeks ke-1 sampai ke-5
print(warna[1:5])

#operasi penjumlahan list 
# Beberapa list lagu
list_lagu = [
    "No Women, No Cry",
    "Dear God"
]

# playlist lagu favorit
playlist_favorit = [
    "Break Out",
    "Now Loading!!!"
]

# Mari kita gabungkan keduanya
semua_lagu = list_lagu + playlist_favorit

print(semua_lagu)

#perkalian
# playlist lagu favorit
playlist_favorit = [
    "Break Out",
    "Now Loading!!!"
]

# ulangi sebanyak 5x
ulangi = 5

now_playing = playlist_favorit * ulangi

print(now_playing)

#List 2 Dimensi
# List minuman dengan 2 dimensi
list_minuman = [
    ["Kopi", "Susu", "Teh"],
    ["Jus Apel", "Jus Melon", "Jus Jeruk"],
    ["Es Kopi", "Es Campur", "Es Teler"]
]

# Cara mengakses list multidimensi
# misalkan kita ingin mengambil "es kopi"
print(list_minuman[2][0])

# List minuman dengan 2 dimensi
list_minuman = [
    ["Kopi", "Susu", "Teh"],
    ["Jus Apel", "Jus Melon", "Jus Jeruk"],
    ["Es Kopi", "Es Campur", "Es Teler"]
]

for menu in list_minuman:
    for minuman in menu:
        print(minuman)
# -*- coding: utf-8 -*-
"""functionClassCode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FGCnfnEgE3DuZzA7W075T6GZcLPsWOYn
"""

#fungsi dengan parameter
#deklarasi fungsi
def datadiri(nama, kota):
  "menampilkan nama dan kota"
  print('Nama Anda : ', nama)
  print('Dari Kota :', kota)

#program utama
nama = input('Masukan nama Anda : ')
kota = input('Masukan kota asal : ')

#memanggil fungsi
datadiri(nama, kota)

#fungsi dengan parameter dan kembalian
#deklarasi fungsi
def perkalian(bil1, bil2):
  "menghitung perkalian 2 bilangan bulat"
  hasil = bil1 * bil2
  return hasil

#program utama
bil1= int(input('input bil 1 : '))
bil2= int(input('input bil 2 : '))

#memanggil fungsi
print('Hasil perkalian ', bil1, ' dengan ', bil2, ' adalah ', perkalian(bil1, bil2))

#Melewatkan Argumen dengan Kata Kunci
def perkalian(bil1, bil2):
   "menghitung perkalian 2 bilangan bulat"
  hasil = bil1 * bil2
  return hasil

#program utama
bil1= int(input('input bil 1 : '))
bil2= int(input('input bil 2 : '))

#memanggil fungsi
print('Hasil perkalian ', bil1, ' dengan ', bil2, ' adalah ',
      perkalian(bil1, bil2))

#class
class Product:
	__vendor_message = "Ini adalah rahasia"
	name = ""
	price = ""
	size = ""
	unit = ""

	def __init__(self, name):
		print("Ini adalah constructor")
		self.name = name
		self.unit = "ml"
		self.size = 250

	def get_vendor_message(self):
		print(self.__vendor_message)

	def set_price(self, price):
		self.price = price

p = Product("Ultora Milek")
p.set_price(5500)

print("%s dengan ukuran %s %s harganya Rp. %d" % (p.name, p.size, p.unit, p.price))
# print p.__vendor_message

p.get_vendor_message()

p1 = Product("Indomilek")
p1.set_price(5000)

print("%s dengan ukuran %s %s harganya Rp. %d" % (p.name, p.size, p.unit, p.price))

print(p == p)
print(p1 == p1)
print(p == p1)
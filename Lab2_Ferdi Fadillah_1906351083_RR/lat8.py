# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:31:39 2019

@author: ferdi.fadillah
"""

#Masukkan konstanta bertipe data integer sesuai variabel yang diinginkan
Panjang = int(input("Masukkan panjang sisi persegi:"))
X1 = int(input("Masukkan komponen X dari titik kiri bawah persegi pertama:"))
Y1 = int(input("Masukkan komponen Y dari titik kiri bawah persegi pertama"))
X2 = int(input("Masukkan komponen X dari titik kiri bawah persegi kedua:"))
Y2 = int(input("Masukkan komponen Y dari titik kiri bawah persegi kedua: "))

#Syarat Persegi Berisisan
if (X1+Panjang, Y1+Panjang) >= (X2, Y2) and (X2+Panjang, Y2+Panjang) >= (X1, Y1):
    print("Persegi Beririsan")

#Yang bukan syarat Persegi Berisisan, yang berarti persegi terpisah       
else:
    print("Persegi Terpisah")
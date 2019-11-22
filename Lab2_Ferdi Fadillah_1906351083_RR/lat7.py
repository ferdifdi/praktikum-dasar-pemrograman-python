# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:55:12 2019

@author: ferdi.fadillah
"""

#Masukkan konstanta bertipe data integer sesuai variabel yang diinginkan
Panjang = int(input("Masukkan panjang sisi persegi:"))
Patokan_X = int(input("Masukkan komponen X dari titik kiri bawah persegi:"))
Patokan_Y = int(input("Masukkan komponen Y dari titik kiri bawah persegi:"))
Cek_X = int(input("Masukkan komponen X dari titik yang ingin dicek:"))
Cek_Y = int(input("Masukkan komponen Y dari titik yang ingin dicek:"))

#Syarat titik di tepi persegi
if ((Cek_X == Patokan_X or Cek_X == Patokan_X+Panjang) and (Patokan_Y <= Cek_Y <= Patokan_Y+Panjang)) or ((Cek_Y == Patokan_Y or Cek_Y == Patokan_Y+Panjang) and (Patokan_X <= Cek_X <= Patokan_X+Panjang)): 
    print("Di tepi")
#Syarat titik di dalam persegi
elif (Patokan_X, Patokan_Y) < (Cek_X, Cek_Y) < (Patokan_X+Panjang, Patokan_Y+Panjang):   
    print("Di dalam")    
#Yg bukan syarat titik di tepi atau pun di dalam persegi, yang berarti titik di luar persegi       
else:
    print("Di luar")

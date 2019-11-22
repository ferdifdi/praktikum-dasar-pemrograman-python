# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:48:47 2019

@author: ferdi.fadillah
"""

#inputan lebar dasi
lebar_dasi = int(input("Masukkan lebar dasi (harus kelipatan 2 dan >= 4): "))

#dasi atas
for i in range (lebar_dasi//2-1):
    print("|" + " "*i + "\\" + " "*(lebar_dasi-4-2*i) + "/" + " "*i + "|") 

#dasi bawah    
for j in range (lebar_dasi//2-1):
    print("|" + " "*((lebar_dasi//2-1)-(j+1)*1) + "/" + " "*(2*j) + "\\" + " "*((lebar_dasi//2-1)-(j+1)*1) + "|") 

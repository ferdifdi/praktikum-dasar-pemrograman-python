# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:06:31 2019

@author: ferdi.fadillah
"""

Permen_Biru = int(input("Masukkan banyak permen biru yang dimiliki: "))
Tukar_Permen = int(input("Masukkan permen biru yang dibutuhkan untuk penukaran 1 permen merah: "))

Permen_Merah_Yang_Didapat = int(Permen_Biru / Tukar_Permen)
Permen_Biru_Yang_Tersisa = int(Permen_Biru - (Permen_Merah_Yang_Didapat * Tukar_Permen))

print("Pak Chanek mempunyai",Permen_Merah_Yang_Didapat," permen merah")
print("dengan",Permen_Biru_Yang_Tersisa," permen biru yang tersisa")
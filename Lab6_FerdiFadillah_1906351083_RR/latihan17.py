# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:12:31 2019

@author: ferdi.fadillah
"""

def baca_matriks():    
    
    dimensi = input("Masukkan dimensi (baris dan kolom, dipisah oleh spasi):")
    dimensi_list = [] 
     
    dimensi = dimensi.split()       
    for elemen in dimensi:
        dimensi_list.append(elemen)
    baris = int(dimensi_list[0])
    
    print("Masukkan isi matriks:")
    isi_list = []
    for i in range (baris):
        isi_per_baris = input()     
        isi = isi_per_baris.split() 
        isi_list.extend(isi)
    
    isi_list.sort() 
    return isi_list
            
def matriks_sama(matriks_1,matriks_2):
    if matriks_1 == matriks_2:
        return True
    return False

print("Masukkan matriks pertama:")    
matriks_1 =  baca_matriks()
print("Masukkan matriks kedua:")
matriks_2 =  baca_matriks()

if matriks_sama(matriks_1,matriks_2):
    print('Isi matriks sama!')
else:
    print('Isi matriks berbeda!')
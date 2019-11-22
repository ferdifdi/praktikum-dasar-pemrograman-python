# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:12:11 2019

@author: ferdi.fadillah
"""

def baca_list(angka):
    angka = angka.split() #angka dibagi    
    angka.sort()   
    angka_list = [] 
    
    #menghindari duplikasi angka saat penambahan kata
    for elemen in angka:
        if elemen not in angka_list:
            angka_list.append(elemen)
            
    return angka_list        
    
def list_sama(list_1,list_2):
    if list_1 == list_2:
        return True
    return False
    
list_1 = baca_list(input('Masukkan list pertama (angka dipisah oleh spasi):'))
list_2 = baca_list(input('Masukkan list kedua (angka dipisah oleh spasi):'))

if list_sama(list_1,list_2):
    print('Isi list sama!')
else:
    print('Isi list berbeda!')
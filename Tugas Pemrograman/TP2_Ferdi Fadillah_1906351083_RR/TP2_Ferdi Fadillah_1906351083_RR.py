# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:42:39 2019

@author: USER
"""

import numpy as np
import matplotlib.pyplot as plt
import math


#INPUT STRING MENJADI LIST OF STRING

print("=======================================================") 
print("Masukkan pesan: (untuk berhenti masukkan string kosong)") 
print("=======================================================")

#list my_list kosong
my_list = []

#memasukkan pesan berupa string berulang-ulang
i = 1 
while i != 0:
    pesan = input("Pesan: ")   
    my_list.append(pesan) #menambahkan pesan     
    
    #jika pesan kosong, maka perulangan berhenti
    if pesan == "":
        i = 0 
              
my_list.remove('') #menghapus string kosong


#TOKENISASI SETIAP STRING

def tokenisasi_str(str):
    
    my_file = open("TP2-stopword.txt", "r") #membuka dan membaca file 
    stopword = my_file.read().split() #membagi kata
    
    #mengecilkan semua huruf dan membuang tanda baca kecuali tanda baca pada ​reduplicated word 
    temp=''
    for kalimat in str: 
        for char in kalimat:
            if char.lower() in 'abcdefghijklmnopqrstuvwxyz123456789- ':
                temp+=char.lower()
        temp+=' '    
    str=temp.split()
    
    #membuang - jika ada
    if "-" in str:
        str.remove("-")
    
    #membuang kata yang ada di stopword
    temp=''
    for kata in str:
        if kata not in stopword:
                temp+=kata
        temp+=' '    
    str=temp.split()
    
    return str    

str = my_list
tokenisasi_str(str)


#HITUNG KEMUNCULAN KATA DAN BUAT GRAFIKNYA

#list frekuensi kosong
frekuensi = []

def kemunculan_kata(str):
    
    print("=======================================")
    print(f'{"No":3s} {"Kata":25s} {"Frekuensi"}')
    print("=======================================")
    
    str = str.split() #string dibagi
    str_list = [] 
    
    #menghindari duplikasi kata saat penambahan kata
    for kata in str:
        if kata not in str_list:
            str_list.append(kata)
   
    #mencetak kata dan frekuensinya               
    for i in range(0, len(str_list)):
        print(f'{i+1:3d} {str_list[i]:25s} {str.count(str_list[i])}')

        #menambahkan list frekuensi dgn bbrp data int scr berulang sehingga membentuk list of int
        frekuensi.append(str.count(str_list[i]))      
        
    #mengatur ukuran gambar
    #frekuensi tertinggi dalam rentang 1-4, menghasilkan panjang gambar 5
    #frekuensi tertinggi dalam rentang 5-8, menghasilkan panjang gambar 10
    #dst
    #banyak daftar kata dalam rentang 1-10, menghasilkan tinggi 5
    #banyak daftar kata dalam rentang 11-20, menghasilkan tinggi 10
    #dst    
    plt.figure(figsize=((math.ceil(max(frekuensi)/4)*5,(math.ceil(len(str_list)/10)*5))))
    
    y_pos = np.arange(len(str_list)-1,-1,-1)  #menguruti list kata dari atas sampai bawah
    plt.barh(y_pos, frekuensi) #membuat bar-bar horizontal yg setiap bar nya sepanjang frekuensi
    plt.yticks(y_pos, str_list)   #menambahkan list kata di sumbu y 
    plt.title('Frekuensi Kemunculan Kata')
    plt.xlabel('Frekuensi')        
    plt.show()

str = (' '.join(tokenisasi_str(str))) #hasil dari tokenisasi_str yg berupa list diubah menjadi string
kemunculan_kata(str)

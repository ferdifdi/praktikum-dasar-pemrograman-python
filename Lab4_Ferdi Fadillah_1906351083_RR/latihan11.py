# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:48:46 2019

@author: ferdi.fadillah
"""

#inputan teks
teks = input("Masukkan teks: ")

jumlah_tawa = 0

#membagi teks menjadi kata per kata
for kata in teks.split(): 
    #jika kata tsb adalah wkwk..w atau wkwk..wk tapi bukan w
    if ( kata ==  ('wk' * (len(kata) // 2)) or kata == ('wk' * (len(kata) // 2)+'w') ) and kata != "w" :
        print(kata.upper(), end=' ') #maka kata tsb huruf-hurufnya diganti menjadi huruf besar
        jumlah_tawa += 1 #menghitung jumlah tawa
    else: #jika kata tsb tdk sesuai kondisi yang kita mau
        print(kata, end=' ') #maka dicetak tanpa perubahan     

#mencetak jumlah tawa        
print("Tertawa wkwk sebanyak ", jumlah_tawa," kali")
            
            
        
        
        

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:52:07 2019

@author: USER
"""

#Buatlah program yang menerima sebuah bilangan bulat N (1 <= N <= 1000), kemudian              tampilkan angka dari 1 sampai N, namun: 
#-     Setiap kelipatan 3 diganti dengan ‘Bing!’. -     Setiap kelipatan 7 diganti dengan ‘Bung!’. -     Setiap kelipatan 21 diganti dengan ‘BingBung!’.

#inputan bilangan bulat N (1 <= N <= 1000)

bilangan = int(input("Masukkan sebuah bilangan bulat N (1 <= N <= 1000):"))

#perulangan mencetak bilangan sebanyak yang diinputkan
for i in range(bilangan):
    i += 1 #bilangan yang dicetak selalu ditambahkan 1 setiap dicetak
    if i % 3 == 0 and i % 7 == 0: # Setiap kelipatan 21 dicetak dengan ‘BingBung!’
        print("BingBung!") 
    elif i % 3 == 0: #Setiap kelipatan 3 dicetak dengan ‘Bing!’
        print("Bing!") 
    elif i % 7 == 0: #Setiap kelipatan 7 dicetak dengan ‘Bung!’
        print("Bung!")  
    else: #yang bukan kelipatan 3 atau 7, dicetak bilangan itu sendiri
        print(i) 
     
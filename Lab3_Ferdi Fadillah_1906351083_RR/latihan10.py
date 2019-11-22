# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:11:29 2019

@author: USER
"""

LP_Anda = 1000
LP_Musuh = 1000
Serangan = ""

while (LP_Anda > 0 and LP_Musuh > 0): 
    print("------------------------")
    print("LP Anda: ",LP_Anda)
    print("LP Musuh: ",LP_Musuh)
    print("------------------------")
    print("Apa yang ingin Anda lakukan?")
    print("1. Serang dengan scratch (100 LP)")
    print("2. Serang dengan throw (300 LP)")
    print("3. Serang dengan flamethrower (500 LP)")
    print("4. Tangkap musuh Anda")
    Serangan = int(input("Masukkan nomor pilihan: "))
    if Serangan == 1:
        print("Anda menggunakan scratch dan mengurangi LP musuh sebanyak 100 poin.")
        LP_Musuh_Baru = LP_Musuh-100
        if LP_Musuh_Baru > 0:
            print("LP musuh yang tersisa sebanyak ",LP_Musuh_Baru," poin.")
    if Serangan == 2:
        print("Anda menggunakan throw dan mengurangi LP musuh sebanyak 300 poin.")
        LP_Musuh_Baru = LP_Musuh-300
        if LP_Musuh_Baru > 0:
            print("LP musuh yang tersisa sebanyak ",LP_Musuh_Baru," poin.")
    if Serangan == 3:
        print("Anda menggunakan flamethrower dan mengurangi LP musuh sebanyak 500 poin.")
        LP_Musuh_Baru = LP_Musuh-500
        if LP_Musuh_Baru > 0:
            print("LP musuh yang tersisa sebanyak ",LP_Musuh_Baru," poin.")
    if Serangan == 4:
        if LP_Musuh <= 500:
            print("Anda berhasil menangkap musuh Anda!")
            LP_Musuh_Baru = -13
        else: 
            print("Anda mencoba menangkap musuh Anda, namun gagal! ")
            LP_Musuh_Baru = LP_Musuh + 0
    if LP_Musuh_Baru > 0:
        print("Musuh Anda menggunakan slap dan mengurangi LP Anda sebanyak 200 poin.")
        LP_Anda_Baru = LP_Anda-200
        if LP_Anda_Baru > 0:
            print("LP Anda yang tersisa sebanyak ",LP_Anda_Baru," poin.")
    LP_Anda = LP_Anda_Baru
    LP_Musuh = LP_Musuh_Baru
    
if LP_Musuh <=0 and LP_Musuh != -13:
    print("Anda menang!")
if LP_Anda <=0:
    print("Anda kalah!")
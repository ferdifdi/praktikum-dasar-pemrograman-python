# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:54:58 2019

@author: ferdi.fadillah
"""

DDMMYYYY = input("Masukkan DD,MM,YYYY undian:")
DDMMYYYY_split = DDMMYYYY.split(",")

#N = dua digit terakhir pada tahun,
N = DDMMYYYY_split[2][2]+DDMMYYYY_split[2][3]
N_int = int(N)

dua_digit_awal_tahun = DDMMYYYY_split[2][0]+DDMMYYYY_split[2][1]

def Cibonacci(N_int):   
    #base case
    if N_int == 0: 
        return 0       
    elif N_int == 1:
        return int(DDMMYYYY_split[0]) #tanggal sbg suku pertama
    elif N_int == 2:
        return int(DDMMYYYY_split[1]) #bulan sbg suku kedua
    
    #recurcive case
    elif N_int > 2:
        return Cibonacci(N_int-1)+Cibonacci(N_int-2)    
 
print("Angka pemenang:",N,Cibonacci(N_int),dua_digit_awal_tahun) 

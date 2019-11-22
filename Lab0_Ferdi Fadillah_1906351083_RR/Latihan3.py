# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:20:30 2019

@author: ferdi.fadillah
"""

Permen_1 = input("Nama Permen 1: ")
Harga_Beli_1 = int(input("Harga Beli Permen 1 : "))
Persen_1 = int(input("Persentase Keuntungan Permen 1 (%) : "))
Permen_2 = input("Nama Permen 2: ")
Harga_Beli_2 = int(input("Harga Beli Permen 2 : "))
Persen_2 = int(input("Persentase Keuntungan Permen 2 (%) : "))

Permen_3 = input("Nama Permen 3: ")
Harga_Beli_3 = int(input("Harga Beli Permen 3 : "))
Persen_3 = int(input("Persentase Keuntungan Permen 3 (%) : "))

Barisan = '{:>5}|{:^20}|{:^15}|{:^15}'

print(Barisan.format('No','Nama Permen','Harga Beli','Harga Jual'))
print(Barisan.format('-'*5,'-'*20,'-'*15,'-'*15))
print(Barisan.format('1',Permen_1,Harga_Beli_1,Persen_1/100*Harga_Beli_1+Harga_Beli_1))
print(Barisan.format('2',Permen_2,Harga_Beli_2,Persen_2/100*Harga_Beli_2+Harga_Beli_2))
print(Barisan.format('3',Permen_3,Harga_Beli_3,Persen_3/100*Harga_Beli_3+Harga_Beli_3))





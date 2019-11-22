# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:12:13 2019

@author: USER
"""

input_my_file = input("Masukkan nama file: ")

#r1 = int(input("Masukkan r1: "))
#r2 = int(input("Masukkan r2: "))
#c1 = int(input("Masukkan c1: "))
#c2 = int(input("Masukkan c2: "))

my_file = open(input_my_file, "r")

my_file_1 = my_file.read().split("\n")
my_file_1.remove("")
print(my_file_1)
my_file_2 = my_file_1.read().split(" ")
my_file_2.remove("")
print(my_file_2)


#for baris in my_file_1:
#    for angka in baris:
#        print(baris[0], angka[0])


        
        
       

#my_file_1 = my_file.read().split("\n")
#my_file_1.remove("")
#print(my_file_1)
#   


my_file.close()

#maaf kak saya ga ngerti :(
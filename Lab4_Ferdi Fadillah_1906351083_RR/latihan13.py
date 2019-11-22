# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:48:48 2019

@author: ferdi.fadillah
"""

N = int(input("Masukkan lebar dasi (harus kelipatan 2 dan >= 4): "))

angka = 1  
for i in range (N//2-1):
    
    print("|", end="")
    print(" "*i, end="")
    for k in range (i):
        if angka > 9:
            angka = 0
        print(angka, end= "")
        angka +=1
        
    print("\\", end="")
    print(" "*(N-4-2*i), end="")
    for l in range (i):
        if angka > 9:
            angka = 0
        print(angka, end= "")
        angka +=1
        
    print("/", end="")
    print(" "*i, end="")
    for o in range (i):
        if angka > 9:
            angka = 0
        print(angka, end= "")
        angka +=1
    print("|", end="")
    print(" ")
    
             
for j in range (N//2-1):
    
    
    
    print("|", end="")
    print(" "*((N//2-1)-(j+1)*1), end="")
    for m in range (j):
        if angka > 9:
            angka = 0
        print(angka, end= "")
        angka +=1
       
    print("/", end="")
    print(" "*(2*j), end="")
    for m in range (j):
        if angka > 9:
            angka = 0
        print(angka, end= "")
        angka +=1
    print("\\", end="")
    print(" "*((N//2-1)-(j+1)*1), end="")
    for n in range (j):
        if angka > 9:
            angka = 0
        print(angka, end= "")
        angka +=1
    print("|", end="")
    print(" ")
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:59:37 2019

@author: ferdi.fadillah
"""

my_dict = dict()
value_list = []

i = 1 
while i != 0:
    i += 1
    user_input = input("Masukkan data:")  
     
    
    #jika pesan kosong, maka perulangan berhenti
    if user_input == "":
        i = 0            

    if user_input != "":
        key, value, TF = user_input.split(",")
    my_dict[key] = value 
    
    if value not in value_list:
        value_list.append(value)
 

    
    
print("Peserta:")

print("Jumlah:")
print(len(my_dict))



for i in range (len(value_list)):
    Jumlah = 0
    for key,value in my_dict.items():    
        if value == value_list[i]:        
            Jumlah= Jumlah+1
            
    print(value_list[i])
    print(Jumlah)
            
    for key,value in my_dict.items():
        if value == value_list[i]:
            print ("-",key)
        




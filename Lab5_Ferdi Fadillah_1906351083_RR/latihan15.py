# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:12:35 2019

@author: USER
"""



def isi_list(pengen_isi, baris, kolom):
    namron_punya_cnt = 0     
    for i in range(baris):
        if i % 2 == 0:
            for j in range(kolom):
                pengen_isi[i][j] = namron_punya_cnt
                namron_punya_cnt+=1
        else:
            for j in range(kolom -1,-1,-1):
                pengen_isi[i][j] = namron_punya_cnt
                namron_punya_cnt+=1
                
def cetak_list(pengen_cetak, baris, kolom):
    for i in range(5):
        for j in range(7):
            print(namron_punya_list[i][j], end=' ')
        print()
        
namron_punya_list = [[0]*7]*5
isi_list(namron_punya_list, 5, 7)
cetak_list(namron_punya_list, 5, 7)
 #maaf kak saya ga ngerti :(
 
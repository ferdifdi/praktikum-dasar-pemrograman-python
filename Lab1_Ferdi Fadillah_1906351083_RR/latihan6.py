# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:35:08 2019

@author: ferdi.fadillah
"""

import turtle
import math

#branding
turtle.penup()
turtle.setpos(0,200)
turtle.pendown()
turtle.write("Turtle Menggambar Bangun Datar", align="center")
turtle.penup()
turtle.setpos(-200,-200)
turtle.pendown()
turtle.write("Copyright Ferdi Fadillah")
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()

Bentuk = input("Masukkan bentuk yang ingin digambar ('lingkaran' atau 'segitiga'):")
Keliling = input("Masukkan panjang keliling gambar :")
int_Keliling = int(Keliling)
Warna_Garis = input("Masukkan warna gambar (red, green, yellow, orange, black, blue):")
Isi_Warna = input("Apakah Anda ingin mengisi warna ke dalam gambar? ('ya' atau 'tidak'):")

if Isi_Warna == 'ya':
    turtle.color(Warna_Garis, Warna_Garis)
elif Isi_Warna == 'tidak':
    turtle.color(Warna_Garis,"")
    
turtle.begin_fill()
if Bentuk == "lingkaran":
    turtle.circle(int_Keliling/(2*math.pi))  
    
elif Bentuk == "segitiga": 
    turtle.left(60)
    turtle.forward(int_Keliling/3)
    turtle.right(120)
    turtle.forward(int_Keliling/3)
    turtle.right(120)
    turtle.forward(int_Keliling/3)  

turtle.end_fill()   
turtle.hideturtle() 
turtle.mainloop()    
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:12:49 2019

@author: USER
"""
import turtle
import random 

#Inputan angka 20-60 dgn default 40
length = int(turtle.numinput("length", "Please enter the side length of the first square [20-60]:", 40, minval=20, maxval=60))

turtle.speed(10000) #kecepatan turtle bergerak

#Memosisikan turtle di sebelah kiri
turtle.penup()
turtle.setpos(-200,0)
turtle.pendown()

#turtle menggambar persegi berputar sebanyak 72
j = 0
while j < 72:
    j += 1
    
    #menentukan warna persegi secara acak
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    turtle.colormode(255)
    turtle.color("black", (R, G, B))
    
    turtle.begin_fill()
    turtle.left(180)  
    turtle.forward(length+j*2) #panjang persegi bertambah 2 secara berulang
    turtle.right(90)
    turtle.forward(length+j*2)
    turtle.right(90)
    turtle.forward(length+j*2)
    turtle.right(90)
    turtle.forward(length+j*2)
    turtle.left(85) #persegi berputar ke kanan 5 derajat dari persegi sebelumnya  
    turtle.end_fill()
 
#Memosisikan turtle di sebelah kanan
turtle.penup()
turtle.setpos(200,0)
turtle.pendown()

#turtle menggambar lingkaran berputar sebanyak 36
for i in range (0,36):
    
    #menentukan warna persegi secara acak
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    turtle.colormode(255)
    turtle.color("black", (R, G, B))
    
    turtle.begin_fill()
    
    #jari-jari lingkaran pertama adalah setengah dari panjang persegi terakhir
    #jari-jari lingkaran berkurang 2 secara berulang
    turtle.circle(((length+(71)*2)/2)-i*2)  
    
    turtle.left(10) #lingkaran berputar ke kiri 10 derajat dari persegi sebelumnya
    
    turtle.end_fill()
       
turtle.hideturtle() 
turtle.mainloop()  
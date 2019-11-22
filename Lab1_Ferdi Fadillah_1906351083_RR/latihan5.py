# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:18:19 2019

@author: ferdi.fadillah
"""

import turtle

Bentuk = input("Masukkan bentuk yang ingin digambar ('lingkaran' atau 'segitiga'):")
if Bentuk == "lingkaran":
    turtle.circle(50)   
if Bentuk == "segitiga":    
    turtle.left(60)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)  
 
turtle.mainloop()

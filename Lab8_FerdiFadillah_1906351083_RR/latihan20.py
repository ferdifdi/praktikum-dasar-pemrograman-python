# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:55:14 2019

@author: ferdi.fadillah
"""

def max_nested_tuple(nested_tuple):
    # Tambahkan kode Anda disini
    
    
if __name__ == '__main__':
    tup1 = (1,2,3,4)
    print(tup1, '->', max_nested_tuple(tup1))
    tup2 = (1,(2,5),(1,(((9)))))
    print(tup2, '->', max_nested_tuple(tup2))
    tup3 = ((), (((((()))))), ((), (()), ()))
    print(tup3, '->', max_nested_tuple(tup3))
    tup4 = ()
    print(tup4, '->', max_nested_tuple(tup4))
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:35:42 2020

@author: Trepat Jose v.
"""
#Eliminador de numeros repetidos

lst = [1, 2, 4, 4, 9, 7, 9, 9]
pos = 0
print(lst)

for i in (lst):
    if(lst.count(i) > 1):
        pos = lst.index(i)
        lst.remove(i)
print(lst)
        
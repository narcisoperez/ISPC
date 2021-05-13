# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:07:29 2020

@author: Trepat Jose v.
"""
#Hipotesis de Collatz

from random import randint

c0 = randint(1, 100)
vueltas = 0

while(c0 != 1):
    vueltas += 1
    if(c0 % 2 == 0):
        c0 = c0 / 2
    else:
        c0 = (c0 * 3) + 1
    print(int(c0))
print("La cantidad de vueltas fue de: ", int(vueltas))
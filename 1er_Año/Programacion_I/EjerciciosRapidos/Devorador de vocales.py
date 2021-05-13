# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:36:29 2020

@author: Trepat Jose v.
"""

userWord = input("Ingrese una palabra: ")
vocales = ['A', 'E', 'I', 'O', 'U']

userWord = userWord.upper()

for i in (userWord):
    if(i in vocales):
        continue
    print(i)

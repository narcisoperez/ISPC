# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:25:13 2020

@author: Trepat Jose v.
"""
#Matematico curioso sin listas
"""
from random import randint

numero = randint(20, 100)
mayor = numero
long = 1

while(numero != 1):
    
    long += 1
    
    if(numero % 2 == 0):    #Par
        numero = numero / 2
    else:                   
        numero = (numero * 3) + 1
        
    if(numero > mayor):
        mayor = numero
    print(int(numero), end=' ')
    
print("\nLongitud de la secuencia", long)
print("El numero mayor es: ", int(mayor))
"""
from random import randint

numero = randint(20, 100)

lst = []

while(numero != 1):
    
   if(numero % 2 == 0):    #Par
       numero /= 2
   else:                   
       numero = (numero * 3) + 1
   
   lst.append(numero)
    
print(int(max(lst)))

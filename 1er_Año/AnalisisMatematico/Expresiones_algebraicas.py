# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:23:39 2020

@author: Trepat Jose V.

Python version: 3.9
"""
#Librerias
import sympy as sp
from fractions import Fraction as Fr

#Creamos los simbolos x,y,z
x, y, z = sp.symbols('x,y,z')

#Actividad N°1: Sumas de polinomios
print("ACTIVIDAD N°1 --> SUMAS\n")

pol_1 = ((5*y**2)*z) + (4*x*y) + (-3*x*z)
pol_2 =((Fr(-1,8)*y**2)*z) + (Fr(1,2)*x*y) + (Fr(-3,5)*x*z)

a = pol_1 + pol_2
print("El resultado de la suma A es:", a)

pol_1 = (4*x**2) + (3*x) + (Fr(-1,5))
pol_2 = (Fr(3,4)*x**3) + (Fr(-1,4)*x**2) + (Fr(8,9)*x) + (Fr(3,7))

b = pol_1 + pol_2
print("El resultado de la suma B es:", b, "\n\n")

#Actividad N°2: Producto entre polinomios
print("ACTIVIDAD N°2 --> Producto\n")

#Se almacenan los polinominos en la variables con tipo polinomio(poly)
pol_1 = sp.poly(4*x*z + 2*x + 3*z)
pol_2 = sp.poly(Fr(1,2)*x + Fr(3,4)*z + 2)

a = pol_1 * pol_2
print("El resultado de la Multiplicacion A es:\n", a)

pol_1 = sp.poly(5*x**2 + 3*x + 2)
pol_2 = sp.poly(Fr(1,2)*x - 3)

b = pol_1 * pol_2
print("\nEl resultado de la MUNLTIPLICACION B es:\n", b )

pol_1 = sp.poly(x**2 - 1)
pol_2 = sp.poly(x**3 + 2)

c = pol_1 * pol_2
print("\nEl resultado de la MUNLTIPLICACION C es:\n", c )

pol_1 = sp.poly(x + 3)
pol_2 = sp.poly(2*x**2 - 5*x + 7)

d = pol_1 * pol_2
print("\nEl resultado de la MUNLTIPLICACION D es:\n", d )

#Crea el simbolo de i
i = sp.symbols('i')

pol_1 = sp.poly(x + 3*i)
pol_2 = sp.poly(Fr(2,3)*i + Fr(5,2)*x + 2)

e = pol_1 * pol_2
print("\nEl resultado de la MUNLTIPLICACION E es:\n", e )


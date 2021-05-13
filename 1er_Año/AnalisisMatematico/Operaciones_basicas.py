# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:02:49 2020

@author: Trepat Jose V.

Python version: 3.9
"""
#Conjuntos numericos
#Actividad N°1
print("ACTIVIDAD N°1:\n")

a = 3-(2+4-(5+1-(2+3-8))-3+9)
print("El resultado de A es:", a)

b = -10+(3-(2-15+9+(2-7)-6))+4
print("El resultado de B es:", b)

c = -(7-8+(15-12-(14+1-9)+5))
print("El resultado de C es:", c)

d = -15-(6+((-3+1-8)-(4-1))-7)+1
print("El resultado de D es:", d)

e = -8+(-7+5)+3-(2-(4-9)+3)-(-7)+9
print("El resultado de E es:", e, "\n\n")

#Actividad N°2: Fracciones
#Importar la funcion fraccion y la renombramos Fr
from fractions import Fraction as Fr

print("ACTIVIDAD N°2:\n")

a = Fr(3, 4) - (Fr(1, 2)+Fr(2, 3))
print("El resultado de A es:", a)

b = (Fr(7, 3)-4) - (Fr(2, 5) - Fr(1, 2))
print("El resultado de B es:",b) 

c = (Fr(1, 2) * Fr(3, 4)) + Fr(4, 3)
print("El resultado de C es:", c)

d = ((Fr(3, 4)-2) / (Fr(4, 3) - Fr(1, 2))) * (Fr(3, 5) + Fr(2, 3))
print("El resultado de D es:", d)

e = ((Fr(1, 2) + Fr(2, 3)) / Fr(1, 2)) - (Fr(7, 15) / Fr(1, 5))
print("El resultado de E es:", e, "\n\n")

#Actividad N°3: Potencia
print("ACTIVIDAD N°3:\n")
b = (Fr(1, 4) ** Fr(3, 2))
b = Fr(b)
print("El resultado de B es:", b)

c = (-Fr(8, 27) ** Fr(4, 3))
c = Fr(c)
print("El resultado de C es: ", round(c, 2), "\n\n")

#Actividades de ejercitacion
print("ACTIVIDADES DE EJERCITACION\n")
a = 3 - Fr(1, 3) - Fr(3, 4) + Fr(5, 6)
print("El resultado de A es:", a)

b = -4 + ((Fr(1, 3)-Fr(2, 5)) / Fr(3, 2)) + Fr(4, 3)
print("El resultado de B es:", b)

c = 2 - (Fr(5, 3) + (4 / (2 + Fr(1, 3))) + 3)
print("El resultado de C es:", c)

d = (4-3)**2 + (5 / (1 - Fr(2, 3)))**2 + Fr(4, 3)
print("El resultado de D es:", d)

#Importar la libreria math
import math

e = math.sqrt((1 / (2 + Fr(3, 11))) + Fr(1, 5))
e = Fr(e)
print("El resultado de E es:", round(e, 2))

f = 4 * (Fr(-1, 3)**2) + (Fr(2, 5) - Fr(1, 4))
print("El resultado de F es:", f)

g = Fr(2, 3) / Fr(-1, 3) + (Fr(3, 4) * Fr(-2, 9))
print("El resultado de G es:", g)

h = -1 - (Fr(-1, 2) + Fr(3,4) + (-2 + Fr(5, 6) - (Fr(1,3) - 1))- Fr(1, 6)) - Fr(1, 3)
print("El resultado de H es:", h)

i = (Fr(1, 3) * (1 + (3 / Fr(-1, 4)))) / (2 * (Fr(1, 2) + (3 / (Fr(3, 4) - Fr(1, 2))))) - Fr(1, 3)
print("El resultado de I es:", i)

j = ((math.sqrt(Fr(3, 5)) * Fr(1, 6)) ** 2) / Fr(-5, 4)
print("El resultado de J es:", round(j, 3)) #-0.013 = -1/75

#Subvariaables del ejercicio K
k1 = (((1 + Fr(1, 3)) / (Fr(1, 4) * Fr(1, 5)) ) * ((Fr(2, 3) + Fr(-1, 5)) / (2 + Fr(1, 3))))
k2 = (1 / (5 + Fr(1, 9)))
k3 = ((math.sqrt(1 + Fr(-3, 4))) / (9 + Fr(1, 5)))

k = k1 - k2 / k3
k = Fr(k)
print("El resultado de K es:", round(k, 1)) #17/10 = 26/15

l = ((((Fr(15, 4) - Fr(1, 5)) / Fr(1, 20)) / (Fr(71, 3))) * 100 +43)**Fr(1, 3) #Raiz cubica
print("El resultado de L es:", round(l))

#Subvariables del ejercicio m
m1 = 1 - (1 / (2 - Fr(1, 2)))
m2 = 1 + (Fr(1, 2) / (1 - Fr(2, 3)))

m = (m1 / m2)**-2
print("El resultado de M es:", m)

#Subvariables del ejercicio n
n1 = (4 * Fr(5, 4)) - Fr(1, 5)
n2 = (4 * Fr(11, 10)) + (math.sqrt(Fr(4, 25)))

n = n1 / n2
print("El resultado de N es:", round(n))

#Subvariables del ejercicio o
o1 = Fr(1, 2) * ((1 - Fr(3, 2)) / (2 - Fr(13, 9)))
o2 = math.sqrt(Fr(16, 5) / 5) / (5 ** -2)

o = o1 + (Fr(1, 5) / o2)
print("El resultado de O es:", o)   #-0.44 = -11/25

#Subvaribles del ejercicio p
p1 = (Fr(3, 4) - 1 + Fr(1, 8))**Fr(1, 3)
p2 = (Fr(5, 3) - Fr(1, 6)) / p1
p3 = 10 / ((Fr(3, 2)**-2) + Fr(2, 3))

p = (p2 * p3)**Fr(1, 3)
print("El resultado de P es:", round(p.real))   #Eliminar la parte imaginaria

#Subvaribles del ejercicio q
q1 = ((Fr(1, 2) + Fr(3, 4)) / (Fr(1, 4) - Fr(3, 2)))
q2 = (Fr(7, 2) / Fr(7, 4))

q = q1 - q2
print("El resultado de Q es:", q)

#Subvariables del ejercicio r
r1 = (Fr(3, 5)**2)**3

r = r1 / ((Fr(3, 5))**4)
print("El resultado de R es:", r)

#Subvariables del ejercicio s
s1 = ((Fr(1, 2) + Fr(1, 3))**2) * Fr(5, 6)

s = s1 ** Fr(1, 3)
print("El resultado de S es:", round(s, 2)) #0.83 = 5/6

t = math.sqrt((Fr(2, 3) - 1) * (1 - Fr(2, 3)) * (-1))
t = round(t, 2)
print("El resultado de T es:", t)   #0.33 = 1/3

u = (Fr(5, 3)**-7) / (Fr(5, 3)**-5)
print("El resultado de U es:", u)

#Subvariables del ejercicio v
v1 = Fr(12, 5) / Fr(3, 5)
v2 = Fr(3, 7) * Fr(1, 6)

v = v1 - v2 - Fr(50, 7) + Fr(3, 14)
print("El resultado de V es:", v)

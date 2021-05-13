# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:23:57 2020

@author: Trepat Jose V.

Python version: 3.9
"""
#Ejercicios de Asignacion
#Ejecicio 2.1

C = int(input("Ingrese el capital inicial en pesos: "))
x = float(input("Ingrese la tasa de interes: "))
n = int(input("Ingrese la cantidad de años que desea mantener la inversion: "))

Cn = C * (1 + x / 100)**n
print("El retorno sera de: ", Cn, "pesos, tras", n, "año/s")

#Ejercicio 2.2

grados_f = float(input("Ingrese la temperatura en Farenhaeit: "))

celsius = (grados_f - 32) / 1.8
print(grados_f, "°F son -->", round(celsius, 2), "°C")

#Ejercicio 2.3

user_name = input("Ingrese su nombre: ")

print(user_name.upper())    #.upper() Cambia a mayusculas todos los elementos del str
print("La cantidad de letras es de:", len(user_name))   #len() cuenta la cantidad de elementos

#Ejercicios de Condicionales simples
#Ejercicio 2.4

user_age = int(input("Ingrese su edad: "))

if (user_age >= 18):
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

#Ejercicio 2.5

user_age = int(input("Ingrese su edad: "))
user_income = int(input("Ingrese el monto de sus ingresos mensuales: "))

if (user_age >= 16 and user_income > 1000):
    print("Usted debe pagar impuestos")
else:
    print("No debe pagar impuestos")

#Ejercicio 2.6

user_sex = input("Ingrese su sexo: ")
user_name = input("Ingrese su nombre: ")

abcedario = "abcdefghijklmnopqrstuvwxyz" 

inicial = user_name[0] #Almacena la inicial del nombre
ubicacion = abcedario.index(inicial) #regresa la ubicacion de la inicial

if (user_sex == "hombre" and ubicacion <= 12):
    print("Perteneces al grupo A")
elif (user_sex == "hombre" and ubicacion > 12):
    print("Perteneces al grupo B")
elif (user_sex == "mujer" and ubicacion <= 11):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

#Ejercicios con Bucles repetitivos
#Ejercicio 2.7

bucle_inicio = int(input("Ingrese el primer numero: "))
bucle_final = int(input("Ingrese el numero final: "))

for x in range(bucle_inicio, bucle_final):
    if(x % 2):
        continue
    print(x, end=" ")

#Ejercicio 2.8

bucle_inicio = int(input("Ingrese un numero para la cuenta regresiva: "))
x = 0
for x in range(bucle_inicio, -1, x-1):
    print(x, end=",")

#Ejercicio 2.9

bucle_final = int(input("Ingrese un numero final para la cuenta: "))
x = 0
for x in range(0, bucle_final + 1):
    if(x % 2):
        print(x, end=",")

#Ejercicio 2.10.1

for x in range(10, 21):
    print(x)

#Ejercicio 2.10.2

best_friends = ["pato","rodrigo","loza","martin","juan"]
for x in range(0, 5):
    print("Hola", best_friends[x])

#Ejercicio 2.10.3

best_friends = []

for x in range(0, 5):
    friend_name = input("Ingrese el nombre un amigo: ")
    best_friends.append(friend_name)
    
for x in range(0, 5):
    print("Hola", best_friends[x])

#ejercicio 2.10.4

best_friends = []
posicion = 1

for x in range(0, 5):
    print("Ingrese el nombre de su", posicion, "° amigo: ")
    friend_name = input()
    best_friends.append(friend_name)
    posicion += 1
    
for x in range(0, 5):
    print("Hola", best_friends[x])

#Ejercicio 2.10.5

amount_friends = int(input("Ingrese la cantidad de amigos que desea saludar: "))

best_friends = []
posicion = 1

for x in range(0, amount_friends):
    print("Ingrese el nombre de su", posicion, "° amigo: ")
    friend_name = input()
    best_friends.append(friend_name)
    posicion += 1
    
for x in range(0, amount_friends):
    print("Hola", best_friends[x])

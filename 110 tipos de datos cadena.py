# -*- coding: utf-8 -*-
"""
cadenas
"""
# Presentar el tipo de dato de cadena

myString = "This is a string."

print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# Trabajar con concatenación de cadenas

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString

print(thirdString)

# Trabajar con cadenas de entrada.

name = input("¿Como te llamas? ")

print(name)

# Dar formato a las cadenas de salida.

animal = input("¿Cual es tu animal favorito?  ")
color = input("¿Cual nes tu color favorito?  ")

print("{}, Te gusta un {} {}!".format(name,animal,color))
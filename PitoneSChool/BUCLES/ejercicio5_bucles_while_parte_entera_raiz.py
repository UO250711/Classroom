#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
'''
Ejercicio 5.- Dado un número natural n, escribe un programa para calcular la parte entera de la raíz
cuadrada de n y muestre en resultado en la forma:
La parte entera de la raíz cuadrada de 38 es: 6
'''
n=int(raw_input("Dame el numero"))
p=n

while(math.pow(n,2)>n):
    print "p*p" , p
    p=p-1

print "La parte entera de la raiz cuadrada de",n,"es:",p
#!/usr/bin/env python
# -*- coding: utf-8 -*-



'''
Ejercicio 13.- 6. Dado un número natural n, escribe un programa para generar (escribir en pantalla) la
secuencia de los n primeros números de Perrin. Los tres primeros números de esta secuencia son P(0)=3,
P(1)=0 y P(2)=2 y el resto se obtienen en la forma: P(n) = P(n-2) + P(n-3) si n>2.
Números de Perrin: 3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29

'''
numero=abs(int(raw_input("a: ")))


for i in range(2,numero):
    if  numero%i!=0 and i>2:
         print  i-2
         print  i-3




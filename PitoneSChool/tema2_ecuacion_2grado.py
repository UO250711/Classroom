#!/usr/bin/python
# -*- coding: latin-1 -*-

# Ejercicio 4 - Ecuacion de segundo grado
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))
print "ecuacion  ",a,"*x^2 + ",b,"*x + ", c, " = 0"
#calculando raices
raiz = float(b**2-(4*a*c))
if raiz < 0:
    print raiz
    print('La ecuacion no tiene solucion')

elif raiz == 0:
    s = float(-b/2*a)
    print ('Una solucion: ',s)

else:
    x1 = float((-b+((b**2 - 4*a*c))**0.5)/(2*a))
    x2 = float((-b-((b**2 - 4*a*c))**0.5)/(2*a))
    print('Dos soluciones: ')
    print('X1: ',x1)
    print('X2: ',x2)

'''
a=float(raw_input("Introduce coeficiente a"))
b=float(raw_input("Introduce coeficiente b"))
c=float(raw_input("Introduce coeficiente c"))

radicando=((b**2)-(4*a*c))

solucion_real=radicando>=0
solucion_unica=radicando==0

if solucion_real:
    if solucion_unica:
        print "La ecuacion tiene una solucion real doble"

    else:
        print "La ecuacion tiene dos soluciones reales"

else:
    print "Dos soluciones complejas conjugadas"
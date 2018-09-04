#! /usr/bin/python
# -*- coding: utf8 -*-

a,b= input ("digite la parte real de su numero y luego la imaginaria, separadas por coma (,)  ")

c= complex (a,b)
d=(((a**2)+(b**2))**(0.5))**2

print ("su numero complejo es: "),c 
print ("El cuadrado del módulo es: "),d

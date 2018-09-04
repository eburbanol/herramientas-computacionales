#! /usr/bin/python
# -*- coding: utf8 -*-

import math

a,b,c= input("Teclee 3 numeros separados por comas (,)")
print a,b,c
w=raw_input("Teclees una palabra con mas de 5 letras")

print w
print w[2:5] #Excluye la celda 0 a 1 e immprime de la 2 a la 5
print w[3]   #Imprime la posicion de la celda 3
print w[4:1:-1] #Imprime de la celda 4 a la celda 1 en ese orden
print w[::-1] #Imprime w alrevés
print w[::2] #Imprime hasta la celda 2.



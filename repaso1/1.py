#! /usr/bin/python
# -*- coding: utf8 -*-

import math

a=9

print "{:1d}".format(a)
print "{:01d}".format(a)
print "{:2d}".format(a)
print "{:02d}".format(a)  #rellena con 0 antes de a
print "{:04d}".format(a)  #Rellena con 0 antes de a
print "{:5d}".format(a)
print "{:05d}".format(a)

print "{:5.3f}".format(math.pi) #(3f) muestra tres cifras decimales luego dle punto
print "{:6.3f}".format(math.pi) #(:6) Usa 6 caracteres para mostrar el resultado. 
print "{:08.3f}".format(math.pi) #(:8)Usa 8 caracteres para mostrar el resultado, rellenando con 0's las casillas faltantes a la izq.

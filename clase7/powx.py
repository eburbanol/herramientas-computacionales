#!/usr/bin/python
# -*- coding: utf8 -*-

x= input ("ingrese la base ")
y= input ("Ingrese el exponente ")

def powx (x,y):
	if x==1 or y==0:
		return 1
	return x*powx(x,y-1)
	
print powx(x,y)

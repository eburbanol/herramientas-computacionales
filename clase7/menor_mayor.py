#!/usr/bin/python
# -*- coding: utf8 -*-

def menor_mayor(x,y):
	if x>y:
		mayor,menor=x,y
	else:
		mayor,menor=y,x
	return menor, mayor

a,b=menor_mayor(6,3)
print a,b

#! /usr/bin/python
# -*- coding: utf8 -*-



def factorial(x):
	a=1
	b=2
	
	while a<=x:
		a=a*b
		b=b+1
	return a
	
print factorial(5)


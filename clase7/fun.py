#! /usr/bin/python
# -*- coding: utf8 -*-

a=10
b=0

def f(x,y):
	a=x+y
	global b
	b=10
	return a
print f(3,4)
print a
print b

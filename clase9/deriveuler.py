#! /usr/bin/python
# -*- coding:  utf8 -*-
"""
DX=

xo = linspace(0,1,001)
function1=xo+DX/2
function2=xo-DX/2

dif_central=(function1-function2)/DX

"""
import pylab as pl
from math import exp

def der_adel(f,x,dx=0.01):
	return (f(x+dx)-f(x))/dx

dx= 1e-1
da=[]
dxl=[]
f=exp
x=1

while dx>1e-10:
	dxl.append(dx)
	da.append((f(x)-der_adel(f,x,dx))/f(x))
	dx=dx*0.05
pl.plot(dxl,da)
pl.show()
raw_input()
	

		

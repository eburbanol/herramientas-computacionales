#! /usr/bin/pyhton
#  -*- coding: utf8 -*-

class Complex:
	def __init__(self, re, im=0):
		self.re=re
		self.im=im
		
	def suma(self, other):
		return Complex(self.re + other.re, self.im + other.im)
	
	def multip(self,other):
		return Complex(self.re*other.re - self.im*other.im, self.im*other.re + other.im+self.re )
	
	def divi(self, other):
		return Complex((self.re*other.re+self.im*other.im)/(other.re**2+other.im**2),(self.im*other.re-self.re*other.im)/(other.re**2+other.im**2))
	
	def imp(self):
		return "{:f}{:f}i".format(self.re, self.im)

if __name__=="__main__":
	q=Complex(1.,5.)
	w=Complex(3.,4.)
	h=Complex(4.)
	
	a=q.suma(w)
	b=q.multip(h)
	c=w.divi(h)
	
	print a.imp()
	print b.imp()
	print c.imp()

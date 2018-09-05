#!/usr/bin/python
#-*- coding: utf8 -*-

a=[1, 4, 6, 8, 9, 11, -3, -4, 6, 10]
for i in range(len(a)):
	for j in range(i+1,len(a)):
		if a[i]>a[j]: 
			a[i],a[j]=a[j],a[i]
print a

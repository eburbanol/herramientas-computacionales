#!/usr/bin/python
# -*- coding: utf8 -*-

def sumatoria(x):
	if x==1:
		return 1
	return x+sumatoria(x-1)
print sumatoria(100)

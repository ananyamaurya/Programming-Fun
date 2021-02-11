# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:30:53 2020

@author: anany
"""

def sqr(num):
    return num * num

def cube(num):
    return num ** 3

def solve(fun,num):
    return(fun(num))


a,b = 4,5

print(solve(sqr,a))


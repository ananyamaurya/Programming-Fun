# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:28:19 2020

@author: anany
"""

import sys

def hello():
    '''
    This function prints HELLO WORLD
    '''
    print("Hello World")
    

hello()
print(type(hello))
copy_hello = hello
ret = copy_hello()
print(ret, 'type=', type(ret))

str1 = 'hello'
print(type(str1))

myVal = 1
print(type(myVal))
print(id(myVal))

myVal = 2
print(type(myVal))
print(id(myVal))

val = 1
print(id(val))

imax = 18988988989798798898989451458421254812
print(sys.getsizeof(imax))


print(__doc__)

print(hello.__doc__)

octal_int = oct(8)
print(octal_int)
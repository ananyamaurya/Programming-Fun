# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:47:15 2020

@author: anany
"""

string = str(input())
caps,small,number,sp_char = 0,0,0,0
for i in string:
    if i.isdigit():
        number += 1
    elif i.isupper():
        caps += 1
    elif i.islower():
        small += 1
    else:
        sp_char += 1
print(string, " has ",caps," Capital ",small," Lower ",number," Numeric and ",sp_char," Special characters")
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 19:28:50 2020

@author: anany
"""

_alpha = 'a'
alpha = 'A'

alphabets_dict = {}

for i in range(26):
    x = ord(_alpha) + i
    alphabets_dict[chr(x)] = x
for i in range(26):
    x = ord(alpha) + i
    alphabets_dict[chr(x)] = x

print(*[[x, y] for x, y in alphabets_dict.items()], sep='\n')

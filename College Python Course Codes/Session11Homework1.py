# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 19:32:50 2020
@author: anany

"""
_alpha = 'a'
alpha = 'A'

hw1Dict = {'small': {'small1': {chr(ord(_alpha) + i): chr(ord(_alpha) + i) + '12' for i in range(26)}},
           'caps': {'caps1': {chr(ord(alpha) + i): chr(ord(alpha) + i) + '12' for i in range(26)}},
           'nums': {'nums1': {str(i): str(i) + '12' for i in range(10)}}}
print(*hw1Dict.items(), sep='\n')

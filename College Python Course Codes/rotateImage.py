# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:10:23 2020

@author: anany
"""

n = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
x = len(n)
if x%2 == 0:
    l = x-1
    for i in range(x//2):
        for j in range(i,l-i):
            t = n[i][j]
            n[i][j] = n[l-j][i]
            n[l-j][i] = n[l-i][l-j]
            n[l-i][l-j] = n[j][l-i]
            n[j][l-i] = t
print(n)
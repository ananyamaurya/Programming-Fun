# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:51:50 2020

@author: anany
"""

m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
li=[]
x = len(m)
y = len(m[0])
for ls in m:
    if 0 in ls:
        l = [i for i in range(len(ls)) if ls[i] == 0]
        
        li.append(l)
    else:
        li.append([","])
       
for i in range(x):
    if "," in li[i]:
        pass
    else:
        for k in li[i]:
            m[i] = [0 for w in range(y)]
            for j in range(x):
                m[j][k] = 0
                
print(m)
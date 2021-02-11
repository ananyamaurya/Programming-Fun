# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:02:59 2020

Question: 3sums problem

@author: anany
"""
from collections import Counter

nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

list_3sums = []
dict_nums = Counter(sorted(nums))
for key, value in dict_nums.items():
    if key == 0: 
        if value >= 3:
            list_3sums.append([0,0,0])
    else:
        if value >= 2:           
            x = 2*key
            x = -x
            if(x in dict_nums.keys()):
                if(sorted([key,key,x]) in list_3sums):
                    pass
                else:
                    list_3sums.append(sorted([key,key,x]))
        if((-key in dict_nums.keys()) and (0 in dict_nums.keys())):
            if(sorted([key,-key,0]) in list_3sums):
                pass
            else:
                list_3sums.append(sorted([key,-key,0]))  
        for s_keys in dict_nums.keys():
            x = 0-(s_keys+key)
            if s_keys != key and x!= key and x!= s_keys:
                    
                print(s_keys,key,x)
                    
                if (x in dict_nums.keys()):
                    if(sorted([key,s_keys,x]) in list_3sums):
                        pass
                    else:
                        list_3sums.append(sorted([key,s_keys,x]))
        
                    
print(list_3sums)
    
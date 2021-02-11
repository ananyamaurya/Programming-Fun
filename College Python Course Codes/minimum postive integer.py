# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:44:47 2020

@author: anany
"""
nums = [3,4,-1,1]
m = max(nums)
if m<1:
    print( 1)
if len(nums) == 1:
    print( 2) if nums[0] == 1 else print(1)
nums = sorted(nums)
for i in range(len(nums)-1):
    print(i, nums[i])
    if(nums[i]<0):
        pass
    else:
        if(nums[i]+1 == nums[i+1]) or (nums[i] == nums[i+1]):
            pass
        else:
            print( nums[i]+1)
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:28:50 2020

@author: anany
"""
import sys

#function to produce fibonacci series
def fibo(n):
    """
    Function generates the fibonacci series of provided length 'n'

    Parameters
    ----------
    n : Integer
        Represents the length of required series.

    Returns
    -------
    li : list
        List of Fibonacci elements.

    """
    li =[0,1]
    for i in range(n-2):
        x = li[i] + li[i+1]
        li.append(x)
    return li

     
try:
    print(fibo(int(input())))
except ValueError:
    print("Enter number only :") 

def fibonacci(count): 
    fib_list = [0, 1] 
  
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), 
                                         range(2, count))) 
  
    return fib_list[:count] 

print("Python Version",sys.version)

  

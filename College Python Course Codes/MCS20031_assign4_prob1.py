"""
Created on Fri Dec  18 15:02:39 2020

@author: anany

Objective:
    Write a recursive function which goes through an empty matrix passed to it which
    has many levels of inner matrices with varying depths, all of them being empty
    and fill them with a custom pattern provided as string while splitting it to a custom size.

"""

from sympy import isprime

l_prime =[]
l_odd = []
l_even = []
while True:
    x = input("Enter an integer or q or Q to quit :: ")
    try:
        x = int(x)
        if isprime(x):
            l_prime.append(x)
        elif x % 2 == 0:
            l_even.append(x)
        else:
            l_odd.append(x)
    except ValueError:
        if str(x) == 'q' or str(x) == 'Q':
            break
        else:
            print("Invalid Input !!!!!!!!")
print("Prime Numbers :: ", l_prime)
print("Even Numbers :: ", l_even)
print("Odd Numbers :: ", l_odd)

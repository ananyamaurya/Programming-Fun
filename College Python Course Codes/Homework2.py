# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 02:49:39 2020

@author: anany

Objective:
    Generate fillMyMatrix function that accepts a list and for every element which is an empty list
    populate it with 2 consecutive natural number and follow along with the sequence

"""

# global fillCount Variable to keep track of increments


matrix1 = [[[], []],
           [[]],
           [[], [], []],
           []]

matrix2 = [[[], []],
           [[]],
           [[], [], []],
           [[]],
           [[], [], []],
           []]


def checkAndFill(li, s, k):
    fillCount = 0
    x = len(s)
    k = int(k)

    def fill(l):
        nonlocal fillCount, x, k
        if not l:
            if (fillCount+k) < x:
                l.append(s[fillCount: fillCount+k])
                fillCount += k
            elif (fillCount+k) == x:
                m = s[fillCount:]
                l.append(m)
                fillCount = 0
            else:
                y = (fillCount + k) % x
                m = s[fillCount:] + s[:y]
                l.append(m)
                fillCount = y
            return l
        for i in l:
            i = fill(i)
        return l
    fill(li)
    return li


# operating on Matrix 1
print("Matrix 1 before filling :::::\n")
print('\n'.join(str(i) for i in matrix1))

matrix1 = checkAndFill(matrix1, 'mauryi', 4)
print("\n\nMatrix 1 after filling :::::\n")
print('\n'.join(str(i) for i in matrix1))
'''
# operating on Matrix 2
print("\n\n\nMatrix 2 before filling :::::\n")
print('\n'.join(str(i) for i in matrix2))

matrix2 = fillMyMatrix(matrix2)
print("\n\nMatrix 2 after filling :::::\n")
print('\n'.join(str(i) for i in matrix2))
'''
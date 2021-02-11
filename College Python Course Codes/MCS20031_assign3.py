# -*- coding: utf-8 -*-
"""
Created on Fri Dec  18 14:49:39 2020

@author: anany

Objective:
    Write a recursive function which goes through an empty matrix passed to it which
    has many levels of inner matrices with varying depths, all of them being empty
    and fill them with a custom pattern provided as string while splitting it to a custom size.

"""
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
matrix3 = [[[], []], [[]], [[], [], []], [[]], [[], [], []], []]


def checkAndFill(li, s, p_len):
    fillCount = 0
    s_len = len(s)
    p_len = int(p_len)
    strVal = [i for i in s]

    # fills the matrix if length of pattern is greater than split
    def fill_s(l):
        nonlocal fillCount, s_len, p_len
        if not l:
            if (fillCount + p_len) < s_len:
                for m in strVal[fillCount: fillCount + p_len]:
                    l.append(m)
                fillCount += p_len
            elif (fillCount + p_len) == s_len:
                for m in strVal[fillCount:]:
                    l.append(m)
                fillCount = 0
            else:
                y = (fillCount + p_len) % s_len
                for m in strVal[fillCount:] + strVal[:y]:
                    l.append(m)
                fillCount = y
            return l
        for i in l:
            fill_s(i)
        return l

    # fills the matrix if split is greater than length of pattern
    def fill_p(l):
        nonlocal fillCount, s_len, p_len
        if not l:
            if fillCount != p_len:
                for m in s[p_len - fillCount:]:
                    l.append(m)
                fillCount = p_len - len(l)
            while fillCount >= s_len:
                for m in strVal:
                    l.append(m)
                fillCount -= s_len
            if fillCount != 0:
                for m in strVal[:fillCount]:
                    l.append(m)
                fillCount = p_len - fillCount
            else:
                fillCount = p_len
            return l
        for i in l:
            fill_p(i)
        return l

    # calls fill_p if split is greater than length of pattern
    # calls fill_s if split is equals to or smaller than length of pattern
    if s_len >= p_len:
        fill_s(li)
    else:
        fillCount = p_len
        fill_p(li)
    return li


# operating on Matrix 1
pattern = 'abcdefghijk'
pat_len = 3

print("\nMatrix 1 before filling :::::\n")
print('\n'.join(str(i) for i in matrix1))

matrix1 = checkAndFill(matrix1, pattern, pat_len)

print("\n\nMatrix 1 after filling :::::\n")
print('\n'.join(str(i) for i in matrix1))

# operating on Matrix 2
print("\nMatrix 2 before filling :::::\n")
print('\n'.join(str(i) for i in matrix2))

matrix1 = checkAndFill(matrix2, pattern, pat_len)

print("\n\nMatrix 2 after filling :::::\n")
print('\n'.join(str(i) for i in matrix2))

# In case if split is greater than pattern.
pattern = 'any'
pat_len = 5
print(f"\nFor pattern :: {pattern} and split size :: {pat_len}")
print("\nMatrix 3 before filling :::::\n")
print('\n'.join(str(i) for i in matrix3))

matrix1 = checkAndFill(matrix3, pattern, pat_len)

print("\n\nMatrix 3 after filling :::::\n")
print('\n'.join(str(i) for i in matrix3))

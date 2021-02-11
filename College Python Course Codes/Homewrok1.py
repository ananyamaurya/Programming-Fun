# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 02:17:41 2020

@author: anany

Objective:
    Generate callfnfromList function that accepts a list and traverse through every element in the list
    If an elements is found to be a function call the function and pass the previous elemnt as parameter

"""


def foo(num):
    print("foo is called with num =", num)


myList = [foo, 11, 12, foo, 14, 15, foo, 17, foo]


def callFnFromList(mList):
    for i in range(len(mList)):
        
        # callable checks whether the object is callable (is a function or not) and returns TRUE if its a function
        if callable(mList[i]):
            
            # to ensure no invalid index is executed
            try:
                mList[i](mList[i - 1])
            except IndexError:
                mList[i](-1)


# calling callfnfromList
callFnFromList(myList)

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:48:09 2020

@author: anany
"""


def outerChkMyMatrix(myMatrix):
    fillCount: int = 97
    li = []

    # inner function
    def checkMatrix(matrix):
        # since fillCount and li are not defined in scope of checkMatrix and not defined globally
        # pointing them as non-local will tell the function to look outside its scope for values
        nonlocal fillCount, li
        for i in range(len(matrix)):
            # since a null matrix is considered as false value if its empty it will give false and not of false equates to true
            # used to check for cases where the list is empty
            if not matrix[i]:
                li.append([])
                continue
            # to check whether ith element of list is a list or  not
            if not isinstance(matrix[i], list):
                if len(matrix) == 3:
                    # to check for boundary cases
                    if 105 < fillCount < 108:
                        if fillCount == 105:
                            # ord(character) returns its ascii value
                            if (ord(matrix[0]) == fillCount) and (
                                    (ord(matrix[1]) == fillCount + 1) and (ord(matrix[2]) == fillCount + 2)):
                                fillCount = 97
                                return
                            else:
                                li.append(matrix)
                                fillCount = 97
                                return
                        elif fillCount == 106:
                            if (ord(matrix[0]) == 106) and ((ord(matrix[1]) == 107) and (ord(matrix[2]) == 97)):
                                fillCount = 98
                                return
                            else:
                                li.append(matrix)
                                fillCount = 98
                                return
                        elif fillCount == 107:
                            if (ord(matrix[0]) == 107) and ((ord(matrix[1]) == 97) and (ord(matrix[2]) == 98)):
                                fillCount = 99
                                return
                            else:
                                li.append(matrix)
                                fillCount = 99
                                return
                    # if not boundary values
                    elif (ord(matrix[0]) == fillCount) and (
                            (ord(matrix[1]) == fillCount + 1) and (ord(matrix[2]) == fillCount + 2)):
                        fillCount += 3
                        return
                    else:
                        li.append(matrix)
                        fillCount += 3
                        return
                else:

                    li.append(matrix)
                    fillCount += len(matrix)
                    return
            else:
                checkMatrix(matrix[i])

    checkMatrix(myMatrix)
    if li:
        return False, li
    else:
        return True, myMatrix


myMatrix0 = ['a', 'b', 'c']

result, myMat = outerChkMyMatrix(myMatrix0)
print('\nThe result of checking the matrix0:', result)
print('The returned matrix is: ', myMat)

myMatrix1 = ['a', 'b']

result, myMat = outerChkMyMatrix(myMatrix1)
print('\nThe result of checking the matrix1:', result)
print('The returned matrix is: ', myMat)

myMatrix2 = [['a', 'b', 'c']]

result, myMat = outerChkMyMatrix(myMatrix2)
print('\nThe result of checking the matrix2:', result)
print('The returned matrix is: ', myMat)

myMatrix3 = [['a', 'b', 'c'], ['d', 'e', 'f']]

result, myMat = outerChkMyMatrix(myMatrix3)
print('\nThe result of checking the matrix3:', result)
print('The returned matrix is: ', myMat)

myMatrix4 = [[[['a', 'b', 'c']]], ['d', 'e', 'f']]

result, myMat = outerChkMyMatrix(myMatrix4)
print('\nThe result of checking the matrix4:', result)
print('The returned matrix is: ', myMat)

myMatrix5 = [[[['a', 'b', 'c']]],
             [[['d', 'e', 'f']]],
             ['g', 'h', 'i'], ['j', 'k', 'z']]

result, myMat = outerChkMyMatrix(myMatrix5)
print('\nThe result of checking the matrix5:', result)
print('The returned matrix is: ', myMat)

myMatrix6 = [[[['a', 'b', 'c']]],
             [[['d', 'z', 'f']]],
             ['g', 'h', 'i'], ['j', 'k', 'a']]

result, myMat = outerChkMyMatrix(myMatrix6)
print('\nThe result of checking the matrix6:', result)
print('The returned matrix is: ', myMat)

myMatrix7 = [[[['a', 'b', 'c']]],
             [[['d', 'e', 'f']]],
             ['g', 'z', 'i'], ['j', 'k', 'a']]

result, myMat = outerChkMyMatrix(myMatrix7)
print('\nThe result of checking the matrix7:', result)
print('The returned matrix is: ', myMat)

myMatrix8 = [[[['a', 'b', 'c']]],
             [[['d', 'e', 'f']], ['g', 'h', 'i']],
             ['j', 'k', 'a'], ['b', 'c', 'd']]

result, myMat = outerChkMyMatrix(myMatrix8)
print('\nThe result of checking the matrix8:', result)
print('The returned matrix is: ', myMat)

myMatrix9 = [[[['a', 'b', 'c']]],
             [[['d', 'e', 'f']], ['g', 'h', 'i']],
             ['j', 'k', 'a'], ['b', 'c', 'd'],
             []]

result, myMat = outerChkMyMatrix(myMatrix9)
print('\nThe result of checking the matrix9:', result)
print('The returned matrix is: ', myMat)

myMatrix10 = [[[['a', 'b', 'c']]],
              [[['d', 'e', 'f']], ['g', 'h', 'i']],
              ['j', 'k', 'a'], ['b', 'c', 'd'],
              ['e', 'g', 'h', 'i']]

result, myMat = outerChkMyMatrix(myMatrix10)
print('\nThe result of checking the matrix10:', result)
print('The returned matrix is: ', myMat)

myMatrix11 = [[[['a', 'b', 'c']]],
              [[['d', 'e', 'f']], [[[[[[[[['g', 'h', 'i']]]]]]]]],
               ['j', 'k', 'a']],
              ['b', 'c', 'd'], ['e', 'f', 'g'],
              ['h', 'i', 'j']]

result, myMat = outerChkMyMatrix(myMatrix11)
print('\nThe result of checking the matrix11:', result)
print('The returned matrix is: ', myMat)

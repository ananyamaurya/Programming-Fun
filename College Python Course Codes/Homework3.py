"""
@author : Ananya

Problem: Perform following operations
# Define a list with different sub-lists having only integers.
# There can be any number of sub-lists with each of them having any number of integers.
# Take it in and append each sub-list with the sum of its values which are already in it.
# Each sub-list is updated with the sum of its elements, as its last element.
# Write a function which accepts the initial list (inList) with sub-lists already filled in.
# Construct a newList which is having the sorted sub-lists based on the last sum element.
# The sorting is to be in the increasing order.
# You are allowed to use only the inList and the newList.
# Try to write the program without needing to have additional lists or any other data
structures.
# You are free to use any built-in functions available.
# The sample inList, and the constructed newList with various values are given in the next
page.
# Define a function that accepts the inList as: def makeNewList(inList):
# Define additional function(s), if required, to have a modular design.

Input Data :
    inList1 = [[1, 2], [3, 4, 5, 7], [5, 6], [7, 8, 1], [0, 1], [1]]
    inList2 = [[1, 2], [3, 4, 5, 7], [5, 6], [7, 8, 1], [0, 1], [1], [0]]
    inList3 = [[1, 2, 5, 6, 8], [], [], [3, 4, 5, 7], [5, 6], [7, 8, 1], [0, 1], [2], [1], [0]]
    inList4 = [[1, 2, 5], [], [3, 4, 5, 7], [5, 6], [7, 8, 1], [0, 1], [1], [0]]
"""


def listSum(li):
    """
    :parameter: list of sublists
    :returns:  list with sum of elements of sublists appended to sublists
    """
    for i in li:
        i.append(sum(i))
    return li


def sortByLast(x):
    return x[len(x)-1]


def makeNewList(list1):
    newList = sorted(list1, key=sortByLast)
    return newList


# Operating on inList1
# List of elements
inList1 = [[1, 2], [3, 4, 5, 7], [5, 6], [7, 8, 1], [0, 1], [1]]
print("Initial List1 :::\n", inList1)
# Appends the sum elements of sublist to sublists
inList1 = listSum(inList1)
print("\ninList1  after sublistSum Operation :::\n", inList1)
newList1 = makeNewList(inList1)
print("\n\nNewList1 \n", newList1)

# Operating on inList2
# List of elements
inList2 = [[1, 2], [3, 4, 5, 7], [5, 6], [7, 8, 1], [0, 1], [1], [0]]
print("Initial List2 :::\n", inList2)
# Appends the sum elements of sublist to sublists
inList2 = listSum(inList2)
print("\ninList2  after sublistSum Operation :::\n", inList2)
newList2 = makeNewList(inList2)
print("\n\nNewList2 \n", newList2)

# Operating on inList3
# List of elements
inList3 = [[1, 2, 5, 6, 8], [], [], [3, 4, 5, 7], [5, 6], [7, 8, 1], [0, 1], [2], [1], [0]]
print("Initial List3 :::\n", inList3)
# Appends the sum elements of sublist to sublists
inList3 = listSum(inList3)
print("\ninList3  after sublistSum Operation :::\n", inList3)
newList3 = makeNewList(inList3)
print("\n\nNewList3 \n", newList3)

# Operating on inList4
# List of elements
inList4 = [[1, 2, 5], [], [3, 4, 5, 7], [5, 6], [7, 8, 1], [0, 1], [1], [0]]
print("Initial List4 :::\n", inList4)
# Appends the sum elements of sublist to sublists
inList4 = listSum(inList4)
print("\ninList4  after sublistSum Operation :::\n", inList4)
newList4 = makeNewList(inList4)
print("\n\nNewList4 \n", newList4)

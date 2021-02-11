"""
Created on Fri Dec  18 15:10:39 2020

@author: anany

Objective:
    Write a recursive function which goes through an empty matrix passed to it which
    has many levels of inner matrices with varying depths, all of them being empty
    and fill them with a custom pattern provided as string while splitting it to a custom size.

"""

names_dict = {}
while True:
    name = str(input("Give full name of your friend or q or Q to quit: "))
    if name == 'q' or name == 'Q':
        break
    nick_name = str(input(f"Give nick name to {name} or q or Q to quit: "))
    if nick_name == 'q' or nick_name == 'Q':
        break
    names_dict[nick_name] = name

while True:
    nick_name = str(input("\nEnter nick name to find name of friend or q or Q to quit: "))
    if nick_name == 'q' or nick_name == 'Q':
        break
    # instead of try except, get() method can also be used. dict_name.get(key) returns None if no entry with the key is found.
    try:
        print(names_dict[nick_name])
    except KeyError:
        print(f"Friend with nick name \"{nick_name}\" does not exist")


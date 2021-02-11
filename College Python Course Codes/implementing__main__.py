# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:31:54 2020

@author: anany
"""
import sys
if __name__ == "__main__":
    print("I am being called from a command line or run independently")
    print("My file name is : ",sys.argv[0])
    
if __name__ != "__main__":
    def display_import():
        print("I am being imported by a script:")
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:25:32 2020

@author: anany
"""
import sys
import os


print("Python Version",sys.version)

print("Operating System :: ",os.name)


print("Process ID :: ",os.getpid())

print("Process ID of Parent Process",os.getppid())

print("Environment Information",os.environ)
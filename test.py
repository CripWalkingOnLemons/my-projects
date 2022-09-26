from ast import ExceptHandler
import sys
import os

global list
global name
list = ["john","John","JOHN"]

name = input("hello what is you name\n")
for i in list:
    if name == i:
        print("it works")
        break
    else:
        print("Wrong answer")
        break





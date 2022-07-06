#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 23:53:44 2022

@author: swarnendu
"""


# Special Operators

word="swarnendu"

for item in enumerate(word):
    print(item)
    
list1=[1,2,3,4]
list2=["ssg","av","sk","avik","tb"]  

for item in zip(list1,list2):  
    print(item)
    
    
# Tuple unpacking

for a,b in zip(list1,list2):
    print(b)
    

# one way of writing items of a string in a list

listA=[]

for item in word:
    listA.append(item)

# List comprehensions


list=[item for item in word]        


listB =[num**2 for num in range(0,10)]


listC=[]

x=[1,2,3,4,5]

for item in x:
    listC.append((9/5)*item)


import math

m=[2.1,3.1,4.1,5.1]

n=[math.sin(item) for item in m]












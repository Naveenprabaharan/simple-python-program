# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:58:22 2022

@author: navee
"""

def isMonotonic(array):
    ascSort = sorted(array)
    decSort = ascSort[::-1]
    if array == ascSort or array==decSort:
        print('True')
    else:
        print("False")
        

#test cases :

isMonotonic([1,2,3])
isMonotonic([1,2,2])
isMonotonic([3,2,1])
isMonotonic([1,2,2])
isMonotonic([3,3,3])
isMonotonic([1])
isMonotonic([])
isMonotonic([2,2,3,1])
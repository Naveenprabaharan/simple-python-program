# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:04:57 2022

@author: naveenprabaharan
"""


def sorteedSquared(a):
    newArray = [x**2 for x in a]
    newArray.sort()
    return newArray

print("Sorted Array : ",sorteedSquared([1,2,3]))
print("Sorted Array : ",sorteedSquared([-4,-1,0,1,2,3]))
print("Sorted Array : ",sorteedSquared([]))
    

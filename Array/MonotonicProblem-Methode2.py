# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:25:15 2022

@author: navee
"""


def checkMonotonic(array):
    if len(array)==0:
        return True
    first = array[0]
    last = array[len(array)-1]
    
    #eqal case [2,2,2,2,2]
    if first==last:
        for i in range(0,len(array)-1):
            if (array[i] != array[i]):
                return False
            
    #non Decresing [1,2,3]
    elif first < last:
        for i in range(0,len(array)-1):
            if (array[i] > array[i+1]):
                return False
            
    # non  increasing [3,2,1]
    else :
        for i in range(0,len(array)-1):
            if (array[i] < array[i+1]):
                return False
    return True
        
    
            
#test cases :

print('value : ',checkMonotonic([1,2,3]))
print('value : ',checkMonotonic([1,2,2]))
print('value : ',checkMonotonic([3,2,1]))
print('value : ',checkMonotonic([1,2,2]))
print('value : ',checkMonotonic([3,3,3]))
print('value : ',checkMonotonic([1]))
print('value : ',checkMonotonic([]))
print('value : ',checkMonotonic([2,2,3,1]))
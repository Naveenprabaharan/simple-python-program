# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:21:11 2022

@author: naveenprabaharan
"""


# methode-1

def sortedSquared(array):
    a,b = 0,len(array)-1
    move = len(array)-1
    newarray = [0 for x in range(len(array))]
    
    while(a<=b and move>=0):
        
        if abs(array[a])>abs(array[b]):
            newarray[move] = array[a]**2
            a+=1
            move-=1
            
        else:            
            newarray[move] = array[b]**2
            b-=1
            move-=1
            
            
    return newarray


# Methode-2

import math

def sortedSquared(array):
    a,b = 0,len(array)-1    
    newarray = [0 for x in range(len(array))]
    
    for i in range(len(array)-1,0,-1):
        leftsqrValue = pow(array[a],2)
        rightsqrValue = pow(array[b],2)
        
        if leftsqrValue>rightsqrValue:
            newarray[i] = leftsqrValue
            a+=1
            
            
        else:            
            newarray[i] = rightsqrValue
            b-=1
            
            
            
    return newarray

print("Sorted Array : ",sortedSquared([1,2,3]))
print("Sorted Array : ",sortedSquared([-4,-1,0,1,2,3]))
print("Sorted Array : ",sortedSquared([]))

# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:19:15 2021

@author: Alejandro MF
"""

def isPrime(num):
    if num == 0 or num ==1 or num==4:
        return False
    for i in range(2,num,1):
        if(num%i==0):
            return False
    return True

for i in range (20):
    if (isPrime(i)):
        print(i, end=" ")
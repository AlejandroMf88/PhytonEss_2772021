# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:58:36 2021

@author: Alejandro MF
"""

def l100kmtompg(liters):
    galones = liters / 3.785411784
    miles = 100 / 1.609344
    return miles / galones
    
def mpgtol100km(miles):
    km100 = miles * 1.609344 / 100
    litros = 3.785411784
    return litros / km100


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
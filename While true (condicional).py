# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:47:35 2021

@author: Alejandro MF
"""
contar=input("Ingrese el # de veces a contar: ")
contar=int(contar)
contador=1
while True:
    print(contador)
    contador+=1
    if contador>contar:
        break
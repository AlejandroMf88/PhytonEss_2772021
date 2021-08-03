# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:33:04 2021

@author: Alejandro MF
"""

def direccion (provincia, ciudad, barrio):
    print("Su direccion es: ")
    print("Su provincia es: ", provincia)
    print("La ciudad de domicilio es: ",ciudad)
    print("La dirección de referencia es: ", barrio)    

pr=input("Ingrese la provincia: ")
br=input("Ingrese el barrio: ")
ci=input("Ingrese la ciudad: ")

direccion(pr,ci,br)
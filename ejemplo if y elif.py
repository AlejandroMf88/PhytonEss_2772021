# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:44:43 2021

@author: Alejandro MF
"""

acl=int(input("ingrese el valor de la ACL: "))
if acl>=1 and acl<=99:
    print("La ACL es estándar")
elif acl>=100 and acl<=199:
    print("La ACL es extendida")
else:
    print("el # ingresado no corresponde a una ACL")

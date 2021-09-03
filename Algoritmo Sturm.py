# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:54:05 2021

@author: Fernanda Guzman
import math as mt
import numpy as np 

mi_funcion = lambda x: x**6 - (4*x)**3 + x - 2

P0 = [-2.0, 1.0, 0.0, -4.0, 0.0, 0.0, 1.0]

#La siguiente función deriva 
def derivar(A):
    Ap = []
    for i in range (len(A)):
        Ap.append(i*A[i])
    return Ap

#La siguiente función es el Teorema de Sturm
def Sturm(P0):
    x = len(P0)
    j = x-1
    P1 = derivar(P0)
    P2_aux = []
    for i in range (x):
        P2_aux.append(0)
    while j > 0:
        if(P1[j]!= 0):
            P2.append(P0[j]/P1[j])
            break
        j -= j
        P2 = []
"""


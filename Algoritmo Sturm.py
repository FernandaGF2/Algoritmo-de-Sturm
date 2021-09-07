# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:54:05 2021
@author: Fernanda Guzman
"""

def derivar (poli):
    polinomio2 = []

    for x in range (len(poli) - 1, 0, -1):
        polinomio2.append(poli[x] * x)
    
    polinomio2 = list (reversed(polinomio2))
    return polinomio2



def dividir (poli1, poli2):   #POLI1 == DIVIDENDO | POLI2 == DIVISOR
    while True :

        c = 0
        a = poli1[len(poli1) - 1] / poli2 [len(poli2) - 1]

        for x in range (len(poli2) - 1, -1, -1):
            b = a * poli2 [x]
            r = poli1[(len(poli1) - 1) - c] - b
            poli1[(len(poli1) - 1) - c] = r
            c = c + 1
        
        x = len(poli1) - 1

        while poli1 [x] == 0:
            poli1.pop(x)
            x = x - 1
        
        if len(poli1) < len (poli2):
            break

    poli1 = [num * -1 for num in poli1]

    return poli1


def sturm (a):
    
    print (a)
    b = derivar(a)
    print (b)

    while True:
        c = dividir(a, b)
        print (c)

        if len (c) != 1:
            a = b 
            b = c
        else:
            break


polinomio = [-2, 1, 0, -4, 0, 0, 1]

sturm(polinomio)

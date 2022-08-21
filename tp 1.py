# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:49:18 2022

@author: Admin
"""
n=int(input())
lista=list(range(1,n))
primos(lista)

def primos(lista):
    nopri=[]
    primos=[]
    for i in lista:
        for n in range(2,i):
            if i%n == 0 :
                nopri.append(i)
                break
        if i not in nopri:
            primos.append(i)
    return len(primos)


def esprimo(n):
    numero=True
    for i in range (2,n):
        if (n % i == 0):
            numero=False
            break
    return numero

for i in range(1,20):
    if esprimo(i)==True:
        primos.append(i)

def contraseña():
    a=input('Nombre completo: ')
    b=input('DNI: ')
    c=input('fecha nac: (dd/mm/aa)')
    
    
    
    
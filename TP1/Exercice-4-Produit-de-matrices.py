# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 14:07:08 2018

@author: Asus
"""

#AMIRAT Hani
#FROSSARD Gabriel

#Fonction qui effectue le produit matriciel de 2 matrices de tailles quelconques
def multiplication(A,B):
    n = len(A); p = len(A[0]);  q = len(B[0])
    return [[sum([A[i][k]*B[k][j] for k in range(p)]) for j in range(q)] for i in range(n)]
    

A=[[1,2,7],[8,4,2],[5,9,10]]   
B=[[1,5,13],[7,8,3],[20,1,0]]
C=multiplication(A,B)
print(C)
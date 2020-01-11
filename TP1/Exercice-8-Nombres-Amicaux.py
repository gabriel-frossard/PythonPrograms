# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 14:07:56 2018

@author: Asus
"""

#AMIRAT Hani
#FROSSARD Gabriel

#Fonxtion qui liste tout les diviseurs de n saisi
def diviseurs(n):
    
    L=[]    
    for i in range(n):
        if n%(i+1)==0:
            L.append(i+1)
            
    return L

#Fonction qui somme les valeurs d'une liste    
def somme(L):
    
    Sum=0
    for val in L:
        Sum+=val
    
    return Sum
    
#Fonction qui vérifie si 2 nombres sont amicaux ou non
def NbAmicaux(A,B):
    
    DiviseursA=diviseurs(A)  
    DiviseursB=diviseurs(B)
    SommeA=somme(DiviseursA)  #SommeA est la somme des diviseurs de A
    SommeB=somme(DiviseursB)  #SommeB est la somme des diviseurs de B
    
    if SommeA==SommeB==A+B:   # Condition verifian si A et B sont amicaux ou non
        return "Les 2 nombres sont amicaux"
    else:
        return "Les 2 nombres ne sont pas amicaux"
        

N=NbAmicaux(220,284)
print(N)
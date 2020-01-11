# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 14:08:36 2018

@author: Asus
"""

#AMIRAT Hani
#FROSSARD Gabriel

#Fonction booléene qui renvoit True si le nombre n est tricolore ou False sinon        
def tricolore(n):
    val=str(n*n)
    for i in val:
        if i not in ['1','4','9']:
            return False
    
    return True

#Fonction qui liste tout les nombres tricolores avant le nombre N choisi
def tous_les_tricolores(N):
    L=[]
    for val in range(N):
        if tricolore(val)==True:
            L.append(val)
            
    return L
    
print(tricolore(21))
print(tous_les_tricolores(5423))
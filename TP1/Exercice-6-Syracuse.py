# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 14:07:38 2018

@author: Asus
"""

#AMIRAT Hani
#FROSSARD Gabriel

#Fonction qui renvoit la suite de Syracuse du nombre n saisi
def Syracuse(n):
    L1=[n]
    while n!=1:
        if n%2==0:
            L1.append(n/2)
            n=n/2
        else:
            L1.append(3*n+1)
            n=3*n+1
    return L1
        

#Fonction qui renvoit l'altiude de la suite de Syracuse du nombre n saisi
def Altitude(n):
    L2=Syracuse(n)
    return max(L2)    

#Fonction qui renvoit le temps de vol de la suite de Syracuse du nombre n saisi
def TpsVol(n):
    L3=Syracuse(n)
    return len(L3)-1

#Fonction qui renvoit le nombre étant compris entre 1 et 1000 qui possède 
#la plus grande altitude dans sa suite de Syracuse
def AltitudeMax():
    L4=[]
    for i in range(1,1001):
        L4.append(Altitude(i))
    return L4.index(max(L4))+1
 
#Fonction qui renvoit le nombre étant compris entre 1 et 1000 qui possède
#le plus grand temps de vol pour sa suite de Syracuse
    
def TpsVolMax():
    L5=[]
    for i in range(1,1001):
        L5.append(TpsVol(i))
    return L5.index(max(L5))+1
    

S=Syracuse(10)
print(S)
M=Altitude(10)
print(M)
T=TpsVol(10)
print(T)
a=TpsVolMax()
print(a)
b=AltitudeMax()
print(b)
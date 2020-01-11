# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 14:07:27 2018

@author: Asus
"""

#AMIRAT Hani
#FROSSARD Gabriel

def hanoi(n,depart,arrivee,autre):
   
    if n > 1:
        hanoi(n-1,depart, autre, arrivee)
    
    if n == 1:
        print ("déplacer plot "+str(depart)+" vers "+str(arrivee))
        return
    print ("déplacer plot "+str(depart)+" vers "+str(arrivee))
    hanoi(n-1,autre,arrivee,depart)
    return
    
print(hanoi(4,1,2,3)) 

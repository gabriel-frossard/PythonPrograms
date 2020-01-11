# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:26:29 2018

@author: gabriel.frossard
"""

import random

def mot_aleatoire():
    mot=''
    L=[]
    
    fich=open("Dico.txt",'r')
    for ligne in fich:
        L=L+[ligne[0]]
    fich.close()
    
    rnd=random.choice(L)
    
    fich=open("Dico.txt",'r')
    for ligne in fich:
        if ligne[0]==rnd:
            mot=ligne[1:]
    fich.close()
     
    return mot.strip()
    
def liste_as_str(L):
    chaine=''
    for i in L:
        chaine=chaine+i
    return chaine


def pendu():
    mot=mot_aleatoire()
    L=[mot[0]]
    for caract in range(len(mot)-1):
        L=L+['_']
    print ("-".join(L),' vous avez 8 chances')
    chance_restante=8
    lettre=''
    liste_lettre=[]
    while chance_restante!=0 and liste_as_str(L)!=mot:
        lettre=input('une lettre ? ')
        while lettre in liste_lettre:
            print ('lettre deja utilisé')
            lettre=input('une autre lettre ? ')
        liste_lettre=liste_lettre+[lettre]
            
        if (lettre in mot)==True:
            for i in range(1,len(mot)):
                if lettre==mot[i]:
                    L[i]=lettre        
        else:
            chance_restante-=1
        
        if chance_restante!=0:
            print ("-".join(L),' il vous reste', chance_restante, 'chances restantes')
    
    if chance_restante==0:
        print ('Tu as perdu !')
    if liste_as_str(L)==mot:
        print ('Tu as gagné !')     
        
    choix=input('rejouer:1 , ne pas rejouer:0  ')
    
    if choix== '0':
        print ('au revoir')
    if choix== '1':
        pendu()
    
print(pendu())


    
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:31:48 2018

@author: gabriel.frossard
"""

from tkinter import Tk, Label, Button, StringVar, Entry, Canvas
import random

#Fonction pendu

def mot_aleatoire():
    global mot # création de la variable mot pour tout le programme
    mot=''
    L=[]
    
    fich=open("Dico.txt",'r') # ouvre le fichier texte contenant les mots du jeu
    for ligne in fich: # création de notre liste de numéro des mots (voir fichier txt)
        L=L+[ligne[0]]
    fich.close()
    
    rnd=random.choice(L) # choix d'une position au hasard dans notre liste de mots
    
    fich=open("Dico.txt",'r') # sélection du mot correspondant à la position choisie aléatoirement
    for ligne in fich:
        if ligne[0]==rnd:
            mot=ligne[1:]
    fich.close()
     
    return mot.strip()
    
def liste_as_str(L): # fonction qui transforme notre liste en chaine de caractères
    chaine=''
    for i in L:
        chaine=chaine+i
    return chaine
        
        
def ouvrir_image(nb): # Fonction qui ouvre les images dans le canvas 
    global photo
    global item
    Canevas.delete(ALL)
    photo=PhotoImage(file='bonhomme'+str(nb)+'.gif')
    item=Canevas.create_image(300,160,image=photo) 
    
    
def demarrer():
    
    dem.set("Démarrer pendu")
    global chance
    chance=8
    mot=mot_aleatoire() 
    
    ouvrir_image(chance) # ouvre l'image du début
    
    global L    
    L=[mot[0]]
    for caract in range(len(mot)-1): # initialisation et affichage du mot à découvrir 
        L=L+['_']   
    resultat.set("") # création d'un champ résultat
    mot_affich.set("") # création d'un champ affichage du mot
    mot_affich.set("-".join(L)) 
    resultat.set(str(chance)+"  chance restantes")

def pendu(): # fonction du jeu 
    global chance
    if lettre.get()=="" or len(lettre.get())>1 : # sécurisation de la saisie d'une lettre unique
        resultat.set("choisissez une lettre")
    
    elif (lettre.get() in mot) :  # le joueur trouve une lettre
        resultat.set("")
        for i in range(1,len(mot)):
                if lettre.get()==mot[i]: # la bonne lettre est replacée dans le mot
                    L[i]=lettre.get()
        mot_affich.set("-".join(L))            
        resultat.set(str(chance)+"  chance restantes") # affichage du nombre de chances restantes
            
    elif mot!="" and chance!=0 and chance-1!=0: # le joueur donne une mauvaise lettre
        chance -= 1
        resultat.set("pas la bonne lettre "+str(chance)+"  chance restantes") #affichage du nombre de chances restantes
        ouvrir_image(chance) # affichage de la l'image correspondante au nombre de chances restantes
     
    elif chance-1==0 :
        resultat.set("Vous avez perdu !") # défaite du joueur
        dem.set("Recommencer ?") # proposition de relancer le jeu
        
    if mot_affich.get().replace("-","")==mot.strip(): # vérification si, avec la dernière lettre proposée, le mot est trouvé
        resultat.set("Vous avez gagné !") # victoire du joueur
        dem.set("Recommencer ?")
    
    mot_affich.set("-".join(L))
    lettre.set("")
  
  
#création de la fenêtre
fen_pendu=Tk()
fen_pendu.title('PENDU 2K18')
fen_pendu.geometry('600x600')
#Création d'un widget Canvas
Canevas = Canvas(fen_pendu, width = 600, height = 425, bg = 'grey')

Canevas.pack(padx=5,pady=5)

#création d'un widget Button('Démarrer pendu')
dem=StringVar()
dem.set("Démarrer pendu")
Bouton2=Button(fen_pendu,textvariable=dem,command=demarrer)
Bouton2.pack(padx=5,pady=5)

#création d'un widget Button('Proposer')

Bouton1=Button(fen_pendu,text='Proposer',command=pendu)
Bouton1.pack(padx=5,pady=10)


#création d'un widget entry
lettre=StringVar()
Lettre=Entry(fen_pendu,textvariable=lettre)
Lettre.focus_set()
Lettre.pack(padx=5,pady=2)

#création d'un widget Label('mot à trouver')
mot_affich=StringVar()
Label1=Label(fen_pendu,textvariable=mot_affich)
Label1.pack(padx=5,pady=5)

resultat=StringVar()
label = Label(fen_pendu, textvariable = resultat)
label.pack(padx = 9, pady = 5)    


fen_pendu.mainloop()

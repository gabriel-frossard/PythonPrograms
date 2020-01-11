# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#AMIRAT Hani
#FROSSARD Gabriel

#fonction qui renvoit True pour une année bissextile et False sinon
def AnneeBissextile(an):
    
    if an % 400 == 0:
        return True
    if an % 100 != 0 and an % 4 == 0:
        return True
    else:
        return False

#Fonction qui renvoit le nombre de jour d'un mois (ici les mois sont numérotés: Janvier=1, etc...)
#La fonction prend en compte si l'année est bissextile ou non (pour février si 28 ou 29 jours)
def NbJourMois(mois,an):
    
    if mois < 1 and mois > 12 :
        return False
        
    if AnneeBissextile(an) == True and mois == 2:
        return 29
    elif AnneeBissextile(an) == False and mois == 2:
        return 28
    else:
        if mois in [1,3,5,7,8,10,12]:
            return 31
        else:
            return 30

#Fonction vérifiant si la date est valide ou non
#La fonction est valide si le date du jour du mois saisi sera conforme au mois saisi 
def DateValide(j,m,a):
    if j > NbJourMois(m,a) :
        return "Date Non Valide"
        
    else:
        return "Date Valide"
        
        
        
print(AnneeBissextile(2020))
print(NbJourMois(9,2007))
print(DateValide(29,2,2008))
jour=input("Rentrez votre jour:")
mois=input("Rentrez votre mois:")
annee=input("Rentrez votre annee:")
print(DateValide(jour,mois,annee))

    



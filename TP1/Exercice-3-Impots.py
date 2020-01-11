# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 14:06:51 2018

@author: Asus
"""

#AMIRAT Hani
#FROSSARD Gabriel

#Fonction qui calcule le montant de l'impôts sur les revenus d'une personne 
def MesImpots(revenu):
    
    if 0 < revenu < 9807:                #Tranche 1
        impots = 0
    
    elif 9807 < revenu < 27086:          #Tranche 2
        impots = (revenu-9807) * 14/100
       
        
    elif 27086 < revenu < 72617:         #Tranche 3
        impots1 = (revenu-27086) * 30/100
        impots2 = (27086-9807) * 14/100
        impots = impots1 + impots2        
        
    elif 72617 < revenu < 153783:        #Tranche 4
        impots1 = (revenu-72617) * 41/100
        impots2 = (72617-27086) * 30/100
        impots3 = (27086-9807) * 14/100
        impots = impots1 + impots2 + impots3
    
    elif revenu > 153783:                #Tranche 5
        impots1 = (revenu-153783) * 45/100
        impots2 = (153783-72617) * 41/100
        impots3 = (72617-27086) * 30/100
        impots4 = (27086-9807) * 14/100
        impots = impots1 + impots2 + impots3 + impots4
        
    return impots
    

Impots=MesImpots(15000) 
print(Impots)
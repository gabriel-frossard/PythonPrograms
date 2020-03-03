"""FROSSARD"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                 Ligne de Partage des Eaux / Watershed                   "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import numpy as np
import cv2
import matplotlib.pyplot as plt

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                    Pre-traitement                     "        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""
"      Obtention des marqueurs        " 
"""""""""""""""""""""""""""""""""""""""   

#Lecture de l'image et conversion en niveau de gris
Img_smarties = cv2.imread("smarties.jpg",0) #Image grayscale

#affichage de l'image en niveaux de gris
plt.figure(1)
plt.imshow(Img_smarties)
plt.show()


#Seuillage de l'image
ret,Img_seuil = cv2.threshold(Img_smarties, 250, 255, cv2.THRESH_BINARY_INV)

#ret,Img_inv = cv2.threshold(Img_seuil, 250, 255, cv2.THRESH_BINARY_INV)
plt.figure(2)
plt.imshow(Img_seuil, 'gray')
plt.show()

ret,Img_inv = cv2.threshold(Img_smarties,250,255, cv2.THRESH_BINARY) #inversion de l'image (pour plus tard)


#Separation des elements -> ouverture

#on erode une fois avec un element structurant de taille 15, 35
elem = np.ones((15,35),np.uint8)
Img_ouv = cv2.erode(Img_seuil, elem, iterations = 1)

#on dilate deux fois avec un element structurant de taille 5, 5
elem = np.ones((5,5),np.uint8)
Img_ouv = cv2.dilate(Img_ouv, elem, iterations = 2)

plt.figure(3)
plt.imshow(Img_ouv,'gray')
plt.show()
#On verifie bien que les differents elements ne se touchent pas

#Attribution des labels
ret, Img_zones = cv2.connectedComponents(Img_ouv)
Img_zones = Img_zones+1 #le font de l'image a maintenant un label 1 et non 0

plt.figure(4)
plt.imshow(Img_zones)
plt.show()

Img_sum = Img_zones*8 + Img_inv #On veut afficher nos marqueurs labélisés sur l'image seuillée

plt.figure(5)
plt.imshow(Img_sum)
plt.show()

#nous avons maintenant acces aux marqueurs de chaque bonbons 


"""""""""""""""""""""""""""""""""""""""
"         Carte des distances         " 
"""""""""""""""""""""""""""""""""""""""

Img_dist = cv2.distanceTransform(Img_seuil,cv2.DIST_L2,5)

plt.figure(5)
plt.imshow(np.uint8(Img_seuil - Img_dist/np.max(Img_dist)*np.max (Img_seuil)), 'gray') #On obtient l'image voulue
plt.show()

Img_dist = Img_dist/20*255 #Calcul à la main

plt.figure(6)
plt.imshow(Img_dist, "gray")
plt.show()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"                    Algorithme LPE                     "        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#liste_coord accueillera les coordonnées des pixels et les rangera en fonction 
#de leur niveau de gris sur l'image des distances. ce sera la FAH
liste_coord = []
for i in range (int (np.max(Img_dist)+1)):   #on cree autant de sous-listes qu'il y a de niveaux de gris dans l'image des distances
    liste_coord.append([])

#on parcourt l'image des zones, Si le pixel appartient à la zone d'un smarties, on l'ajoute à coord_liste dans la bonne sous-liste
for j in range(1, 500):
    for i in range (1, 228) :
        if Img_zones[i,j] != 1 :    #si la zone n'est pas le fond de l'image
            liste_coord[int (Img_dist[i, j])].append((i,j)) #dans la sous-liste correspondant au bon niveau de gris on ajoute le pixel
 
#liste_finish reference tous les pixels qui ont deja étés traités           
liste_finish = []

#on parcourt les sous listes de liste_coord en partant des distances les plus élevées (l'interieur des smarties)
for couleur in range (250):
    couleur = 255 - couleur
    
    #plt.figure(7)           #Ces lignes permettent d'afficher les 250 etapes intermediaires de la segmentation
    #plt.imshow(Img_zones)
    #plt.show()     
    
    #tant que le niveau de gris n'est pas vide, on continue
    while liste_coord[couleur] != [] :
        
        #on prend le premier pixel de la sous-liste
        a = liste_coord[couleur][0]
        
        #si le pixel n'est pas sur le bord de l'image, on le traite
        if a[0] != 1 and a[0] != 228 and a[1] != 1 and a[1] != 500 :
            
            #voisin du bas
            #si le pixel voisin n'est pas dans liste_coord et n'a pas deja été traité, on le traite
            if ((a[0]+1, a[1]+0) not in  liste_coord[int(Img_dist[a[0]+1, a[1]+0])]) and ((a[0]+1, a[1]+0) not in liste_finish):
                #le pixel voisin appartient maintenant à la zone du pixel a
                Img_zones[a[0]+1, a[1]+0] = Img_zones[a]
                #on ajoute le pixel voisin a la bonne place dans liste_coord
                liste_coord[int(Img_dist[a[0]+1, a[1]+0])].append ((a[0]+1, a[1]+0))
                    
            #voisin de gauche
            if (a[0] + 0, a[1] - 1) not in liste_coord[int(Img_dist[a[0] + 0, a[1] - 1])] and (a[0] + 0, a[1] - 1) not in liste_finish:
                Img_zones[a[0] + 0, a[1] - 1] = Img_zones[a]
                liste_coord[int(Img_dist[a[0] + 0, a[1] - 1])].append((a[0] + 0, a[1] - 1))

            #voisin du haut
            if (a[0]-1, a[1]+0) not in liste_coord[int(Img_dist[a[0] - 1, a[1] + 0])] and (a[0] - 1, a[1] + 0) not in liste_finish:
                Img_zones[a[0] - 1, a[1] + 0] = Img_zones[a]
                liste_coord[int(Img_dist[a[0] - 1, a[1] + 0])].append ((a[0]-1, a[1]+0))
                        
            #voisin de droite
            if (a[0] + 0, a[1] + 1) not in liste_coord[int(Img_dist[a[0] + 0, a[1] + 1])] and (a[0] + 0, a[1] + 1) not in liste_finish:
                Img_zones[a[0] + 0, a[1] + 1] = Img_zones[a]
                liste_coord[int(Img_dist[a[0] + 0, a[1] + 1])].append((a[0] + 0, a[1] + 1))
                
        #le pixel a a été traité
        liste_finish.append(a)
        #on l'enleve de la liste_coord
        liste_coord[couleur].pop(0)
    

plt.figure(8)
plt.imshow(Img_zones)
plt.show()                                           

print ("Il y a sur l'image", np.max(Img_zones)-1, "smarties")
# -1 car le fond de l'image est considere comme une zone

#Sur l'image finale, on repere bien les différents smarties
#Les lignes entre les différentes couleurs sont les liges de partage des eaux

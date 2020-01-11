from tkinter import *
import random

vie = 3
murs = []
bas = False
haut = False    
colones_Detruites_Gauche = 0
colones_Detruites_Droite = 0
press_Gauche = 0
press_Droite =0 

'''fonction d initialisation, se lance quand on appuie sue le bouton start et met en place les personnages'''
def init():
    global lien_Vaisseau, lien_Alien1, lien_Alien2, lien_Alien_Mort, vaisseau, alien, aliens, lignes, colones, aliens_Image, nbr_Aliens_Morts
    nbr_Aliens_Morts = 0

    boutton_Start.destroy()

    '''creation du vaisseau (en dehors de l ecran)'''
    lien_Vaisseau = PhotoImage(file = 'vaisseau.gif')   #image 60x56px

    coord_Vaisseau_start_X = 600
    coord_Vaisseau_start_Y = 595
    decalage_Init_Vaisseau = 100

    vaisseau = canevas.create_image(coord_Vaisseau_start_X, coord_Vaisseau_start_Y + decalage_Init_Vaisseau, anchor = S, image = lien_Vaisseau)


    '''creation des aliens (en dehors de l ecran)'''
    lien_Alien1 = PhotoImage(file = 'alien1.gif')        #image 44x32px
    lien_Alien2 = PhotoImage(file = 'alien2.gif')
    lien_Alien_Mort = PhotoImage(file = 'explosion.gif')

    colones = range (300, 1000, 100)
    lignes = range (5, 205, 50)
    decalage_Init_Aliens = 210
    aliens = []
    aliens_Image = []
    for a in colones:
        ligne = 0
        
        for b in lignes :
            if ligne%2 == 0:
                alien = canevas.create_image (a, b - decalage_Init_Aliens, anchor = N, image = lien_Alien1)
            if ligne%2 == 1:
                alien = canevas.create_image (a, b - decalage_Init_Aliens, anchor = N, image = lien_Alien2)
            aliens.append(alien)
            
            ligne+=1

    '''deplacement du vaisseau en position initiale'''         
    deplacer_Vaisseau_Init(vaisseau, decalage_Init_Vaisseau)

    '''deplacement des aliens en position initiale'''
    deplacer_Aliens_Init(aliens, decalage_Init_Aliens, colones, lignes)
    
    vies_init()


'''fonction qui deplace le vaisseau jusqu a sa position intiale'''        
def deplacer_Vaisseau_Init(vaisseau, decalage_Init_Vaisseau):
    if decalage_Init_Vaisseau > 0:
        decalage_Init_Vaisseau -= 2
        canevas.move(vaisseau, 0, -2)
        ma_Fenetre.after(50, lambda: deplacer_Vaisseau_Init(vaisseau, decalage_Init_Vaisseau))
        return
    return



'''fonction qui deplace les aliens jusqu a leur position initiale'''
def deplacer_Aliens_Init(aliens, decalage_Init_Aliens, colones, lignes):
    global ready_Mouvement, tire_Ok, vitesse_Temps
    if decalage_Init_Aliens > 0:
        decalage_Init_Aliens -= 2
        for a in aliens:
            canevas.move(a, 0, 2)
        ma_Fenetre.after(25, lambda: deplacer_Aliens_Init(aliens, decalage_Init_Aliens, colones, lignes))
    else:     
        ma_Fenetre.after(200, lambda: deplacement_Aliens(aliens))
        ready_Mouvement = 1
        tire_Ok = 1
        tire_Aliens()


def deplacement_Aliens(aliens):
    global vitesse_X, vitesse_Y, lignes, colones, aliens_Maj
    y_Max = 0
    for a in aliens:
        if a != 'mort':
            coord = canevas.coords(a)
            if coord[1] + 32 > y_Max:
                y_Max = coord[1] +32
    if y_Max < 450:
        if colones[-1] + 22 + vitesse_X > 1100:
            vitesse_X = -vitesse_X
            for a in aliens:
                if type(a) == str():
                    return
                else:
                    canevas.move(a, 2*(1100- colones[-1]- 22)+ vitesse_X, vitesse_Y)
    
            for a in lignes:
                nouv = a + vitesse_Y
                lignes[lignes.index(a)] = nouv
    
            for a in colones:
                nouv = a + 2*(1100- colones[-1]- 22)+ vitesse_X
                colones[colones.index(a)] = nouv
                
    
        elif colones[0] - 22 + vitesse_X < 100:
            vitesse_X = -vitesse_X
            for a in aliens:
                if type(a) == str():
                    return
                else:
                    canevas.move(a, -(2* (-100 + colones[0] - 22) - vitesse_X), vitesse_Y)
    
            for a in lignes:
                nouv = a + vitesse_Y
                lignes[lignes.index(a)] = nouv
    
            colone0 = colones[0]
            for a in colones:
                nouv = a - (2* (-100 + colone0 - 22) - vitesse_X)
                colones[colones.index(a)] = nouv
                
    
        else:
            for a in aliens:
                if type(a) == str():
                    return
                else:
                    canevas.move(a, vitesse_X, 0)
            for a in colones:
                nouv = a + vitesse_X
                colones[colones.index(a)] = nouv
        maj_Colones()
        ma_Fenetre.after(vitesse_Temps, lambda: deplacement_Aliens(aliens))
        
    else:
        print('DEFAITE')        
        
        
        
def maj_Colones():
    global colones, aliens, aliens_Maj, colones_Detruites_Gauche, colones_Detruites_Droite, colones_Maj, colones_Detruites
    aliens_Maj = aliens
    compteur_Gauche = 0
    compteur_Droite = 0
    while aliens_Maj [0] == 'mort' and aliens_Maj [1] == 'mort' and aliens_Maj [2] == 'mort' and aliens_Maj [3] == 'mort':
        
        aliens_Maj = aliens_Maj[4:]
        compteur_Gauche +=1
        

        if compteur_Gauche > colones_Detruites_Gauche:
            colones = colones[1:]
            colones_Detruites_Gauche += 1
            
    while aliens_Maj [-1] == 'mort' and aliens_Maj [-2] == 'mort' and aliens_Maj [-3] == 'mort' and aliens_Maj [-4] == 'mort':
        aliens_Maj = aliens_Maj[:-4]
        compteur_Droite +=1
        if compteur_Droite > colones_Detruites_Droite:
            colones = colones[:-1]
            colones_Detruites_Droite += 1

    colones_Detruites = colones_Detruites_Gauche + colones_Detruites_Droite

def deplacement_Vaisseau_Gauche():
    global vaisseau, press_Gauche
    if ready_Mouvement == 1 and press_Gauche == 1:
        if canevas.coords(vaisseau)[0] - 30 <= 100:
            canevas.coords(vaisseau, 130, 595)
        else:
            canevas.move(vaisseau, -10, 0)
            ma_Fenetre.after(500, deplacement_Vaisseau_Gauche)
            
def deplacement_Vaisseau_Droite():
    global vaisseau, press_Droite
    if ready_Mouvement == 1 and press_Droite == 1:
        if canevas.coords(vaisseau)[0] + 30 >= 1100:
            canevas.coords(vaisseau, 1070, 595)
        else:
            canevas.move(vaisseau, 10, 0)
            ma_Fenetre.after(500, deplacement_Vaisseau_Droite)
            
def deplacement_Vaisseau_BAS_OK(event):
    global vaisseau, bas
    if bas == False:
        coord_Vaisseau = canevas.coords(vaisseau)
        if coord_Vaisseau[0] > 590 and coord_Vaisseau[0] < 610:
            a = 200
            bas = True
            deplacement_Vaisseau_Bas(a)
        
 
def deplacement_Vaisseau_Bas(a):
    if a > 0 :
        a -= 1
        canevas.move(vaisseau, 0, 1)
        ma_Fenetre.after(50,lambda:deplacement_Vaisseau_Bas(a))
    else:
        #popup fuite
        print('1')
    
#def deplacement_Vaisseau_HAUT_OK(event):
#    global vaisseau, haut
#    if bas == False:
#        coord_Vaisseau = canevas.coords(vaisseau)
#        if coord_Vaisseau[0] > 70 and coord_Vaisseau[0] < 130:
#            a = 1000
#            bas = True
#            deplacement_Vaisseau_Haut(a)
#        
# 
#def deplacement_Vaisseau_Haut(a):
#    if a > 0 :
#        a -= 1
#        canevas.move(vaisseau, 0, -10)
#        ma_Fenetre.after(50,lambda:deplacement_Vaisseau_Haut(a))
#    else:
#        #popup fuite
#        print('1')
    
 
def mouvement_Droite_Ok(event):
    global press_Droite, bas
    if bas == False:
        if press_Droite == 0:
            press_Droite = 1
            deplacement_Vaisseau_Droite()
    
def mouvement_Droite_Stop(event):
    global press_Droite
    press_Droite = 0
    deplacement_Vaisseau_Droite()
    
def mouvement_Gauche_Ok(event):
    global press_Gauche, bas
    if bas == False:
        if press_Gauche == 0:
            press_Gauche = 1
            deplacement_Vaisseau_Gauche()
    
def mouvement_Gauche_Stop(event):
    global press_Gauche
    press_Gauche = 0
    deplacement_Vaisseau_Gauche()
    
    
def creation_Tire_Vaisseau(event):
    global vaisseau, tire_Ok, tire
    if tire_Ok == 1:
        tire_Ok = 0
        coord_tire_x1 = canevas.coords(vaisseau)[0] - 2
        coord_tire_y1 = canevas.coords(vaisseau)[1] - 25
        coord_tire_x2 = canevas.coords(vaisseau)[0] + 2
        coord_tire_y2 = canevas.coords(vaisseau)[1] - 11
        tire = canevas.create_rectangle(coord_tire_x1, coord_tire_y1, coord_tire_x2, coord_tire_y2,fill = 'yellow')
        deplacement_Tire_Vaisseau()
    
def deplacement_Tire_Vaisseau():
    global tire, tire_Ok
    try:
        if canevas.coords(tire)[1]< 0:
            canevas.delete(tire)
            tire_Ok = 1
            return
    except IndexError:
        pass
        
    canevas.move(tire, 0, -50)
    touche_V_M(tire)
    
    
    
    
    



def mort_Alien(numero_Alien):
    global aliens, lien_Alien_Mort, tire_Ok, nbr_Aliens_Morts, vitesse_Temps
    canevas.itemconfig(aliens[numero_Alien], image = lien_Alien_Mort)
    canevas.delete(tire)
    tire_Ok = 1
    vitesse_Temps -= 10
    ma_Fenetre.after(500, lambda: suppression_Explosion(numero_Alien))
    
    
def suppression_Explosion(numero_Alien):
    global aliens
    canevas.delete(aliens[numero_Alien])
    aliens[numero_Alien] = 'mort'
    victoire()
    
def apparition_Murs():
    global murs
    for a in range(250, 851 , 110):
        mur(a, 450)
    print (murs)
        
def mur(x, y):
    global murs
    longueur = 100
    hauteur = 50
    for a in range(0 + x, longueur + x, 10):
        for b in range(0 + y, hauteur + y, 10):
            mur = canevas.create_rectangle(a, b, a+10, b+10, fill = 'white')
            murs.append(mur)
    
    


   
def tire_Aliens():
    global aliens
    aliens_Vivants = []
    for a in aliens:
        if a != 'mort':
            aliens_Vivants.append(a)
    print (aliens_Vivants)
    try:
        rand = random.randint(0,len(aliens_Vivants)-1)
        alien_Tire = aliens_Vivants[rand]
        creation_Tire_Alien(alien_Tire)
        ma_Fenetre.after(2000, tire_Aliens)
    except ValueError:
        pass
    
    
def creation_Tire_Alien(alien_Tire):
    
    coord_tire_x1 = canevas.coords(alien_Tire)[0] - 2
    coord_tire_y1 = canevas.coords(alien_Tire)[1] + 32
    coord_tire_x2 = canevas.coords(alien_Tire)[0] + 2
    coord_tire_y2 = canevas.coords(alien_Tire)[1] + 40
    tire = canevas.create_rectangle(coord_tire_x1, coord_tire_y1, coord_tire_x2, coord_tire_y2,fill = 'yellow')
    deplacement_Tire_Alien(tire)
    
def deplacement_Tire_Alien(tire):
    try:
        if canevas.coords(tire)[1] > 574:
            canevas.delete(tire)
        canevas.move(tire, 0, +20)
        ma_Fenetre.after(100, lambda:deplacement_Tire_Alien(tire))
        touche_A_V(tire)
        touche_A_M(tire)
    except IndexError:
        pass
    
    
    
#def touche_A_M(tire):
#    global murs
#    coord_Tire = canevas.coords(tire)
#    print(tire)
#    for a in murs:
#        coord_Mur = canevas.coords(a)
#        if (coord_Tire[2] > coord_Mur[0] - 20):
#            print('a')
#            if (coord_Tire[1] < coord_Mur[1]) + 20:
#                print('b')
#                if (coord_Tire[3] > coord_Mur[1] - 20):
#                    print('c')
#                    if (coord_Tire[0] < coord_Mur[0] + 20) :
#                    
#
#
#
#                        canevas.delete(tire)
#                        canevas.delete(a)
#                        murs.pop(a)
#                        print('""""""""""""""""""""""""""""""""""""""""""')
                        
#def touche_A_M(tire):
#    global murs
#    coord_Tire = canevas.coords(tire)
#    b = canevas.find_overlapping(coord_Tire[0], coord_Tire[1], coord_Tire[2], coord_Tire[3])
#    print (b)
#    print(len(b))
#    if len(b) > 2:
#    #murs.pop(murs.index(b))
#        canevas.delete(tire)
#        canevas.delete(b)
#            
            
def touche_A_M(tire):
    global murs 
    coord_Tire = canevas.coords(tire)      
    for a in murs:
        coord_Mur = canevas.coords(a)
        if (coord_Tire[2] > coord_Mur[0] ) and (coord_Tire[1] < coord_Mur[1])  and (coord_Tire[3] > coord_Mur[1] ) and (coord_Tire[0] < coord_Mur[2] ):
            print ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            if a != 'detruit': 
                canevas.delete(tire)
                canevas.delete(a)
                murs[murs.index(a)] = 'detruit'
                print (murs)
                
def touche_V_M(tire):
    global murs, tire_Ok
    coord_Tire = canevas.coords(tire)      
    for a in murs:
        coord_Mur = canevas.coords(a)
        if (coord_Tire[2] > coord_Mur[0] ) and (coord_Tire[1] < coord_Mur[1])  and (coord_Tire[3] > coord_Mur[1] ) and (coord_Tire[0] < coord_Mur[2] ):
            print ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            if a != 'detruit': 
                canevas.delete(tire)
                canevas.delete(a)
                murs[murs.index(a)] = 'detruit'
            tire_Ok = 1
        else:
            touche_V_A()
            
def touche_A_V(tire):
    global vaisseau, vie
    coord_Tire = canevas.coords(tire)
    coord_Vaisseau = canevas.coords(vaisseau)
    if (coord_Tire[0] < coord_Vaisseau[0] + 40) and (coord_Tire[2] > coord_Vaisseau[0] - 40) and (coord_Tire[1] < coord_Vaisseau[1]) and (coord_Tire[3] > coord_Vaisseau[1] - 56):
        vie -= 1
        canevas.delete(tire)
        defaite(vie)
        vies()                       
 
 
def touche_V_A():
    global aliens, tire, tire_Ok, lignes,colones, nbr_Aliens_Morts, colones_Detruites_Gauche
    coord_Tire = canevas.coords(tire)
    for a in aliens:
        if a != 'mort':
            if (coord_Tire[0] < canevas.coords(a)[0] + 22 and coord_Tire[2] > canevas.coords(a)[0] - 22 and coord_Tire[1] < canevas.coords(a)[1] + 16 and coord_Tire[3] > canevas.coords(a)[1] - 16):
                numero_Alien = aliens.index(a)
                mort_Alien(numero_Alien)
                maj_Colones()
                return
            else:
                ma_Fenetre.after(100, lambda: deplacement_Tire_Vaisseau())


    
                             
 
 

          
def victoire():
    global aliens
    victoire = 1
    for a in aliens:
        if a != 'mort':
            victoire = 0
    if victoire == 1:
        ma_Fenetre.destroy()

                 
def defaite(vie):
    if vie == 0:
        ma_Fenetre.destroy()    

def vies_init():
    global vie, lien_Vaisseau, vaisseau1, vaisseau2, vaisseau3
    vaisseau1 = canevas.create_image(150, 650 , anchor = W, image = lien_Vaisseau) 
    vaisseau2 = canevas.create_image(230, 650 , anchor = W, image = lien_Vaisseau) 
    vaisseau3 = canevas.create_image(310, 650 , anchor = W, image = lien_Vaisseau) 
    label_Vie = Label(ma_Fenetre, text ="VIES :",fg ="white",bg ="black")
    label_Vie_c = canevas.create_window (120, 650, window = label_Vie)
    
def vies():
    global vie, vaisseau1, vaisseau2, vaisseau3
    print(vie)
    if vie == 2:
        canevas.delete(vaisseau3)
    elif vie == 1:
        canevas.delete(vaisseau2)
    else:
        canevas.delete(vaisseau1)
    
'''creation de la fenetre'''
ma_Fenetre = Tk()
ma_Fenetre.configure(bg = 'black')
ma_Fenetre.geometry('1200x700+0+0')


'''creation du canevas'''
canevas = Canvas (ma_Fenetre, bg = 'black', width = 1200, height = 700)
canevas.pack()

canevas.create_line(1100, 0, 1100, 600, fill = 'white')
canevas.create_line(100, 0, 100, 600, fill = 'white')
canevas.create_line(100, 600, 565, 600, fill = 'white')
canevas.create_line(635, 600, 1100, 600, fill = 'white')
canevas.create_line(565, 600, 565, 700, fill = 'white')
canevas.create_line(635, 600, 635, 700, fill = 'white')


'''variable qui determine quand le joueur prend le controle sur le vaisseau'''
ready_Mouvement = 0
tire_Ok = 0

'''vitesse de deplacement des aliens'''
vitesse_X = 50
vitesse_Y = 10
vitesse_Temps = 1000

'''bouton pour commencer la partie '''
boutton_Start = Button (ma_Fenetre, text = 'START', bg = 'black', fg = 'white', command = init, relief = FLAT)
boutton_Start_Can = canevas.create_window (602, 300, window = boutton_Start)

boutton_Quitter = Button (ma_Fenetre, text = 'EXIT', bg = 'black', fg = 'white', command = ma_Fenetre.destroy, relief = FLAT)
boutton_Quitter_Can = canevas.create_window (1150, 50, window = boutton_Quitter)



    
ma_Fenetre.bind('<KeyPress-q>', mouvement_Gauche_Ok)
ma_Fenetre.bind('<KeyPress-d>', mouvement_Droite_Ok)
ma_Fenetre.bind('<KeyPress-Left>', mouvement_Gauche_Ok)
ma_Fenetre.bind('<KeyPress-Right>', mouvement_Droite_Ok)
ma_Fenetre.bind('<KeyPress-s>', deplacement_Vaisseau_BAS_OK)
#ma_Fenetre.bind('<KeyPress-z>', deplacement_Vaisseau_HAUT_OK)

ma_Fenetre.bind('<space>', creation_Tire_Vaisseau)
 
ma_Fenetre.bind('<KeyRelease-q>', mouvement_Gauche_Stop)
ma_Fenetre.bind('<KeyRelease-d>', mouvement_Droite_Stop)
ma_Fenetre.bind('<KeyRelease-Left>', mouvement_Gauche_Stop)
ma_Fenetre.bind('<KeyRelease-Right>', mouvement_Droite_Stop)

apparition_Murs()


ma_Fenetre.mainloop()
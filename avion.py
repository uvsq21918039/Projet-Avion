#avion.py
#########
# Groupe MPCI 3
# Antoine Rios Campo
# William Mollet 
# Naoufal Amallah
# Anas Shaik
# Lakshmi Kootala
# Abdel Hakim Belmehdi 

# https://github.com/uvsq21918039/Projet-Avion
######
#########################################################
# import des librairies
import tkinter as tk 
import random as rd
########################################################


#########################################################
#définition des constantes

LARGEUR=40
HAUTEUR=60
LARGEUR_C=LARGEUR*30+2
HAUTEUR_C= HAUTEUR*7+2
NB_COL=30
NB_LIGN=7
COULEUR_QUADR = "black"
COULEUR_FOND ="white"
COULEUR_COULOIR ="grey50"
COULEUR_PASS_DEBOUT_SANS_BAGAGE ="green"
COULEUR_PASS_DEBOUT_AVEC_BAGAGE = "yellow"
COULEUR_PASS_ASSIS="red"
PASSAGER_DEBOUT_SANS_BAGAGE = 1
PASSAGER_DEBOUT_AVEC_BAGAGE = 2
PASSAGER_ASSIS = 3
#########################################################

#########################################################
#définition des variables globales
tableau=None 
passager=["Voici la liste des passagers: "]


#########################################################


#########################################################
#définition des fonctions 

def quadrillage():
    """Affiche un quadrillage constitué de cellule de taille 40x60 avec un couloir de couleur gris"""
    cellule = canvas.create_rectangle((0,3*HAUTEUR+2),(LARGEUR_C,4*HAUTEUR+2),fill=COULEUR_COULOIR)
    y = 2
    while y <= 8*HAUTEUR:
        canvas.create_line((0, y), (30*LARGEUR+2, y), fill=COULEUR_QUADR)
        y += HAUTEUR
    x = 2 
    while x <= 31*LARGEUR:
        canvas.create_line((x, 0), (x, 7*HAUTEUR+2), fill=COULEUR_QUADR)
        x += LARGEUR


def entree_avion():
    """Génere les passagers à l'entrée de l'avion et determine leur couleur en fonction des bagages"""
    global tableau
    for i in range(1, 181):
        #si l'entrée est libre
        if tableau[4][0] == 0:
                x = LARGEUR+2
                y = 3*HAUTEUR+2
            #si le passager n'a pas de bagages  
                if passager[i][3] == 0:
                    carre = canvas.create_rectangle((2, y), (x, y+HAUTEUR), fill=COULEUR_PASS_DEBOUT_SANS_BAGAGE)
                    tableau[4][0]= PASSAGER_DEBOUT_SANS_BAGAGE
            #si le passager a des bagages
                else :
                    carre = canvas.create_rectangle((2, y), (x, y+HAUTEUR), fill=COULEUR_PASS_DEBOUT_AVEC_BAGAGE)
                    tableau[4][0]= PASSAGER_DEBOUT_AVEC_BAGAGE  


###############################
#A COMPLETER
def mouv_passager():
    for i in range(1,181):
        for l in range(NB_LIGN):
            for c in range(NB_COL):
                #si la colonne du siège du passager n'est pas atteinte  
                if tableau[4][c] <= passager[i][1] :
                    #si la cellule de devant est libre
                    if tableau[4][c+1] == 0 :
                        canvas.move(carre, LARGEUR)
                        tableau[4][c] == 0
                #si la colonne du siège du passager est atteinte
                else :
                    #si le passager n'a pas de bagages
                    if passager[i][3] == 0 :
                        #si le siège du passager se situe vers la partie inferieure de l'avion
                        if passager[i][2] < 4 :
                            if tableau[l-1][c] == 0 :
                                canvas.move(carre, 0, -HAUTEUR)
                            else : 
                        #si le siège du passager se situe vers la partie supérieure de l'avion
                        else :  
                            if tableau[l+1][c] == 0 :
                                canvas.move(carre, 0, HAUTEUR)     
################################
           

def generateur_passager():
    """Génère une liste contenant les informations de chaque passager (numéro, ligne ,colonne, bagage)"""
    for i in range (1,181): 
        passager.append ([i, rd.randint(1,7), rd.randint(1,30), rd.randint(0,2)])
    for elem in passager :
        print(elem)    
  
#########################################################

#########################################################
#programme principal

tableau = []
for i in range(NB_LIGN):
    tableau.append([0]*NB_COL)   
print(tableau)

racine = tk.Tk()
racine.title("Automate Avion")



# création des widgets
canvas = tk.Canvas(racine,width=LARGEUR_C,height=HAUTEUR_C,bg="white")
lbl_entrée = tk.Label(racine, text="ENTREE")

# positionnement
canvas.grid(column=1,rowspan=7)
lbl_entrée.grid(column=0,row=3)
# autres fonctions
generateur_passager() 
quadrillage()
entree_avion()
# boucle principal
racine.mainloop()
########################################################



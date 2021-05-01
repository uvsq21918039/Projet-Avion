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
########################################################


#########################################################
#définition des constantes

LARGEUR=40
HAUTEUR=60
LARGEUR_C=LARGEUR*30+2
HAUTEUR_C= HAUTEUR*7+2
COULEUR_QUADR= "black"
COULEUR_FOND ="white"
COULEUR_PLACE_LIBRE="green"
COULEUR_PLACE_OCCUPE="red"

#########################################################

#########################################################
#définition des variables globales
tableau= None







#########################################################


#########################################################
#définition des fonctions 

def quadrillage():
    """Affiche un quadrillage constitué de rectangle de largeur LARGEUR et de longueur HAUTEUR"""
    canvas.create_rectangle((0,3*HAUTEUR+2),(LARGEUR_C,4*HAUTEUR+2),fill="blue")
    y = 2
    while y <= 8*HAUTEUR:
        canvas.create_line((0, y), (30*LARGEUR+2, y), fill=COULEUR_QUADR)
        y += HAUTEUR
    x = 2 
    while x <= 31*LARGEUR:
        canvas.create_line((x, 0), (x, 7*HAUTEUR+2), fill=COULEUR_QUADR)
        x += LARGEUR

def xy_to_ij(x, y):
    """Retourne la colonne et la ligne du tableau correspondant
       aux coordonnées (x,y) du canevas"""
    return x // HAUTEUR, y // LARGEUR

 #########################################################

#########################################################
#programme principal

racine = tk.Tk()
racine.title("Automate Avion")



# création des widgets
canvas = tk.Canvas(racine,width=LARGEUR_C,height=HAUTEUR_C,bg="white")
lbl_entrée = tk.Label(racine, text="ENTREE")

# positionnement
canvas.grid(rowspan=7)
lbl_entrée.grid(column=1,row=3)
# autres fonctions
quadrillage()


# boucle principal
racine.mainloop()
########################################################



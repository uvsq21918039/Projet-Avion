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
<<<<<<< HEAD
#########################################################
# import des librairies
import tkinter as tk 
########################################################


#########################################################
#définition des constantes

LARGEUR=45
HAUTEUR=30
COULEUR_FOND ="white"
COULEUR_PLACE_LIBRE="green"
COULEUR_PLACE_OCCUPE="red"

#########################################################

#########################################################
#définition des variables globales








#########################################################


#########################################################
#définition des fonctions 

def quadrillage():
    """Affiche un quadrillage constitué de carrés de côté COTE_PARCELLE"""
    y = 2
    while y < 8*HAUTEUR:
        canvas.create_line((2, y), (30*LARGEUR, y), fill="black")
        y += HAUTEUR
    x = 2 
    while x < 31*LARGEUR:
        canvas.create_line((x, 0), (x, 7*HAUTEUR), fill="black")
        x += LARGEUR
 #########################################################

#########################################################
#programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine,width=30*LARGEUR,height=7*HAUTEUR,bg=COULEUR_FOND)
canvas.grid()

quadrillage()
racine.mainloop()
########################################################
=======
import tkinter as tk

racine = tk.Tk()
canvas = tk.Canvas(racine, bg='green', height=1400, width=630)
canvas.grid()

racine.mainloop()

>>>>>>> 8d330a91c69383478cc6086eebc6ba252a6562fc

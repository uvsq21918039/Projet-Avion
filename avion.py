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



import tkinter as tk
import random as rd


#########################################################
#définition des constantes
COTE = 40
HAUTEUR = 7*COTE  #7 lignes
LARGEUR = 30*COTE  #30 colonnes
#########################################################


#########################################################
#définition des variables globales
passager = []           #Liste contenant les informations du passagers(colonne actuelle, ligne actuelle, colonne de destination , ligne de destination, nombre de bagages)
couloir = []            #Liste qui decrit les cellules du couloir [colonne, ligne]
siege_libre = []        #Liste qui contient les places libres [colonne, ligne]
#########################################################


#########################################################
#définiton des fonctions
def quadrillage():
    """Création des cellules de l'avionet des listes siege_libre """
    global siege_libre, couloir
    for i in range(1, LARGEUR, COTE):
        for j in range(1, HAUTEUR, COTE):
            if j == HAUTEUR/2 - COTE/2 + 1:
                couloir.append([i // COTE, j // COTE])
                canvas.create_rectangle(i, j, i+COTE, j+COTE, fill="grey")
            else:
                canvas.create_rectangle(i, j, i+COTE, j+COTE, fill="white")
                siege_libre.append([i // COTE, j // COTE])


def couleur_siege():
    """Fonction qui définie la couleur des cellules en fonction de la place et du nombre de bagages"""
    for c in passager:
        if c[4] > 0:
        #si le passager a des bagages    
            canvas.create_rectangle(c[0] * COTE + 1, c[1] * COTE + 1 , c[0] * COTE + 1 +COTE, c[1] * COTE + 1 +COTE, fill="yellow")               
        elif c[0] == c[2] and c[1] == c[3]:
        #si le passager est assis a son siège
            canvas.create_rectangle(c[0] * COTE + 1, c[1] * COTE + 1 , c[0] * COTE + 1 +COTE, c[1] * COTE + 1 +COTE, fill="red")
        elif c[4] == 0:
        #si le passager n'a pas de bagages     
            canvas.create_rectangle(c[0] * COTE + 1, c[1] * COTE + 1 , c[0] * COTE + 1 +COTE, c[1] * COTE + 1 +COTE, fill="green")                


def genere_passager():
    """Fonction qui génère les passagers à l'entrée de l'avion"""
    global passager, siege_libre
    if siege_libre:
        for c in passager:
            if c[0] != 0 and c[1] == 3:   
            #si l'entrée est libre        
                siege_attribue = rd.choice(siege_libre)
                siege_libre.remove(siege_attribue)
                passager.append([0, 3, siege_attribue[0], siege_attribue[1], rd.randint(0, 2)])
            

def nouvelle_etape():
    """Fonction qui effectue une étape de l'automate pour chaque cellule"""
    global passager, siege_libre
    if passager:
        move()
        genere_passager() 
    else:
        siege_attribue = rd.choice(siege_libre)
        siege_libre.remove(siege_attribue)
        passager.append([0, 3, siege_attribue[0], siege_attribue[1], rd.randint(0, 2)])


def move():
    """Fonction qui permet de bouger les passagers dans l'avion en fonction des voisins"""
    global passager
    for el in passager:
        if el[0] == el[2]:
        #si la colonne du siège est atteinte    
            if el[4] > 0:
            #si le passager a des bagages    
                el[4] -= 1
            else:
            #si le passager n'a plus de bagage    
                if el[1] > el[3]:
                #si le siège du passager se situe sur la partie supérieure de l'avion    
                    el[1] -= 1
                    for k in passager:
                        if el[0:2] == k[0:2] and k[1] != k[3] and k != el:
                            el[1] -= 1
                            break
                        elif el[0:2] == k[0:2] and k[1] == k[3] and k != el:
                            k[1] -= 1
                            break
                elif el[1] < el[3]:
                #si le siège du passager se situe sur la partie inférieure de l'avion    
                    el[1] += 1
                    for k in passager:
                        if el[0:2] == k[0:2] and k[1] != k[3] and k != el:
                            el[1] += 1
                            break
                        elif el[0:2] == k[0:2] and k[1] == k[3] and k != el:
                            k[1] += 1
                            break
        elif el[0] != el[2]:
        #si la colonne du siège n'est pas atteinte    
            mouvement = True
            for k in passager:
                if k[1] == 3 and el[0] + 1 == k[0]:
                    mouvement = False
                    break
            if mouvement == True:
                el[0] += 1 
   

def demarrer():
    """Fonction qui permet de lancer le programme"""
    quadrillage()
    couleur_siege()
    nouvelle_etape()
    canvas.after(100, demarrer)
#########################################################          


#########################################################
#programme pricipal
racine = tk.Tk()
racine.title("Automate simulant le déplacement des passagers dans un avion")
#création des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="black")
Bouton_demarrer = tk.Button(racine, text = "DEMARRER", command = demarrer)
lbl_entrée = tk.Label(racine, text="ENTREE")

#positionnement des widgets
canvas.grid(row = 2, column=1,columnspan = 3)
Bouton_demarrer.grid(row = 2, column = 4)
lbl_entrée.grid(column=0,row=2)


racine.mainloop()


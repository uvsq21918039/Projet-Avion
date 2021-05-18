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
tableau = None 
passager=["Voici la liste des passagers: "]
siege = ["siège"]
delai = 500
val = 0
#########################################################


#########################################################
#définition des fonctions 
def quadrillage():
    """Création des cellules de l'avion"""
    for i in range (30):
        for j in range (7):
            cellule = canvas.create_rectangle(i*LARGEUR, j*HAUTEUR, (1+i)*LARGEUR, (1+j)*HAUTEUR, fill = COULEUR_FOND, outline=COULEUR_QUADR)
            siege.append(cellule)
    print(siege)           


def generateur_liste_passager():
    """Génère une liste contenant les informations de chaque passager (numéro, ligne ,colonne, bagage)"""
    for i in range (1,181): 
        passager.append ([i, rd.randint(1,7), rd.randint(1,30), rd.randint(0,2)])
    for elem in passager :
        print(elem)


def entree_avion():
    """Génere les passagers à l'entrée de l'avion et determine leur couleur en fonction des bagages"""
    global tableau
    for i in range(1, 181):
        #si l'entrée est libre
        if tableau[4][0] == 4:
            #si le passager n'a pas de bagages  
            if passager[i][3] == 0:
                tableau[4][0]= PASSAGER_DEBOUT_SANS_BAGAGE # = 1
            #si le passager a des bagages
            else :
                tableau[4][0]= PASSAGER_DEBOUT_AVEC_BAGAGE  # = 2  
    

def couleur_cellule():
    for i in range (NB_LIGN):
        for j in range(NB_COL):
                if tableau[i][j] == 0 : 
                    canvas.itemconfig(siege[((i+1)+(j*7))], fill=COULEUR_FOND) #cellule vide
                elif tableau [i][j] == 1:
                    canvas.itemconfig(siege[((i+1)+(j*7))], fill=PASSAGER_DEBOUT_SANS_BAGAGE) #cellule avec passager debout sans bagage
                elif tableau[i][j] == 2 : 
                    canvas.itemconfig(siege[((i+1)+(j*7))], fill=COULEUR_PASS_DEBOUT_AVEC_BAGAGE) #cellule avec passager debout avec bagage
                elif tableau[i][j] == 3:
                    canvas.itemconfig(siege[((i+1)+(j*7))], fill=COULEUR_PASS_ASSIS) #cellule avec passager assis
                else :
                    canvas.itemconfig(siege[((i+1)+(j*7))], fill=COULEUR_COULOIR) #cellule du couloir
 

def deplacement_passager():
    for i in range (NB_COL):
        for j in range(1,181):
            if i < passager[j][2] :
           #si la colonne du siege du passager j n'est pas atteinte
                if tableau[4][i+1] == 0 :
                #si la cellule devant est libre
                    tableau[4][i+1] = int(tableau[4][i])
                    tableau[4][i] = 0
            elif i == passager[j][2]:
            #si la colonne du siege du passager j est atteinte  
                if tableau[4][i] == 2 : 
                #si le passager a des bagages    
                    if passager[j][3] > 0 :
                        passager[j][3] -= 1
                    else : 
                        tableau[4][i] = 1
                        #le passager n'a plus de bagages
                        for n in range(NB_LIGN):
                            if n != passager[j][1]:
                                if passager[j][1] > 4 :
                                    tableau[n+1][i] = 1
                                    tableau[n-1][i] =0
                                else : 
                                    tableau[n-1][i] = 1
                                    tableau[n+1][i] = 0
                            else :
                            #si le passager a atteint son siege
                                tableau[n][i] = 3              

                             
def etape():
    """Fait une étape de l'automate en modifiant la variable globale tableau """
    global tableau
    tableau_res = copy.deepcopy(tableau)
    for i in range(NB_COL):
        for j in range(NB_LIG):
            tableau_res[i][j] = deplacement_passager()
    tableau = tableau_res

def etape_n(event):
    """Appelle la fonction etape sans argument"""
    etape()


def start():
    """Démarre l'automate"""
    global id_after
    etape()
    id_after = racine.after(delai, start)


def start_stop():
    """Démarre ou arrête l'automate et change le nom du bouton"""
    global val
    if val == 0:
        bout_start_stop.config(text="arrêter")
        start()
    else:
        bout_start_stop.config(text="démarrer")
        racine.after_cancel(id_after)
    val = 1 - val




########################
# programme principal

tableau = []
for i in range(NB_LIGN):
    if i == 3 :
        tableau.append([4]*NB_COL)   
    else :    
        tableau.append([0]*NB_COL)   
print(tableau)

racine = tk.Tk()
racine.title("Automate Avion")



# création des widgets
canvas = tk.Canvas(racine,width=LARGEUR_C,height=HAUTEUR_C,bg="white")
lbl_entrée = tk.Label(racine, text="ENTREE")
bout_start_stop = tk.Button(racine, text="démarrer", command=start_stop)

# positionnement
canvas.grid(column=1,rowspan=7)
lbl_entrée.grid(column=0,row=3)
bout_start_stop.grid(column=2, row=1)
# autres fonctions
quadrillage()
generateur_liste_passager()
couleur_cellule()
entree_avion()


# boucle principal
racine.mainloop()
########################################################                    
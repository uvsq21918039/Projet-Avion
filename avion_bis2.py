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
import copy
########################################################


#########################################################
#définition des constantes

LARGEUR=40
HAUTEUR=60
LARGEUR_CAN=LARGEUR*30
HAUTEUR_CAN= HAUTEUR*7
NB_COL=30
NB_LIGN=7
COULEUR_QUADR = "black"
COULEUR_SIEGE ="white"
COULEUR_COULOIR ="grey60"
DEBOUT_SANS_BAGAGE ="green"
DEBOUT_AVEC_BAGAGE = "yellow"
PASS_ASSIS="red"
PASSAGER_DEBOUT_SANS_BAGAGE = 1
PASSAGER_DEBOUT_AVEC_BAGAGE = 2
PASSAGER_ASSIS = 3
#########################################################

#########################################################
#définition des variables globales
tableau = None 
passager=[]#contient les informations des passagers(ligne, colonne, nombre de bagages) 
siege_libre= []#contient tous les sièges qui n'ont pas été encore attitrés aux passagers
coords=[]#contient les coordonnées du passager en temps réel (x,y)
delai = 500
val = 0
color = None
#########################################################

tableau = []
for i in range(NB_LIGN):
    if i == 3 :
        tableau.append([4]*NB_COL)   
    else :    
        tableau.append([0]*NB_COL) 
print(tableau)
#########################################################
#définition des fonctions 
def quadrillage():
    """Création des cellules de l'avion"""
    for l in range (2, LARGEUR_CAN, LARGEUR):
        for h in range (2, HAUTEUR_CAN, HAUTEUR):
            x = l+LARGEUR-2
            y = h+HAUTEUR-2
            if h == 3*HAUTEUR+2: 
                cellule = canvas.create_rectangle(l, h, x, y, fill = COULEUR_COULOIR, outline=COULEUR_QUADR)
            else : 
                cellule = canvas.create_rectangle(l, h, x, y, fill = COULEUR_SIEGE, outline=COULEUR_QUADR)
                siege_libre.append([h // HAUTEUR, l //LARGEUR])
    print(siege_libre)    


def generateur_passager():
    """Génère les passagers à l'entrée de l'avion ainsi qu'une liste de passager sous la forme(ligne, colonne, bagage)"""
    global passager, siege_libre, tableau
    if siege_libre :
        if tableau[3][0] == 4 :
            siege_attribue = rd.choice(siege_libre)
            siege_libre.remove(siege_attribue)    
            passager.append([siege_attribue[0], siege_attribue[1], rd.randint(0, 2)])
            coords.append([3, 0])
            for elem in passager :
                if elem[2] == 0 :
                    tableau[3][0] = 1
                else :
                    tableau[3][0] = 2   
        print(passager)
        print(coords)


def creer_forme_passager():
    for i in range (NB_LIGN):
        for j in range(NB_COL):
            for c in coords:
                if tableau [i][j] == 1:
                    canvas.create_oval(c[1] *LARGEUR, c[0] *HAUTEUR , c[1] *LARGEUR + LARGEUR, c[0]*HAUTEUR+HAUTEUR, fill= "red")
                elif tableau[i][j] == 2 : 
                    canvas.create_oval(c[1] *LARGEUR, c[0] *HAUTEUR , c[1] *LARGEUR + LARGEUR, c[0]*HAUTEUR+HAUTEUR, fill= "green")
                elif tableau[i][j] == 3:
                    canvas.create_oval(c[1] *LARGEUR, c[0] *HAUTEUR , c[1] *LARGEUR + LARGEUR, c[0]*HAUTEUR+HAUTEUR, fill= "orange")
                else: 
                    canvas.delete()


def voisin_droite():
    """Retourne si la case à droite de la case de coordonnées (coords[0], coords[1]) est occupée"""
    cpt_1 = 0
    for i in coords : 
        if tableau[3][i[1]+1] != 4 :   
            cpt_1 += 1
    return cpt_1        


def voisin_vertical():
    """Retourne si la case en haut ou en bas de la case de coordonnées (coords[0], coords[1])  est occupée"""
    cpt_2 = 0
    for i in coords :
        if i[0] > 3 : 
            if tableau[i[0]+1][i[1]] != 0 :   
                cpt_2 += 1
        elif i[0] < 3 :            
            if tableau[i[0]-1][i[1]] != 0 :   
                cpt_2 += 1          
    return cpt_2        
        

def deplace_passager():
    global passager , tableau
    for j in coords :
        n = voisin_droite()
        m = voisin_vertical()
        for i in passager:
                if j[1] != i[1]:
                #si la colonne  n'est pas atteinte
                    if n == 0 :
                        j[1] += 1
                        if i[2] == 0 :
                            tableau[j[0]][j[1]] = PASSAGER_DEBOUT_SANS_BAGAGE
                            tableau[j[0]][j[1]-1] = 4
                        else :
                            tableau[j[0]][j[1]] = PASSAGER_DEBOUT_AVEC_BAGAGE
                            tableau[j[0]][j[1]-1] = 4

                elif j[1] == i[1]:
                #si la colonne est atteinte
                    if i[2] > 0:
                    #si le passager a des bagages
                        i[2] -= 1
                    else:
                    #si le passager n'a plus de bagages   
                        if j[0] < i[0]:
                        #si le siège du passager se situe sur la partie supérieure de l'avion     
                            
                            if m == 0 :
                                if j[0] != i[0] :
                                #si la ligne n'est pas atteinte    
                                    j[1] += 1
                                    tableau[j[0]][j[1]] = DEBOUT_SANS_BAGAGE   
                                else :
                                #si la ligne est atteinte    
                                    tableau[j[0]][j[1]] = PASS_ASSIS  
                                tableau[j[0]-1][j[1]] =0      
                            
                            elif m == 1 :
                                tableau[(j[0]+1)][(j[1])] == DEBOUT_SANS_BAGAGE 
                                j[1] += 1
                                tableau[j[0]][j[1]] = PASS_ASSIS
                                tableau[j[0]-1][j[1]] =0 
                        elif j[1] > i[1]:
                        #si le siège du passager se situe sur la partie inférieure de l'avion    
                            if m == 0 :
                                if j[0] != i[0] :
                                #si la ligne n'est pas atteinte    
                                    j[0] -= 1
                                    tableau[(j[0])][(j[1])] = DEBOUT_SANS_BAGAGE   
                                else :
                                #si la ligne est atteinte    
                                    tableau[(j[0])][(j[1])] = PASS_ASSIS  
                                tableau[j[0]+1][(j[1])] =0   





def etape():
    "Effectue une etape de l'automate"
    global tableau
    tableau_res = copy.deepcopy(tableau)
    generateur_passager()
    creer_forme_passager()
    for i in range(NB_LIGN):
        for j in range(NB_COL):
            tableau_res[i][j] = deplace_passager()
    tableau = tableau_res


def start():
    """Démarre l'automate"""
    global id_after
    etape()
    id_after = racine.after(delai, start)


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
canvas = tk.Canvas(racine,width=LARGEUR_CAN,height=HAUTEUR_CAN,bg="white")
bout_start_stop = tk.Button(racine, text="démarrer", command=start)
# positionnement
canvas.grid(column=1,rowspan=7)
bout_start_stop.grid(column=2, row=2)
# autres fonctions
quadrillage()
#generateur_passager()
#creer_forme_passager()
print(tableau)


# boucle principal
racine.mainloop()
########################################################                    
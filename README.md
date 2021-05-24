# Projet-Avion
# Introduction 
Ce projet aura pour but de créer un plan d'avion et de réguler les passagers avec leurs numéros de sièges correspondants ainsi que la prise en charge du rangement de leurs bagages.
# Modèle
On pose le cadre général qui est de répresenter la géographie d'un problème spatio-temporel par un réseau de cellules 
dont l'état change au cours du temps en fonction de règles simples codant le problème. Nous allons le modéliser par un avion mono-couloir avec 3 sièges de chaque coté du couloir, ce qui nous donne 6 rangées au total.
# But du programme
Les passagers embarquent à un point d'apparition au début du couloir pour ensuite se diriger vers leur siège attribué.
Chaque passager à une destination soit un siège attribué par des coordonnées ainsi que des bagages représenté par les valeur 0 à 2 qu'ils devront déposer obligatoirement dans les coffres à bagages situé dans le couloir avant d'aller s'asseoir.

# Utilisation 

- Le programme va s'ouvrir sur le plan de l'avion vide.
- Un bouton " Démarrer " est disposé à droite pour pouvoir ainsi démarrer le programme.
- A l'issu du déclenchement du bouton démarrer le programme s'éxécute et fait apparaitre les passagers automatiquement.
- Le programme est automatique et il s'arrête au moment où tous les passagers seront assis à leurs sièges respectifs.
- Les passagers en rouge désigne les passagers qui n'ont pas compléter leurs tâches (déposer leurs bagages et/ou rejoindre leurs sièges).
- Les passagers en orange désigne ceux qui ont rangés leurs bagages mais qui ne sont pas encore à leurs places.
- Les passagers en vert ceux qui ont finis de rangé leurs bagages et qui sont assis à leurs places correspondantes.
- Quand tous les passagers sont afficher en oranger alors le programme est terminé.

# Les Problèmes rencontrés

- A l'éxécution de notre programme, les passages ne se déplacent pas comme prévu et reste fixe bien que les fonctions marchent individuellement.


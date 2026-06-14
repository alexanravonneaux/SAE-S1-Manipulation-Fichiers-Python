# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from random import randrange # import d’un module aléa

nombreDesix = 0
n = int(input("Combien de lancé de dé ? "))
for i in range(n):
    faceObtenue = randrange(1,7) # aléa entre 1 et 6
    if faceObtenue == 6 :
        nombreDesix = nombreDesix + 1
print("Nombre de ‘6’ : " + str(nombreDesix))
proba = nombreDesix / n

print("Pour"+str(n)+" lancers, la probabilité de l'événement obtenir le 6 est égale à"+str(proba))
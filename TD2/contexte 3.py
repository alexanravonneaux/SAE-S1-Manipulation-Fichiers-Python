# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

distance = int(input("distance ?"))
volume = float(input("Volume ?(en m3)"))
poids = int(input("Poids ?"))

base = 50
if poids >= 60 :
    base = base + (poids - 60)
    
if volume >= 1 :
    base = base + 20
    
if distance >= 100 :
    base = base + ((distance - 100)*0.5)

print("le coût total de la livraison est de " + str(base) + "euros")
    
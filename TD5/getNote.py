# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def GetNote (sexe : str, distance : float) -> float:
    if sexe == "fille" :
        note = 3 * distance - 8.5
    if sexe == "garçon" :
        note = 2.57 * distance - 8.28
    
    if note < 0:
        note = 0
    elif note > 0 :
        note = 20
    
    return round (note,2)

def arrondiDemiPointSup (note : float) -> float():
    note = (note * 2) / 2 
    if note % 0.5 != 0 :
        note = (note * 2) / 2 
    else :
        note
    return round(note)

nbeleve = int(input("Nombres d'élèves : "))
for i in range(1,nbeleve+1):
    sexe = input("sexe de l'élève n°"+ str[i] + '(F ou G) :')
    distance = float(input("Distance en m réalisés par l'élève n°"+ str[i] +":"))
    sommeNote += GetNote (sexe, distance)
    
print("moyenne :"+ str(round(sommeNote/nbeleve),2))
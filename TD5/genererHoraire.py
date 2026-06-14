# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:50:31 2024

@author: fgarni04
"""

def ajouterDuree(lHoraire : str, laDuree : int) -> str:
    
    # Reécupérer les heures et les minutes en entier
    heures = int(lHoraire[:2])
    minutes = int(lHoraire[3:])
    
    minutes += laDuree
    
    if minutes >= 60:
        heures += 1     # heures = heures + 1
        minutes -= 60  # minutes = minutes - 60
    
    if heures == 24:
        heures = 0
    
    if heures < 10:
        heures = "0" + str(heures)
    else:
        heures = str(heures)
        
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)
    
    h = heures + "h" + minutes
    return h

# Prg ppal
n = int(input("Combien de créneaux ?"))
h = "08h00"
for i in range(n):
    print(ajouterDuree(h,15))
    h = ajouterDuree(h,15)


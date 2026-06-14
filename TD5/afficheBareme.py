# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:19:34 2024

@author: fgarni04
"""

def getPrix(leNbJours : int) -> int:
    tarif1 = 13
    tarif2 = 43
    tarif3 = 64
    
    if leNbJours <= 7 :
        prix = tarif1 + (leNbJours-1) * 5
    elif leNbJours <= 14:
        prix = tarif2 + (leNbJours-7) * 3
    else:
        prix = tarif3 + (leNbJours-14) * 2
        
    return prix

# Prg ppal
for i in range(1,31):
    print("Jour(s) n°" + str(i) + " - Prix : " + str(getPrix(i)))



# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:54:10 2024

@author: aravonne
"""
salaireAn = int(input("Quelles est votre salaire annuel ? "))
fraisreel = int(input("Quelles est le montant de vos frais reels ? "))

RBGF = salaireAn -(salaireAn * 0.1)

RBGR = salaireAn - fraisreel
if RBGF > RBGR : 
    print ("La méthode la plus avantageuse est celle des frais reels avec un montant de " + str(RBGR) + "euros plutot que " + str(RBGF) + "euros avec la déduction forfaitaire")
else : 
    print ("La méthode la plus avantageuse est celle de la déduction forfaitaire avec un montant de " + str(RBGF) + "euros plutot que " + str(RBGR) + "euros avec les frais reels")
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:47:35 2025

@author: aravonne
"""

def saisieResultat (nomEq1: str, buteurEq1 : list, nomEq2 : str, buteurEq2 : list) :
    
    if len(buteurEq1) > len(buteurEq2) :
        futsal[nomEq1][0] += 3
    elif len(buteurEq1) < len(buteurEq2):
        futsal[nomEq2][0] += 3
    else : 
        futsal[nomEq1][0] += 1
        futsal[nomEq2][0] += 1
        
    nbkb = int(input("Nombre de match à saisir :"))
    
    for i in range (1, nbkb +1) :
        nomEq1 = input("Match n°"+ str(i) +" - équipe 1 : ")
        nomEq2 = input("Match n°"+ str(i) +" - équipe 2 : ")
    
    res = str(input("Score dans l'ordre de la saisie : "))
    
    but1 = int(res[0])
    but2 = int(res[2])
    
    listebuteureq1 =[]
    
    for i in range(1, but1) :
        buteurEq1 = str(input("Buteur n°"+str(i)+" - équipe 1 : "))
    for i in range (1,but2) :
        buteurEq2 = str(input("Buteur n°2 - équipe 1 : "))
    
    
    
    

    
futsal = {"profs" : [0,"bureau", 0, "Garnier", 0, "Ibazizou", 0, "" ]}
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:40:07 2024

@author: aravonne
"""

from random import randrange
a=0
nombre = randrange(1, 101)
nbdmd = float(input("Donnez un nombre entre 1 et 100 : "))


while nbdmd != nombre:  # Continue tant que le nombre deviné n'est pas le bon
    if nbdmd < nombre:
        print("Votre nombre est inférieur au nombre mystère.")
    else:
        print("Votre nombre est supérieur au nombre mystère.")
    
    nbdmd = int(input("Redonnez un nombre entre 1 et 100 : "))
    a+=1

# Lorsque la boucle se termine, cela signifie que le nombre a été trouvé
print("Le nombre mystère est " + str(nombre))
print("Le nombre de tentative est de " + str(a))

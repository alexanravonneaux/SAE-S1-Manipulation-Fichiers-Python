# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from turtle import *
from random import randrange
speed(10) # vitesse de déplacement de la tortue, ici au
# minimum (= 1). Le max est la valeur 0
rayon = int(input("rayon ?"))
penup()
goto(0,-rayon)
pendown()
circle(rayon)
penup()
goto(0,0)
pendown()
while xcor()* xcor() + ycor()* ycor() < rayon*rayon : 
    setheading(randrange(1,350))
    forward(10)

mainloop()

from turtle import *

def carre(taille, couleur):
    "fonction qui dessine un carré de taille et de couleur déterminé"
    color(couleur)
    c= 0
    while c<4:
        forward(taille)
        right(90)
        c = c+1

carre(100, "green")
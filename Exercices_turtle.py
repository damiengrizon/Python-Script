# TURTLE :
'''
from turtle import *
forward(120)
left(90)
color('red')
forward(80)

reset()
a=0
while a<12:
    a=a+1
    forward(150)
    left(150)
'''
'''
reset() - on efface tout et on recommence
goto(x, y) - Aller à l'endroit des coordonnées x,y
forward(distance) - avancer d'une distance données
backward(distance)
up()
down()
color(couleur)
left()
right()
with(épaisseur)
fill(1) -  rempli un contour fermé à l'aide de la couleur selectionnée
write(texte) - texte -> doit être une chaine de caractère
'''
'''
reset()
write("coucou")
'''

# Dessiner grace à une fonction une série de triangle équilatéraux d'une couleur bien déterminé ( il doit donc y avoir un paramètre dans la fonction qui détermine la couleur du triangle)

# Utiliser ensuite cette fonction pour reproduire ce même triangle  en différents endroits, en changeant de couleur à chaque fois

'''
liste_couleurs = ['black', 'red', 'white','green','yellow', 'blue', 'purple']


from random import randint
from turtle import *
reset()
speed(1)

def triangle(color, positionX, positionY):
    up()
    goto(positionX,positionY)
    down()
    fillcolor(color)
    begin_fill()
    for i in range(0,3):
        forward(120)
        left(120)
    end_fill()
    up()

i = 0
while i < 800:
    triangle(liste_couleurs[randint(0, 6)],randint(-300,300),randint(-400,400))
    i += 10
'''
# ajout d'une fonction qui va tracer des carrés en ligne à la suite des uns des autres
'''
from turtle import *
reset()
speed(10)

def carre(taille, nombreCarre):
    up()
    posX = -300
    goto(posX,0)
    down()
    while nombreCarre > 0 :
        down()
        for i in range(0,4):
            forward(taille)
            left(90)
        up()
        posX += 50
        goto(posX, 0)
        nombreCarre = nombreCarre -1

carre(40, 10)
done()
'''

# Ajout d'une fonction qui permet de tracer des étoiles à 5 branches:
#def etoil5():


from turtle import *
reset()
speed(10)
tailleEtoile = 30
nombreEtoile = 9

def etoile(taille, angle=0):
    right(angle)
    down()
    for i in range(0,5):
        right(144)
        forward(taille)
    up()

'''
def dessinePlusieurs(objet, nombreObjet):
    up()
    posX = -300
    goto(posX,0)
    down()
    while nombreObjet > 0 :
        for i in range(0,5):
            tailleEtoile = tailleEtoile + 10
        for i in range(0,4):
            tailleEtoile = tailleEtoile - 10

        posX += 80
        goto(posX, 0)
        nombreObjet = nombreObjet -1
'''
while nombreEtoile > 0 :
    for i in range(0,5):
        tailleEtoile = tailleEtoile + 10
        etoile(tailleEtoile)
        nombreEtoile = nombreEtoile -1
        forward(100)
    for i in range(0,4):
        tailleEtoile = tailleEtoile - 10
        etoile(tailleEtoile) 
        nombreEtoile = nombreEtoile -1
        forward(100)
done()


# ajout d'une fonction qui dessine des triantgles et des carrés à la suite des uns des autres:
'''
from turtle import *
    # initialisation des paramètres et de la position du curseur 
reset()
speed(10)
up()
goto(0,-200)

def carre(taille, angle):
    left(angle)
    for i in range(0,4):
        down()
        forward(taille)
        left(90)
        up()

def triangle(taille, couleur, angle):
    left(angle)
    fillcolor(couleur)
    begin_fill()
    for i in range(0,3):
        down()
        forward(taille)
        left(120)
        up()
    end_fill()


for i in range(0,1000,100):
    carre(80,20)
    up()
    forward(100)
    triangle(80, "red", 20 )
    up()
    forward(100)
done()
'''
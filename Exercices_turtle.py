# TURTLE :
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
reset()
write("coucou")
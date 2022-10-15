from turtle import *


def carre(taille, couleur):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    up()
    speed(1)
    color(couleur)
    c = 0 
    down()
    while c<4:
        forward(taille)
        right (90)
        c +=1
    done()
    



for i in range(10):
    position = (i +10)
    print(position)
 #   goto(position, 0)
 #   careRed = carre(25, "red")
    





# la procédure ci-dessous imprime une sorte de rosace et la rempli


from turtle import *
'''
turtle.speed(10)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''
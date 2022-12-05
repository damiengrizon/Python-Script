from tkinter import *

def drawcircle():
    # global x1, y1, x2, y2  # coordonnées de la ligne
    x1, y1, x2, y2 = 10, 200, 210, 400  
    "tracé d'un cercle dans le canevas can1"
    can1.create_oval([x1, y1, x2, y2], width = 1, outline='green')

def olympiqueRing():
    x1, y1, x2, y2 = 10, 200, 210, 400  
    x3, y3, x4, y4 = 110, 100, 310, 300
    couleur = ['red', 'blue', 'black', 'green','pink', 'yellow', 'purple']

    nbre_cercle = 7
    while 7 >= nbre_cercle >= 4:
        coul = couleur[nbre_cercle-1]
        can1.create_oval([x1, y1, x2, y2], width = 2, outline = coul)
        x1, x2 = x1 +200, x2 +200
        print(f"numéro du cercle {nbre_cercle} x: {x1, y1, x2, y2}")
        print(coul)
        nbre_cercle -= 1

    while 3 >= nbre_cercle > 0:
        coul = couleur[nbre_cercle-1]
        can1.create_oval([x3, y3, x4, y4 ], width = 2, outline = coul)  
        x3, x4 = x3 +200, x4 +200
        print(f"numéro du cercle {nbre_cercle} {x3, y3, x4, y4}")
        print(coul)
        nbre_cercle -= 1

def circleOne(cercle):
    x1, y1, x2, y2 = 10, 200, 210, 400  
    x3, y3, x4, y4 = 110, 100, 310, 300
    couleur = ['red', 'blue', 'black', 'green','pink', 'yellow', 'purple']

    if 4 <= cercle <= 7:
        coul = couleur[cercle-1]
        x1, x2 = x1 +200*(7-cercle), x2 +200*(7-cercle)
        can1.create_oval([x1, y1, x2, y2], width = 2, outline = coul)
        print(f"numéro du cercle {cercle} x: {x1, y1, x2, y2}")

    if 3 >= cercle > 0:
        coul = couleur[cercle-2]
        x3, x4 = x3 +200*(cercle -1), x4 +200*(cercle -1)
        can1.create_oval([x3, y3, x4, y4 ], width = 2, outline = coul)  
        print(f"numéro du cercle {cercle} {x3, y3, x4, y4}")        

fen1 = Tk()

# création des widgets "esclaves" :
can1 = Canvas(fen1, bg = 'white', height=500, width=820)
can1.pack(side=LEFT)
bou1 = Button(fen1, text="quitter", command = fen1.quit)
bou1.pack(side = BOTTOM)
bou2 = Button(fen1, text="Tracer un cercle", command = drawcircle)
bou2.pack()
bou3 = Button(fen1, text="Tracer les anneaux", command = olympiqueRing)
bou3.pack()
bou4 = Button(fen1, text="Tracer 1", command = lambda  : circleOne(1))
bou4.pack()
bou5 = Button(fen1, text="Tracer 2", command = lambda  : circleOne(2))
bou5.pack()
bou6 = Button(fen1, text="Tracer 3", command = lambda  : circleOne(3))
bou6.pack()
bou7 = Button(fen1, text="Tracer 4", command = lambda  : circleOne(4))
bou7.pack()
bou8 = Button(fen1, text="Tracer 5", command = lambda  : circleOne(5))
bou8.pack()
bou9 = Button(fen1, text="Tracer 6", command = lambda  : circleOne(6))
bou9.pack()
bou10 = Button(fen1, text="Tracer 7", command = lambda  : circleOne(7))
bou10.pack()
fen1.mainloop() # démarrage du réceptionnaire d'évènement
fen1.destroy() # destruction fermeture de la fenetre
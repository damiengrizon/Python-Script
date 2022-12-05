
# B / Modifier le programme ci-dessous en y ajoutant 5 bouttons. Chacun de ces bouttons provoquera le tracé de chacun des anneaux.
from tkinter import *

# fonction qui doit tracer un cercle avec create_oval

def drawcircle():
    # global x1, y1, x2, y2  # coordonnées de la ligne
    x1, y1, x2, y2 = 10, 200, 210, 400  
    "tracé d'un cercle dans le canevas can1"
    can1.create_oval([x1, y1, x2, y2], width = 1, outline='green')

def olympiqueRing():
    x1, y1, x2, y2 = 10, 200, 210, 400  
    x3, y3, x4, y4 = 110, 100, 310, 300
    couleur = ['red', 'blue', 'black', 'green','pink']

    nbre_cercle = 5

    while 5 >= nbre_cercle >= 3:
        coul = couleur[nbre_cercle-1]
        can1.create_oval([x1, y1, x2, y2], width = 2, outline = coul)
        x1, x2 = x1 +200, x2 +200
        print(coul)
        nbre_cercle -= 1

    while 3 >= nbre_cercle > 0:
        can1.create_oval([x3, y3, x4, y4 ], width = 2, outline = coul)  
        x3, x4 = x3 +200, x4 +200
        coul = couleur[nbre_cercle-2]
        print(coul)
        nbre_cercle -= 1

def draw_one_olymp_circle(nbrcercle):
    pass

#------ Progamme principal ------

# création du widget principal ("maître") :

fen1 = Tk()


# création des widgets "esclaves" :
can1 = Canvas(fen1, bg = 'white', height=500, width=820)
can1.pack(side=LEFT)
bou1 = Button(fen1, text="quitter", command = fen1.quit)
bou1.pack(side = BOTTOM)
bou2 = Button(fen1, text="Tracer un cercle", command = drawcircle)
bou2.pack()
bou3 = Button(fen1, text="Tracer cercle 1", command = draw_one_olymp_circle(1)).pack(side =LEFT)
bou4 = Button(fen1, text="Tracer cercle 2", command = draw_one_olymp_circle(2))
bou4.pack()
bou5 = Button(fen1, text="Tracer cercle 3", command = draw_one_olymp_circle(3))
bou5.pack()
bou6 = Button(fen1, text="Tracer cercle 4", command = draw_one_olymp_circle(4))
bou6.pack()
bou7 = Button(fen1, text="Tracer cercle 5", command = draw_one_olymp_circle(5))
bou7.pack()
bou6 = Button(fen1, text="Tracer tous les anneaux", command = olympiqueRing)
bou6.pack()
fen1.mainloop() # démarrage du réceptionnaire d'évènement
fen1.destroy() # destruction fermeture de la fenetre

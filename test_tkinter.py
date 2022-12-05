# ouvre une fenetre avec un texte en rouge puis un boutton pour la fermer
'''
from tkinter import *
fen1 = Tk()
tex1 = Label(fen1, text = 'bonjour tout le monde ! ', fg = 'red')
# tex1.pack()
bou1 = Button(text='quitter', command = fen1.destroy)
# bou1.pack()
fen1.mainloop()
'''

# Exercice sur TKinter en version original
'''
# Petit exercice utilisant la bibliothèque graphique tkinter
from tkinter import * 
from random import randrange

# --- définition  des fonctions gestionnaires d'évènement : ---
def drawline():
    "tracéd'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2, width = 1, fill = coul)

    # modification des coordonnées pour la ligne suivante :
    y1, y2 = y1+5, y2 +5

def changeColor():
    "changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue', 'orange', 'yellow']
    c = randrange(8) # genere un nombre aléatoire  de 0 à 7
    coul = pal[c]

#------ Progamme principal ------

# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 10, 790, 10 # coordonnées de la ligne
coul = 'dark green'

# création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg = 'white', height=800, width=800)
can1.pack(side=LEFT)
bou1 = Button(fen1, text="quitter", command = fen1.quit)
bou1.pack(side = BOTTOM)
bou2 = Button(fen1, text="Tracer une ligne", command = drawline)
bou2.pack()
bou3 = Button(fen1, text="Autre couleur", command = changeColor)
bou3.pack()

fen1.mainloop() # démarrage du réceptionnaire d'évènement
fen1.destroy() # destruction fermeture de la fenetre
'''

# Exercice de modification sur Tkinter

# Petit exercice utilisant la bibliothèque graphique tkinter
'''
from tkinter import * 
from random import randrange

# --- définition  des fonctions gestionnaires d'évènement : ---
# fonction qui doit tracer une ligne

def drawline():
    "tracé d'une ligne dans le canevas can1"
   # global x1, y1, x2, y2, coul
    x1, y1, x2, y2 = 10, 790, 790, 10
    can1.create_line(x1,y1,x2,y2, width = 1, fill = coul)

    # modification des coordonnées pour la ligne suivante :
    y1, y2 = y1+5, y2 +5
'''
'''
# fonction qui doit tracer un rectangle avec create_rectangle ou un polygone avec creat_polygone
def drawline():
    "tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_polygon([150,75,300,75,225,150], width = 1, fill = coul)
    # Pour un polygone, un couple de coordonnées correspond à un des points du polygones

    # modification des coordonnées pour la ligne suivante :
    y1, y2 = y1+5, y2 +5
'''
'''
# fonction qui doit tracer deux lignes rouges en croix au centre du canevas : une horizontale et une verticale
def drawline2():
    global x3, y3, x4, y4
    global x5, y5, x6, y6
    can1.create_line(x3,y3,x4,y4, width = 2, fill = "red")
    can1.create_line(x5,y5,x6,y6, width = 2, fill = "red")

    


def changeColor():
    "changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue', 'orange', 'yellow']
    c = randrange(8) # genere un nombre aléatoire  de 0 à 7
    coul = pal[c]

#------ Progamme principal ------

# les variables suivantes seront utilisées de manière globale :
#x1, y1, x2, y2 = 10, 790, 790, 10 # coordonnées de la ligne
x3, y3, x4, y4 = 350, 400, 450, 400 
x5, y5, x6, y6 = 400, 350, 400, 450
coul = 'dark green'

# création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg = 'white', height=800, width=800)
can1.pack(side=LEFT)
bou1 = Button(fen1, text="quitter", command = fen1.quit)
bou1.pack(side = BOTTOM)
bou2 = Button(fen1, text="Tracer une ligne", command = drawline)
bou2.pack()
bou3 = Button(fen1, text="Autre couleur", command = changeColor)
bou3.pack()
bou4 = Button(fen1, text="viseur",command = drawline2)
bou4.pack()
fen1.mainloop() # démarrage du réceptionnaire d'évènement
fen1.destroy() # destruction fermeture de la fenetre
'''

# A / Créer un cours programme qui dessinera les 5 anneaux olympiques dans un rectangle de fond blanc(white). Un bouton <quitter> doit permettre de fermer la fenètre

from tkinter import *

# les variables suivantes seront utilisées de manière globale :


# fonction qui doit tracer un cercle avec create_oval
def drawcircle():
    # global x1, y1, x2, y2  # coordonnées de la ligne
    x1, y1, x2, y2 = 10, 200, 210, 400  
    "tracé d'un cercle dans le canevas can1"
    can1.create_oval([x1, y1, x2, y2], width = 1, outline='green')

def olympiqueRing():
    x1, y1, x2, y2 = 10, 200, 210, 400  
    x3, y3, x4, y4 = 110, 100, 310, 300
    couleur = ['red', 'blue', 'black', 'green','pink', 'yellow', 'purple']
    # boucle for
    '''
    for i in range(0,4):
        coul = couleur[i]
        can1.create_oval([x1, y1, x2, y2], width = 2, outline = coul)
        coul = couleur[i+1]
        x1, x2 = x1 +200, x2 +200
    for i in range(4,7):
        
        can1.create_oval([x3, y3, x4, y4 ], width = 2, outline = coul)  
        x3, x4 = x3 +200, x4 +200
        print (coul)
        coul = couleur[i+1]
    '''  
    # boucle while  
    nbre_cercle = 7
    while 7 >= nbre_cercle >= 4:
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
        '''
        can1.create_oval([200, 500, 400, 700 ], width = 2, outline='blue')
        can1.create_oval([400, 500, 600, 700 ], width = 2, outline='pink')
        can1.create_oval([600, 500, 800, 700 ], width = 2, outline='black')
        '''

        #x1, x2 = x1 + 200, x2 + 200

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
bou3 = Button(fen1, text="Tracer les anneaux", command = olympiqueRing)
bou3.pack()
fen1.mainloop() # démarrage du réceptionnaire d'évènement
fen1.destroy() # destruction fermeture de la fenetre

# B / Modifier le programme ci-dessus en y ajoutant 5 boutton. Chacun de ces bouttons provoquera le tracé de chacun des anneaux.
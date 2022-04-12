# Un radian est égal à 57 degrés 17 minutes 44 secondes ou 63,66 grades.
# Ecrivez un programme qui convertisse en degrés, minutes, secondes un angle fourni au départ en radian
'''
angleRadian = 57
angleDegre = 57*angleRadian
angleminute = 17*angleRadian
angleSeconde = 44*angleRadian

print(f"{angleRadian} radian est égale à {angleDegre + (angleminute-angleminute%60)/60} degrées, {angleminute%60} minutes ,{angleSeconde%60} secondes.")
'''
# ecrire un programme qui convertisse en degrées Celcius  une température exprimée au départ en degrés fahrenheit ou l'inverse
# la formule de converstion est  Tf = Tc x 1,8 + 32 --> Tc = (Tf-32)/1,8

'''
def convertFahrenheit(tempCelcius):
    tempFahrenheit = tempCelcius * 1.8 + 32
    print(f" la température en Fahrenheit est de : {tempFahrenheit}")

def convertCelcius(tempFahrenheit):
    tempCelcius = (tempFahrenheit -32 )/1.8
    print(f"La température en Celcius est de {tempCelcius}")

convertFahrenheit(456)
convertCelcius(852)
'''

# Ecrire un programme qui calcule les interets  accumulés chaque année pendant 20 ans, par capitalisationd'un somme de 100 euros placés en banque avec un taux fixe  de 4,3%
'''
somme = 10000
tauxInteret = 0.043

for i in range(1, 21):
    somme = somme + somme * tauxInteret
    print(f"année {i} : somme sur le compte : {somme}")
'''
# Ecrire un programme qui affiche le nombre de grain déposé sur chacune des cases d'un jeux d'échec ( 64 cases) sachant que l'on double la valeur des grains à chaque case
# le faire de deux manières en nombre entier puis en nombre réel
'''
nombreDeGrainDeRiz = 1
print(f"case 1 : le nombre de grains de riz est de : {nombreDeGrainDeRiz}")
for i in range(2, 65):
    nombreDeGrainDeRiz = nombreDeGrainDeRiz*2
    print(f"case {i} : le nombre de grains de riz est de : {nombreDeGrainDeRiz}")
'''
'''
c=1
g=1
while c < 65:
    c, g = c+1, g*2
    print (f"numéro de la case : {c}; nombre de grain de riz : {g}")
'''
# Ecrire un script qui détermine si une chaîne contient ou non le caractère "e"
'''
chaine = "salut les amis, vous allz bin?"
reponse = False
for i in range (0, len(chaine)):
    if chaine[i] == "e":
        reponse = True

if reponse == True:
    print ("la chaîne de caractère contient au moins un 'e'")
else:
    print ("il n'y a pas de \"e \" dans la chaîne de caractère")
'''
# Ecrire un script qui compte le nombre d'occurences du caractère "e" dans une chaîne.
'''
chaine = "salut les amies, vous allez bien?"
reponse = False
nombreDeE = 0
for i in range (0, len(chaine)):
    if chaine[i] == "e":
        nombreDeE += 1
        reponse = True

if reponse == True:
    print (f"la chaîne de caractère contient  {nombreDeE} : lettre(s) 'e'")
else:
    print ("il n'y a pas de \"e \" dans la chaîne de caractère")
'''

# Ecrire un script qui recopie une chaîne ( dans une nouvelle variable ) en l'inversant
'''
chaine = "lapinerillette"
motReverse = chaine[::-1]
print(motReverse)
'''
# Ecrire un script qui recopie une chaîne ( dans une nouvelle variable ) en ajoutant des astérix entre les caractères
'''chaine = "salut tout le monde"
result ="" 
for i in range (0, len(chaine)):
    result = result + str(chaine[i]) + "*"
print(result)
'''
'''
# affichage des jours de la semaine avec l'opérateur modulo et la gestion d'une liste
jour = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
a, b = 0,0
while a<25:
    a = a+1
    b = a %7
    print(a,jour[b])
'''

# En partant de l'exercie précédent, écrivez un script qui détermine si une chaîne de caractères donnée est un palindrôme ( c'est à dire une chaîne qui peut se lire indifféremment dans les deux sens comme radar et SOS par exemple:!)  
'''
chaine = "poiuyuiop"
if chaine == chaine[::-1]:
    print("*cette chaine de caractère est un palindrôme")
else :
    print("*cette chaine de caractère n'est pas un palindrôme")
'''

# Soit les listes suivantes :
#t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
# Ecrivez un programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les éléments des deux listes en les alternants, de telle manière que chaque nom de mois soit suivi du nombres de jours correspondant:
# ex : ['janvier',31, ' fevrier', 30,....]
'''
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
longueurliste = len(t1)

for i in range (0, longueurliste):
    t3 =f"{t1[i]} {t2[i]}" 
    print(t3)
'''
# Ecrivez un programme qui affiche "proprement" tous les éléments d'une liste. Si on l'appliquait par exemple à la liste t2 ( les éléments à la suite et sans séparateur)
'''
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
for i in range (len(t2)):
    print(t2[i], end=' ')
'''
# Ecrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par exemple, si on l'appliquait  à la  liste [32, 5, 12, 8, 3, 75, 2, 15] le programme devrait afficher :" le plus grand élément de cette liste a la valeur 75".
'''
l= [32, 5, 12, 88, 3, 75, 2, 15]
rep=0
for i in range(0,len(l)):
    print(l[i])
    if rep < l[i]:
        rep = l[i]

print ("le  plus grand chiffre de la liste est : " + str(rep))
'''
# Ecrivez un programme qui analyse un par un tous les éléments d'une liste de nombres ( par exemple celle de l'exercice précedent)  pour générer deux nouvelles listes. L'une contiendra seulement  les nombres pairs de la liste initiale, et l'autre les chiffres impairs.( astuce :  utiliser le modulo)
'''
l= [32, 5, 12, 88, 3, 75, 2, 15, 7, 8, 36]
lPair = []
lImpair = []
for i in range(0, len(l)):
    if l[i]%2 == 0:
        lPair.append(l[i])
    else:
        lImpair.append(l[i])

print("liste pair : " + str(lPair) )
print("liste Impair : " + str(lImpair))
'''

# Ecrivez un programme qui analyse un par un tous les éléments d'une liste de mots ( ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'] ) pout generer deux nouvelles listes, l'une avec le nombre de caractète inférieur à 6 et l'autre supérieur ou plus.
'''
l=['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
lInferieur6 = []
lSuperieur6 = []
for i in range(0,len(l)):
    if len(l[i])<6:
        lInferieur6.append(l[i])
    if len(l[i])>=6:
        lSuperieur6.append(l[i])
    else:
        print("error")
print("liste lInferieur6 : " + str(lInferieur6) )
print("liste lSuperieur6 ou égal : " + str(lSuperieur6))
'''
# Ecrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse founie par l'utilisateur  en miles/heure. (Rappel 1 Miles = 1609 mètres)
'''
from math import *
reponse = input("Convertiseur miles/h : Quelle est la valeur que vous souhaitez convertir en m/s et en km/h?")

1609 metres - 3600 secondes ( miles/heures)
1 metre - 1seconde (m/s)
1000 metres - 3600 secondes (km/h)
1 miles/h  = 1609 m en 3600s

reponseInt = float(reponse)
#milesParSeconde = reponseInt/3600
#metreParSeconde = milesParSeconde/1609
metreParSeconde = reponseInt*1609/3600
kilometreParHeure = reponseInt * 1.609

print (f"Votre vitesse en miles/heures : { reponse }, en m/s : {metreParSeconde} , en km/h {kilometreParHeure} ")
'''
# Ecrivez un programme qui calcule le périmètre et l'aire d'un triangle quelquonque dont l'utilisateur founit les trois côtés
# formule de l'aire d'un triangle quelquonque S = racine carré {d.(d-a).(d-b).(d-c)}
# d= longueur du demi-périmètre et a,b et c sont les trois côtés
from math import *

longeurCotesTriangle = []
perimetre = 0
aire = 0

def testInputValide():
    longueurCoteTriangle = input("veuillez entrer la longueur d'un côtés du triangle, puis valider avec la touche entrée :  ")
    try:
        reponseInt= int(longueurCoteTriangle)
        if reponseInt <= 0 :
            print("Veuillez entrer une valeur supérieur à 0!")
            return testInputValide()
    except:
        print("Veuillez entrer un chiffre!")
        return testInputValide()
    return reponseInt

for i in range(3):
    reponse = testInputValide()
    print(" longueur du côtés  "+ str(i+1) +" du triangle : " + str(reponse))
    longeurCotesTriangle.append(reponse)
    perimetre += longeurCotesTriangle[i]
d = perimetre/2


aire = sqrt(d*(d-a)*(d-b)*(d-c))


print(" le périmètre du triangle est  : " + str(perimetre))

'''
d= (a+b+c)/2
aireDuTriangle = sqrt(d*(d-a)*(d-b)*(d-c))
print(f" le périmètre du triangle donnée est : {d*2} et son aire est est de {d}")
'''
# Ecrivez un programme qui calcule la période d'un pendule simple de longueur donnée.
# formule de calcule : T = 2*Pi*Racine carré(l/g)
# l = longueur du pendule; G = la valeur de l'accélération de la pesanteur au lieu d'expérience

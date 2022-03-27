# programme qui calcule le volume d'un parallélépipède rectangle dont sont founis au départ, la largeur, la hauteur et la profondeur
'''
def volumeParalelepidede(largeur,longueur,profondeur):
    volume = longueur*largeur*profondeur
    print("le volume du paralélépipède est de " + str(volume))
    return volume

volumeParalelepidede(55,9,5)
'''
# Programme qui convertis un nombre entier de secondes fourni au départ en un nombres d'années, de mois, de jours, de minutes et de secondes (utiliser l'opérateur modulo %)
# un an = 12 mois; un mois = 30 jours; un jour = 1440 minutes; 1 minutes = 60 secondes

'''
nombreDeSecondes = 1234567894
nbrAnnee = 0
nbrMois = 0
nbrJour = 0
nbrMinute = 0

nbrMinute = (nombreDeSecondes - nombreDeSecondes%60) / 60 #minutes

if nbrMinute > 60:
    nbrheure = (nbrMinute - nbrMinute%60) // 60
    nbrMinute = nbrMinute%60
    if nbrheure >24:
        nbrJour = (nbrheure - nbrheure%24) // 24
        nbrheure = nbrheure%24
        if nbrJour > 30:
            nbrMois = (nbrJour - nbrJour%30) // 30
            nbrJour = nbrJour%30
            if nbrMois > 12:
                nbrAnnee = (nbrMois - nbrMois%12) // 12
                nbrMois = nbrMois%12

print(f"il y a  {nbrAnnee} année(s)  {nbrMois}  mois {nbrJour}  jour(s) {nbrheure}  heures  {nbrMinute} minute(s) et  {nombreDeSecondes % 60}  secondes")
'''

# Ecrire un programme qui affiche les 20 premiers termes de la table de multiplication de 7, en signalant au passage les multiples de 3 à l'aide d'une asterisque
# exemple : 7 14 21* 28 35 ...
'''
for i in range (1,21):
    resultat= 7*i
    if resultat%3==0:
        print (f"{i} x 7 = {resultat}* ")
    else:
        print (f"{i} x 7 = {resultat} ")
'''
#Ecrire un programme qui calcule les 50 premiers termes de la table de multiplication de 13, mais n'affiche que ceux qui sont des multiples de 7
'''
for i in range(1, 51):
    resultat = 13 * i
    if resultat%7==0:
        print(f"{i} x 13 = {resultat}")
'''
# Ecrire un programme qui affiche la suite de symbole suivants:
# *
# **
# ***
# ****
# *****
# ******
# *******
'''
reponse=""
for i in range (1,100):
    reponse+= "*"

    print(reponse, i)
'''

# inverser une chaîne de caractère
'''
def inverse(mot):
    return print(mot[::-1])
inverse("gros lapin du tonnerre")
# On utilise ici la méthode slice(debut:fin:step) en mettant les valeur à 0 debut et de fin on obtiens une inversion
'''

# Demander le noms des personnes de façon infini
# lorsque le nom est vide alors on sort de la boucle avec un break
# Une fois sorti du programme on affiche tout les noms saisis par l'utilisateur
'''
list = []
while True:
    nom = input("Quelle est le nom de la personne que vous souhaitez ajouter : ")
    if nom == "":
        break
    list.append(nom)
    
print("le nom de la ou les personne(s) que vous avez saisie est :",  list[::])
'''
# trouver la distance la plus petite de cette liste:
# distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
'''
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
distance_min = distance_chauffeur_km[0]

for distance in distance_chauffeur_km:
    if distance < distance_min:
        distance_min = distance

print("la valeur la plus petite de la liste est : " , distance_min)
'''
# Améliorer le programme ci dessus pour en "l'associant" avec la valeur de la seconde liste afin que la réponse associe le chauffeur le plus proche et son nom
# nom_chauffeur = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
'''
nom_chauffeur = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
distance_min = distance_chauffeur_km[0]
nom_chauffeur_min = nom_chauffeur[0]

for i in range(len(distance_chauffeur_km)):
    if distance_chauffeur_km[i] < distance_min:
        distance_min = distance_chauffeur_km[i]
        nom_chauffeur_min = nom_chauffeur[i]

print("la distance la plus petite de la liste est : " , distance_min, " km et le nom du chauffeur est: ", nom_chauffeur_min)
'''
# Donner la valeur la plus petite de la liste de distance mais en utilisant la fonction sort:
'''
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
distance_chauffeur_km.sort()
print("la distance la plus petite de la liste est : " , distance_chauffeur_km[0])
'''
# En utilisant une liste de tuples qui associe mieux les données refaire l'exercice avec la nouvelle liste
# nom_et_distance = = [("Patrick", 1.5), ("Paul", 2.2), ("Marc", 0.4), ("Jean", 0.9), ("Pierre", 7.1), ("Marie", 1.1), ("Maxime", 0.6)]
noms_et_distances = [("Patrick", 1.5), ("Paul", 2.2), ("Marc", 0.4), ("Jean", 0.9), ("Pierre", 7.1), ("Marie", 1.1), ("Maxime", 0.6)]

index = 0
'''
for i in range(len(nom_et_distance)):
    distance_min = nom_et_distance[0][1]
    print(f"distance min est à la valeur :{distance_min}")
    if nom_et_distance[i][1] < distance_min[1]:
        distance_min = nom_et_distance[i][1]
        print(distance_min)
        index = i
        print(i)


print(nom_et_distance[1])
'''
nom_et_distance_min = noms_et_distances[0]
for nom_et_distance in noms_et_distances:



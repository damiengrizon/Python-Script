# I Que fait le programme ci-dessous dans les quatre cas où l'on aurait défini au préalable wue la variable a vaut 1, 2, 3 ou 15?
'''
if a!=2:
    print('perdu')
elif a==3:
    print ('un instant svp')
else: print('gagné')
'''
# Si  a est égale à ...
# a=1: perdu
# a=2: gagné
# a=3: un instant svp
# a=15: perdu


# II Que font ces programmes?
#a)
''''
a=5
b=2
if (a==5)&(b<2):
    print('"&" singnifie "et"; on peu aussi utiliser \ le mot "and"')
'''
# ce programme affiche le print si et seulement si a=5 et b est strictement inférieur à 2
# donc ici il affiche le print

#b)
'''
a, b = 2, 4
if (a==4) or (b!=4):
    print('gagné')
elif (a==4) or (b==4):
    print('presque gagné')
'''
# la première condition n'est pas validé, la seconde est validé car B=4 donc on affiche presque gagné

#c)
'''
a=1
if not a:
    print('gagné')
elif a:
    print('perdu')
'''

# le programme affiche perdu car a = 1 donc a a la valeur True
# Si a=0 alors a prends la valeur False donc print affiche 'gagné'
# Il est donc important de faire attention à la clause if car cela peut influencer sur le script et tout changer au niveau des résultats attendu
# III - Reprendre le programme c) avec a=0 au lieu de a=1.
# Que se passe t il ? conclure?
#-------------------------------------------------------------
# Ecrire un programme qui, étant donnée deux bornes entières a et b, additionne les nombres multiples de 3 et de 5  compris entre ces bornes. 
# Prendre par exemple a=0, b=32 ; le resultat devrait alors être 0 + 15 + 30.
# Modifier légèrement ce programme  pour qu'il additionne les nombres multiples de 3 ou de 5 compris entre les bornes a et B. Avec les bornes 0 et 32,
# Le resultat devrait alors être : 0 + 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 30 = 225

#V1
'''
a = 0
b = 32
for i in range (a,b-1):
    if i%3==0 and i%5==0:
        print(i)
'''
#V2
'''
list_resultat = []
resultat_addition = 0
a = 0
b = 32
for i in range (a,b-1):
    if i%3==0 or i%5==0:
        list_resultat.append(i)
        resultat_addition = resultat_addition + i

print(list_resultat)
print(resultat_addition)
'''

# déterminer si une année (dont le millésime est introduit par l'utilisateur) est bisextile ou non.
# Une année A est bisextile si A est divisible par 4. Elle ne l'est cependant pas si A est un multiple de 100, à moins que A soit multiple de 400.
# ----- pour le test les années bosextiles sont les années : 2016 - 2020 - 2024 - 2028 - 2032
#V1
'''
année_utilisateur = input("Entrer une année afin de savoir si celle ci est bisextile ou non :  ")
année_utilisateur_INT = int(année_utilisateur)
if année_utilisateur_INT%4 == 0:
    if année_utilisateur_INT%100 == 0 and année_utilisateur_INT%400!=0:
        print("Attention l'année " + str(année_utilisateur_INT) + "n'est pas bisextile")
    print("l'année " + str(année_utilisateur_INT) + " est bisextile")
'''
#V2
''''
année_utilisateur = input("Entrer une année afin de savoir si celle ci est bisextile ou non :  ")
année_utilisateur_INT = int(année_utilisateur)
if année_utilisateur_INT%4==0:
    bs=1 # l'année est bisextile
elif année_utilisateur_INT%100 == 0:
    bs=0 # l'année n'est pas bisextile
elif année_utilisateur_INT%400 == 0:
    bs=1 # l'année est bisextile
else:
    bs=0 # l'année n'est pas bisextile
    
if bs==0:
    print("l'année n'est pas bisextile")
elif bs==1:
    print("l'année est bisextile")
'''
# Demande à l'utilisateur  son nom et son sexe. En fonction de ces données, afficher "cher monsieur" ou chere madame suivi du nom de la personne.
'''
nomPersonne = input("Quel est votre nom?")

print("erreur dans le nom, vous devez entrer un nom!")

sexePersonne = input("quel est votre sexe?")

print("erreur : les données à saisir sont homme ou femme")

if sexePersonne == "homme":
        print("cher monsieur " + nomPersonne)
elif sexePersonne == "femme":
    print("Chère madame " + nomPersonne)
else :
    print("les données entrées sont incorrectes!")
'''
# Demander à l'utilisateur d'enter trois longueur a, b, c. A l'aide de ces trois longueurs, déterminer s'il est possible de construire un triangle
# Déterminer ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque. Attention : un triangle rectangle peut être isocèle.
'''
print("veuiller entrer trois chiffres pour déterminer les trois côtés d'un triangle:")
coteA = input("Quelle est la longueur du premier côté du triangle : ")
coteB = input("Quelle est la longueur du deuxième côté du triangle : ")
coteC = input("Quelle est la longueur du troisième côté du triangle : ")
print(f"Ce triangle possède trois cotes de longueur :  {coteA}, {coteB}, {coteC} ")
'''
def verifTriangleRectangle(a,b,c): # longueur des cotés du triangle
    listCote=[a,b,c]
    sommeDesCotes = 0
    indexmax = listCote.index(max(listCote)) # on recupere l'index de la valeur max
    maxi = listCote[indexmax] # on sauvegarde la valeur max dans une variable
    listCote.pop(indexmax) # on suprime la valeur max de la liste

    for element in listCote:
        sommeDesCotes += element**2
    
    if sommeDesCotes == maxi**2:
        return True
    else:
        return False
    
    


print(verifTriangleRectangle(6,8,10))
    
    

'''
if int(coteA)==0 or int(coteB)==0 or int(coteC)==0:
    print("un des côtés est égal à zéro, il ne peut donc pas sagir d'un triangle")
elif:
'''
'''
listtest= [3,4,5]
print(max(listtest))
'''
# Demander à l'utilisateur qu'il entre un nombre. Afficher ensuite :  soit la racine carré de ce nombre, soit un message indiquant que la racine carré 
# de ce nombre ne peut pas être calculée.

# Convertir une note scolaire N quelconque entrée par l'utilisateur  sous forme de points ( par exemple 27 sur 35), en note standardisée suivant le code ci-àprès:
'''
Note                    Appréciation
N>= 80%                     A
80% > N >= 60%
60% > N >= 50%
50% > N >= 40%
N< 40%                      E
'''


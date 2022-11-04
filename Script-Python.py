# Définissez une fonction compteCar(ca, ch) qui renvoie le nombre  de fois que l'on rencontre le caractère ca dans la chaîne de caractères ch. Par exemple, l'exécution de l'instruction : print(compteCar('e','cette phrase est un exemple')) doit donner le résultat : 7
'''
def compteCar(ca, ch):
    compteur = 0
    for i in range(0, len(ch)):
        if ch[i] == ca:
            compteur += 1
    return compteur


print(compteCar('e','cette phrase est un exemple'))
print(compteCar('o', ' Je me suis fait bobo bo lors de la bo et la bof'))
'''
# définissez une fonction indexMax(liste) qui renvoie l'index de l'élément ayant la valeur la plus élever dans la liste transmise en argument. Exemple d'utilisation :
# serie = [5, 8, 2, 1, 9, 3, 6, 7]
# print (indexMax(serie))
# 4
'''
def indexMax(liste):
    indexMax = 0
    valeurMax = 0
    for i in range(0, len(liste)):
        #print(f"contenu : {liste[i]}")
        if liste[i]>valeurMax:
            valeurMax = liste[i]
            indexMax = i
            #print(f"valeur max : {valeurMax}")

    return indexMax

serie = [5, 8, 2, 1, 9, 3, 6, 7, 5]
print (indexMax(serie))
'''

# Définissez une fonction nomMois(n) qui renvoie le nom du enième mois de l'année.
# Par exemple, l'exécution de l'instruction :
# print(moisNom(4)) doit donner : avril.
'''
def moisNom(n):
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
    return mois[n-1]

print(moisNom(10))
'''

# Définissez une fonction inverse(ch) qui permette d'inverser l'ordre des caractères d'une chaîne quelconque. La chaîne inversé sera renvoyée au programme  appelant.
'''
def inverse(ch):
    for i in range( 0, len(ch)):
        return ch[::-1]

print(inverse("france"))
print(inverse("bla et je n'ai pas fini"))
'''
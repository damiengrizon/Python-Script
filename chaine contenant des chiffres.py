from curses.ascii import isdigit


# Exercice permettant de trouver dans une chaine de caractère si cette dernière contient un chiffre ou pas

chaineTestChiffre = input("Entrer une séquence pour savoir si elle contient un chiffre : ")
resultat = any([lettre for lettre in chaineTestChiffre if isdigit(lettre)])

if resultat :
    resultat = "contient au moins un"
else:
    resultat = "ne contient pas de"
print(f"Vous avec entré : {chaineTestChiffre} et cette séquence {resultat} chiffre")


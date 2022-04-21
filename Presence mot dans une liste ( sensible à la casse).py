# l'exercice est de trouver dans une liste la présence d'un élément, attention celui-ci doit être insensible à la casse

def element_dans_liste(element, liste_cible):
    for element_liste in liste_cible:
        if element_liste.lower() == element.lower():
            return True
        else:
            return False


noms = ["Jean", "Lapin", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]
element = input("Quel est l'élément pour lequel vous souhaitez savoir s'il est présent dans la liste ?")
if element_dans_liste(element,noms):
    print(f"{element} est bien dans la liste")
else:
    print("l'élément n'est pas dans la liste")
# Tout cela ne fontionne pas le retour est toujours que l'élément n'est pas dans la liste
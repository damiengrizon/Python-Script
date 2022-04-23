# l'exercice est de trouver dans une liste la présence d'un élément, attention celui-ci doit être insensible à la casse
# V1:
'''
def element_dans_liste(element, liste_cible):
    for element_liste_cible in liste_cible:
        if element_liste_cible.lower() == element.lower():
            return True   
    return False
        

element = input("Quel est l'élément pour lequel vous souhaitez savoir s'il est présent dans la liste ?")
noms = ["Jean", "Lapin", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]      

if element_dans_liste(element,noms):  
    print(f"{element} est bien dans la liste")
else:
    print("l'élément n'est pas dans la liste")
'''
# V2:
element = input("Quel est l'élément pour lequel vous souhaitez savoir s'il est présent dans la liste ?")
noms = ["Jean", "Lapin", "Sophie", "Martin", "Christophe", "Zoe", "Martin"] 

def element_dans_liste(element, liste_cible):
    return any([element_liste_cible for element_liste_cible in liste_cible if element_liste_cible.lower() == element.lower()])

if element_dans_liste(element,noms):  
    print(f"{element} est bien dans la liste")
else:
    print("l'élément n'est pas dans la liste")
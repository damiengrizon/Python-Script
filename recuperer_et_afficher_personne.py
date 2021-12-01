def recuperer_infos_personne(numero_personne):
    nom = input("nom de la personne : " + str(numero_personne) + " :")
    age = input("age de la personne : " + str(numero_personne) + " :")
    return nom, age

def afficher_infos_personne(numero_personne, nom, age):
    print("La personne "+ str(numero_personne) +" est " + nom + " et son age est de " + str(age)+ " an(s)")
    print("le nom possède " +  str(len(nom)) + " caractères.")


def recuperer_et_afficher_personne(numero_persone):
    nom_personne, age_personne = recuperer_infos_personne(numero_persone)
    afficher_infos_personne(numero_persone, nom_personne, age_personne)

nombre_de_personne = int(input(" nombre de personne : "))

for i in range(nombre_de_personne):
        recuperer_et_afficher_personne(i+1)

'''
def est_mineur():
    if age < 18:
        True 
    False   

recuperer_et_afficher_personne("jean", "jean", 18)
recuperer_et_afficher_personne("jordan", "marie", 22)
recuperer_et_afficher_personne("Artuhuer", "pierre", 12)
'''
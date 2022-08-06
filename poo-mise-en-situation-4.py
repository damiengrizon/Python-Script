# POO EXERCICE DE MISE EN SITUATION 4


class Etre_Vivant:
    ESPECE = "Espèce non défini"

    def afficherEspece(self):
        print("Je suis un " +  self.ESPECE)
        print()

class Personne(Etre_Vivant):
    ESPECE = " humain "

    def __init__(self, nom: str, age : int):
        self.nom = nom
        self.age = age

    def sePresenter(self):
        print("Bonjour, je m'appelle " + self.nom  + " j'ai " + str(self.age) + " ans. " )


class Etudiant(Personne):
    def __init__(self, nom: str, age : int, etude: str):
        super().__init__(nom, age)
        self.etude = etude

    def sePresenter(self):
        super().sePresenter()
        print(" je suis : " + self.etude)

class Chat(Etre_Vivant):
    # Par défaut, il y a un constructeur vide. C'est pour ça que pour le chat il n'apparait pas ici
    ESPECE = " Félin "



personne = Personne('Jean', 23)
personne.sePresenter()

chat = Chat()
chat.afficherEspece()

etudiant = Etudiant('Bernard', 19, "étudiant en maitrise des études")
etudiant.sePresenter()
etudiant.afficherEspece()
# ---
# noms = []
# nombre_personne = int(input("Quel est le nombre de personne que vous souhaitez présenter? "))

#liste_personne = []
#for i in range(nombre_personne) :
#    liste_personne.append(Personne(input("nom de la personne " + str(i+1) + " : ")))




# for personne in liste_personne:
#    liste_personne.append(Personne(input("nom de la personne " + str(i+1) + " : ")))

#for personne in liste_personne:
#    personne.SePresenter()
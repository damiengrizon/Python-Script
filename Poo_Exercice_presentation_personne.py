class Personne:
    def __init__(self, nom ="", age = 0):
        self.nom = nom
        self.age = age
        if self.nom == "":
                self.demanderNom()
                self.demanderAge()
    
    def sePresenter(self):
        infoPersonne = f"Je m'appelle {self.nom}"

        if self.age == 0:
            print(infoPersonne)
        else :
            print(infoPersonne + f" et mon age est de {self.age} an(s)" )
            if self.estMajeur():
                print("Je suis majeur")
            else :
                print("Je suis mineur")
    
    def estMajeur(self):
        return int(self.age) >= 18
        # la solution ci dessus est plus simple et retourne un booléen
        '''
        if self.age < 18:
            return False
        elif self.age >18:
            return True
        '''
    def demanderNom(self):
        self.nom = input("quel est votre nom?")
        return self.nom

    def demanderAge(self):
        self.age = input("quel est votre age?")
        return self.age

personne1 = Personne("Jean", 15)
personne2 = Personne("Paul", 25)
personne3 = Personne("Pierre")
personne4 = Personne()

# personne2.demanderNomEtAge()
personne1.sePresenter()
personne2.sePresenter()
personne3.sePresenter()
personne4.sePresenter()
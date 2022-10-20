# Défnissez une fonctions ligneCar(n, ca) qui renvoie une chaine de n caractères ca.
# un exemple serait cacacacaca si on met ligneCar(5,ca)
def ligneCar(n, ca):
    result = ""
    for i in range (0,n):
        result += ca
    print(result)
        

ligneCar(5, "ca")
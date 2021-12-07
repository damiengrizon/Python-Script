n = input("Quelles tables de multiplication souhaitez-vous?")
min = input("Quel est le premier chiffre de la table de multiplication que vous souhaitez? - validez pour 1")
max = input("Quel est le dernier chiffre de la table de multiplication que vous souhaitez? - validez pour 10")


def afficher_table_multiplication(n, min = 3, max = 11):
    for min in range(max):
        print("min : " + str(min) + " et n :" + str(n) + "resultat : " + str(int(min)*int(n)))
    

afficher_table_multiplication(n)

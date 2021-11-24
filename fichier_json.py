# JSON
# manipuler des données structurées

# on va sérialiser les données DATA -> TXT"" (JSON)
# --> on utilise la fonction dumps pour sérialiser
# on peut aussi désérialiser TXT(JSON) -> DATA
# --> on utilise la fontion loads pour désérialiser
import json

personne = {"nom" : "Paul",
            "age" : 25,
            "amis" : ["Sophie", "Marie", "Jean"]}

personne_json = json.dumps(personne)
print ("json  :  " + personne_json)

f = open("fichier_json.txt", "w")
f.write(personne_json)
f.close()
# fichier texte
# si l'on veut ajouter du texte à la ligne il faut ajouter un saut de ligne \n
# 'r' ouvre en lecture (par défaut)
# 'w' ouvre en écriture, en effaçant le contenu du fichier
# 'x' ouvre pour une création exclusive, échouant si le fichier existe déjà
# 'a' open for writing, appending to the end of file if it exists -
# 'b' mode binaire
# 't' mode texte (par défaut)
# '+' ouvre en modification (lecture et écriture)

exemplePhrase = ["Salut mon lapin comment ça va", "Mange tes carotes mon gros", "Je peux pas je suis au régime"]

f = open("mon_fichier.txt", "w")

f.write("bonjour\n")
# Sers à afficher les lignes de la liste
f.writelines(exemplePhrase)
# le \n permet le retour à la ligne
f.write("\n")
# Pour afficher la liste mais en prenant les éléménts un à un pour les remettre à la ligne
f.write("\n".join(exemplePhrase))

f.close()
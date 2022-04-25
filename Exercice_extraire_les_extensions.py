# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"

fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

'''
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte)
vacances.jpeg (Image JPEG)
planning (Aucune extension)
data.dat (Extension non connue)
'''
# récuperer l'extension avec son index sur la liste fichier
# comparer l'extension avec la deuxième liste
# afficher la deuxième partie de l'extention

def recuperer_extension(listeNoms, nombre) :
    if "." in listeNoms[nombre]:
        return listeNoms[nombre].lower().split(".")[-1]
    else:
        return False

for element in definition_extensions:
    for noms in fichiers:
        if definition_extensions[definition_extensions.index(element)][0] == recuperer_extension(fichiers, definition_extensions.index(element)):
            print(fichiers[definition_extensions.index(element)] + " " +  definition_extensions[definition_extensions.index(element)][1] )
        else:
            print(f"{fichiers[definition_extensions.index(element)]} :  Extension non connue ")

    #extension = [ fichier.lower().split(".")[-1] if "." in fichier else False for fichier in listeFichier]
    #return extension

#for i in definition_extensions:
 #   print(definition_extensions[0][1])
  #  print(recuperer_extension(fichiers, 0))

'''
if definition_extensions[i][1] == recuperer_extension(fichiers, i):
print("coucou")
else:
print("pas coucou")
'''


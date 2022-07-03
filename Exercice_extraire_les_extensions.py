# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"

fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jPeg", "planning", "data.dat", "proutpad.exe")

definition_extensions = (
    ("doc", "Document Word"),
    ("exe", "Executable"),
    ("txt", "Document Texte"),
    ("jpeg", "Image JPEG")
    )

dic_definition_extensions = {
    "doc" : "Document Word",
    "exe" : "Executable",
    "txt" : "Document Texte",
    "jpeg": "Image JPEG"
}

'''
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte)
vacances.jpeg (Image JPEG)
planning (Aucune extension)
data.dat (Extension non connue)
'''
# créer une nouvelle liste avec les extensions seulemenent et False quand il n'y en a pas
# comparer la liste d'extension avec la liste des definitions
# ajouter à la liste fichier avec l'indice de l'extension obtenue +1  pour avoir le texte de l'extention
'''
Pour chaque element de la liste de fichiers :
si l'extention est la meme que celle de la definition alors tu affiches la deuxième partie en plus et entre parenthèse
'''
for fichier in fichiers:
    # recupere l'extension du fichier et la met en minuscule - dernier element séparé par un point
    if fichier.lower().split(".")[-1] in dic_definition_extensions:
        print(fichier, "(" + dic_definition_extensions[fichier.lower().split(".")[-1]] + ")")
    elif "." not in fichier :
        print(fichier,"("+"Aucune extension"+")")
    elif fichier.lower().split(".")[-1] not in dic_definition_extensions:
        print(fichier,"("+"Extension non connue"+")")
    
   
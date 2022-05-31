import time
import random

name = input ('Comment vous appelez vous?')
print(f"Bonjour {name}, c'est l'heure de jouer au pendu!")
# donne une séquence de 1 seconde avant d'afficher la suite du script
time.sleep(1) 
print(f"Taper une lettre pour trouver le mot caché...")
time.sleep(0.5)
# liste de mots servant de source au jeu du pendu
words = ['python', 'nintendo', 'lapin', 'chaloperie']
# choisi un  mot au hasard dans la liste words
word = random.choice(words)
# la variable guesses va servir à afficher les lettres que l'on a déjà trouver
guesses = ''
turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed +=1
    if failed == 0 :
        print("\n Bravo, vous avez gagné !!!")
        break
    guess = input("\n taper la lettre de votre choix : ")
    guesses += guess
    if guess not in word:
        turns-=1
        print("\n Hélas vous n'avez rien trouvé")
        print("\n il vous reste ", + turns , "essais")
        if turns == 0:
            print("perdu!!")


#Questionnaire V1
'''
def poserQuestion(Q,a,b,c,d,LettreBonneReponse):
    global score
    print()
    print(Q)
    print()
    print("(a)" + a )
    print("(b)" + b )
    print("(c)" + c )
    print("(d)" + d )
        
    reponseQuestion = input ( "quelle est votre réponse?")
    reponseCorrect = False
    if reponseQuestion == LettreBonneReponse:
        print("ouah t trop fort")
        score+=1
    else:
        print("Dommage, ce n'est pas la bonne réponse")
        
    


score = 0
poserQuestion("Qui est le plus rapide ? ","lapin", "renard", "pieuvre", "guépard", "d")
poserQuestion("Qui est le plus lent ? ","lapin","tortue", "pieuvre", "guépard", "b")
poserQuestion("Qui est le pénible ? ","lapin", "renard", "pieuvre", "chat", "d")
poserQuestion("Qui est le plus grand ? ","lapin", "renard", "éléphant", "guépard", "c")
print ( "votre score est de  : " + str(score))
'''

#Questionnaire V2 
# Adaptation avec l'utilisation des listes et des tuples

question1 = ("Qui est le plus rapide ? ", ("lapin", "renard", "pieuvre", "guépard"), "guépard")
question2 = ("Qui est le plus lent ? ", ("lapin","tortue", "pieuvre", "guépard"),"tortue" )
question3 = ("Qui est le pénible ? ", ("lapin", "renard", "pieuvre", "chat"),"chat")
question4 = ("Qui est le plus grand ? ", ("lapin", "renard", "éléphant", "guépard"), "éléphant")
score = 0

def poserQuestion(question):
    global score
    print()
    print(question[0])
    for i in range(len(question[1])):
        print( i+1, "-" , question[1][i] )
    print() 
    demander_reponse_numerique_utilisateur(1,len(question[1])


    if question[1][reponseInt-1] == question[2]:
        print("ouah t trop fort")
        score+=1
    else:
        print("Dommage, ce n'est pas la bonne réponse")

poserQuestion(question1)
poserQuestion(question2)
poserQuestion(question3)
poserQuestion(question4)
print(f"ton score est de", score)

def demander_reponse_numerique_utilisateur(min,max):
    reponseQuestion = input ( "quelle est votre réponse? (de " + str(min) + " à " + str(max) + ") :")
    while reponseQuestion > max:
        print("votre réponse est supérieur au nombre de réponses")
    while reponseQuestion =
    reponseInt = int(reponseQuestion)
    




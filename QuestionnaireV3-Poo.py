# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

'''
def demander_reponse_numerique_utlisateur(min, max):
    reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int

        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utlisateur(min, max)
    

''''''
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
''''''
def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")
    print("  " + question[0])
    for i in range(len(choix)):
        print("  ", i+1, "-", choix[i])

    print()
    resultat_response_correcte = False
    reponse_int = demander_reponse_numerique_utlisateur(1, len(choix))
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        resultat_response_correcte = True
    else:
        print("Mauvaise réponse")
        
    print()
    return resultat_response_correcte


''''''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

''''''

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :", score, "sur", len(questionnaire))

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)
'''

# transformation du code ci dessus en version POO:
# 
# il faudrait :
#   question :
#       - titre de la question  - str
#       - reponse possible      - (str)
#       - bonne réponse         - str
#       poser()                 -> bool
#       demander_reponse_numerique_utlisateur(min, max)
#
#   questionnaire :
#       - question
#       lancer questionnaire()

class Question:
    def __init__(self, titreQuestion : str, reponsesQuestion, bonneReponse : str):
        self.titreQuestion = titreQuestion
        self.reponsesQuestion = reponsesQuestion
        self.bonneReponse = bonneReponse
    
    def poser_question(self):
        print("QUESTION")
        print("  " + self.titreQuestion)
        for i in range(len(self.reponsesQuestion)):
            print("  ", i+1, "-", self.reponsesQuestion[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utilisateur(1, len(self.reponsesQuestion))
        if self.reponsesQuestion[reponse_int-1].lower() == self.bonneReponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte
    
    def demander_reponse_numerique_utilisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utilisateur(min, max)



# question1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# question1.poser_question()    


class Questionnaire():
    def __init__(self, questions):
        self.questions = questions

    def lancer_questionnaire(self):
        score = 0
        for question in self.questions:
            if question.poser_question():
                score += 1
        print("Score final :", score, "sur", len(self.questions))



'''
questions = (
            Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
            Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
            Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
            )
questionnaire1 = Questionnaire(questions)
questionnaire1.lancer_questionnaire()
'''
# Version simplifié pour lancer le questionnaire :

questionnaire1 = Questionnaire(
            (
            Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
            Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
            Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
            )
).lancer_questionnaire()


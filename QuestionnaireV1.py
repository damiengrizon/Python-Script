def poserQuestion(Q,a,b,c,d,LettreBonneReponse):
    print(Q)
    print("(a)" + a )
    print("(b)" + b )
    print("(c)" + c )
    print("(d)" + d )
        
    reponseQuestion = input ( "quelle est votre réponse?")

    if reponseQuestion == LettreBonneReponse:
        print("ouah t trop fort")
    else:
        print("Dommage, ce n'est pas la bonne réponse")

poserQuestion("Qui est le plus rapide ? ","lapin", "renard", "pieuvre", "guépard", "d")
poserQuestion("Qui est le plus lent ? ","lapin","tortue", "pieuvre", "guépard", "b")
poserQuestion("Qui est le pénible ? ","lapin", "renard", "pieuvre", "chat", "d")
poserQuestion("Qui est le plus grand ? ","lapin", "renard", "éléphant", "guépard", "c")

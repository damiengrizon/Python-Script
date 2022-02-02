def afficherTableDeMultiplication(n, min = 0, max = 10):
    if min > max:
        print ( "error t'es nul en math")
        return
    print("La table de multiplication de : " + str(n))
    for i in range(min, max + 1):
        print(str(n) + " * " + str(i) + " = "+ str(n*i) )

afficherTableDeMultiplication(8, 8, 5)
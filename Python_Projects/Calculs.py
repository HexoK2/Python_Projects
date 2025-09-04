import random
import time
import re

def affiche_result(result, start_time):
    print("Vous avez répondu aux dix questions, voici votre score: " + str(result) + "/10 en " + str(round(time.time() - start_time)) + " secondes")

    if result <= 5:
        print("Hmm... ce n'est pas un très bon score... Tu peux faire mieux!")

    if result > 5 and result < 8:
        print("C'est pas mal, mais tu peux mieux faire, réessaye!")

    if result >= 8:
        print("C'est un excellent score! Je pense que tu peux passer au niveau 3 ")


Points = 0
intro = input("Bonjour nouvel utilisateur, merci de jouer à mon jeu, avant de commencer, sur quel niveau veux-tu jouer?( 1, 2 ou 3)?")
intro2 = print("Voici les règles du jeu: dix questions vous seront posé, vous aurez dix secondes par question. ")
intro3 = print("A chaque bonne réponse vous obtenez un point et dans le cas inverse(pour le niveau 2 et 3), vous perdez un point.")
intro4 = print("Pour que le jeu soit plus amusant, veuillez ne pas utiliser la calculatrice ;)")
time.sleep(2)

question = 0


if intro == "1":
    start_time = time.time()
    while question < 10:
        number_one = random.randint(1, 30)
        number_two = random.randint(1, 30)
        operators = ['+']

        # effectuer le calcul en utilisant l'opérateur choisi
        resultat = number_one + number_two

        # demander une réponse à l'utilisateur
        réponse = input("Quel est le résultat de " + str(number_one) + " + " + str(number_two) + "?")

        if réponse.isnumeric() or réponse.isdigit():
            if int(réponse) == resultat:
                print("Bonne réponse")
                Points += 1
            else:
                print("Mauvaise réponse, le résultat était", resultat)
            question += 1
        else:
            print("La réponse ne contient pas uniquement des chiffres.")

    affiche_result(Points, start_time)

if intro == "2":
    start_time = time.time()
    while question < 10:
        number_one = random.randint(1, 60)
        number_two = random.randint(1, 60)
        operators = ['+', '-']

        # choisir un opérateur aléatoirement
        operator = random.choice(operators)

        # effectuer le calcul en utilisant l'opérateur choisi
        resultat = eval(str(number_one) + operator + str(number_two))

        # demander une réponse à l'utilisateur

        réponse = input("Quel est le résultat de " + str(number_one) + operator + str(number_two) + "?")

        # vérifier si la réponse est correcte

        if réponse.isnumeric() or réponse.isdigit():
            if int(réponse) == resultat:
                print("Bonne réponse")
                Points += 1
            else:
                print("Mauvaise réponse, le résultat était", resultat)
                Points -= 1
            question += 1
        else:
            print("La réponse ne contient pas uniquement des chiffres.")

    affiche_result(Points, start_time)


if intro == "3":
    start_time = time.time()
    while question < 10:
        number_one = random.randint(1, 100)
        number_two = random.randint(1, 100)
        operators = ['+', '-', '*']

        # choisir un opérateur aléatoirement
        operator = random.choice(operators)

        # effectuer le calcul en utilisant l'opérateur choisi
        resultat = eval(str(number_one) + operator + str(number_two))

        # demander une réponse à l'utilisateur

        réponse = input("Quel est le résultat de " + str(number_one) + operator + str(number_two) + "?")
        # vérifier si la réponse est correcte
        if réponse.isnumeric() or réponse.isdigit():
            if int(réponse) == resultat:
                print("Bonne réponse")
                Points += 1
            else:
                print("Mauvaise réponse, le résultat était", resultat)
                Points -= 1
            question += 1
        else:
            print("La réponse ne contient pas uniquement des chiffres.")

    affiche_result(Points, start_time)

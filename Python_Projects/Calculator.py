import random

while True :
    Operator  =['+', '-', '*', '/']
    RandomNumbers = input("Premier nombre ?")
    if RandomNumbers.isdigit() :
        RandomNumbers2 = input("Deuxième nombre ?")
        if RandomNumbers2.isdigit() :
            operator = input("Operateur ?")
            if operator in Operator :
                print(str(RandomNumbers) + (operator) + str(RandomNumbers2))
                print(eval(str(RandomNumbers) + str(operator) + str(RandomNumbers2)))
            else:
                print("Sasissez un operateur !")
        else:
            print("Saisissez un nombre !")
    else:
        print("Saisissez un nombre !")








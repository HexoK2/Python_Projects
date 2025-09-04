import random
import operator



Operators = operator
RandomNumbers = input("Premier nombre ?")
RandomNumbers2 = input("Deuxième nombre ?")
RandomOperators = random.choice(Operators)

print(str(RandomNumbers) + str(RandomOperators) + str(RandomNumbers2))
print(eval(str(RandomNumbers) + str(RandomOperators) + str(RandomNumbers2)))

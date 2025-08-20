import random


#Toute les variables necessaire

Letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers = '0123456789'
Character = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

Password = Letters + Numbers + Character

Password_Number = int(input("Quelle longueur de mot de passe voulez-vous ?"))
Password_result = ""

for _ in range(Password_Number):
    Password_Choice = random.choice(Password)
    Password_result += Password_Choice

print(Password_result)
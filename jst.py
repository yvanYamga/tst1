# PROTOTYPE #
# Le juste prix #

from random import randint

Prix = randint(50,250)
print ("*****Bienvenue dans le jeu du juste*****", Prix)

jst = int(input("Veuillez entrer votre proposition de prix :"))

if Prix != jst:
    print("Votre proposition n'est pas correcte")

else :
    print("BRAVO VOUS AVEZ RAISON C'EST LE PRIX EXACTE")

print("Merci d'avoir participé ")


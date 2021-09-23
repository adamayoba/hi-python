#Importation des librairies
import random

#saisi de l'utilisateur
def saisie_U(message="Veillez saisir le caratère "):
    entrez = input(message)
    return entrez

nom = saisie_U("Veillez saisir votre nom")
print("Bonne chance!", nom)


mots = ['programmer', 'code', 'manger','suivre', 'courir', 'chanter', 'fuire',
         'visio', 'ecole', 'maison', 'ordinateur','machine', 'logiciel','programme',
         'teams','remote','distance']

mot = random.choice(mots)
print(mot)

print("*********************choix des caractères*******************************")

choix =''
nombre_Essay = 10

while nombre_Essay > 0:
    echec = 0

    for carac in mot:

        if carac in choix:
            print(carac)

        else:
            print("_")

            echec +=1

    if echec == 0:

        print("tu as gagné")

        print("the word est:",mot)
        break

    choi = saisie_U()

    choix += choi

    if choi not in mot:
        nombre_Essay-=1

        print("mauvais choix")

        print("tu as encore", + nombre_Essay,'choix')

        if nombre_Essay == 0:
            print("Tu as perdu")

    else:
        print("Bien joué continue comme ça!")








#importation package
from random import randint

#les options et choix de l'ordinateur
def choixOrdi():
    aleaMot = ["Rock", "Paper", "Scissors"]
    ordinateur = aleaMot[randint(0, 2)]
    return ordinateur


#saisie du joueur
def saisieJoeur(message = "Joeur entre Rock, Paper et Scissors"):
    jouer = input(message)
    return jouer


#le deroulement du jeux

def main():
    commence = True
    bonMot = False
    while bonMot or commence:
        jouer = False
        joueur = saisieJoeur()
        ordinateur = choixOrdi()

        while jouer == False:
            jouer = joueur

            if jouer == ordinateur:
                print("égalité")
            elif jouer == "Rock":
                if ordinateur == "Paper":
                    print("Tu as perdu", ordinateur,"couvre le",jouer)
                else:
                    print("Tu gagne", joueur,"écrase l'",ordinateur)
            elif jouer == "Paper":
                if ordinateur == "Scissors":
                    print("Tu as perdu", ordinateur,"coupe le",jouer)
                else:
                    print("Tu gagne", jouer,"couvre l'",ordinateur)
            elif jouer == "Scissors":
                if ordinateur == "Rock":
                    print("Tu as perdu", ordinateur,"écrase le",jouer)
                else:
                    print("Tu gagne", jouer,"écrase l'",ordinateur)
            else:
                print("Saisissez le bon mot")
            bonMot = True


main()




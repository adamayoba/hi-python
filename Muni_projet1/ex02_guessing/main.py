import random

def aleatoire():
    aleaNombre = random.randint(1, 50)
    return aleaNombre

def saisiNombre(message = "saisissez le nombre"):
    nombre = int(input(message))
    return nombre

def compareNombre(nombreU, nombreM):
    if nombreU < nombreM:
        return "Nombre plus petit"
    elif nombreU > nombreM:
        return "Nombre plus grand"
    else:
        return "Félicitation!!!"


def main():
    felicite = False
    commence = True

    while felicite or commence:
        aleaNombre = aleatoire()
        nombreU = saisiNombre()
        message = compareNombre(nombreU,aleaNombre)

        while message != "Félicitation!!!":
            print(message)
            nombreU = saisiNombre("Réessayer encore")
            message = compareNombre(nombreU, aleaNombre)

        print(message)
        felicite = True

main()
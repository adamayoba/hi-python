import json

with open('exo00.json') as file:
    donnee = json.load(file)

with open('exo00.ini', 'w') as fini:
    for key, value in donnee.items():
        fini.write(key + "=" + str(value)+"\n")




import pandas as pd
import json

with open('exo00.json') as fj:
    donnee = json.load(fj)

    fcsv = pd.json_normalize(donnee['Etudiants'])

    fcsv.to_csv("exo00.csv")


##### CSV BESTAND INLEZEN EN AFDRUKKEN

import csv

# Vervang 'bestand.csv' door het pad naar jouw CSV-bestand
bestand = 'bestand.csv'

# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Elke rij (record) afdrukken
    for row in reader:
        for item in row:
            print(item,end="\t")
        print("")

  ##### CSV BESTAND INLEZEN NAAR EEN DICTIONARY

import csv

# Vervang 'persooneel.csv' door het pad naar jouw CSV-bestand
bestand = 'personeeldata.csv'

# Maak een lege dictionary voor de data
data = {}

# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Lees de header (kolomnamen) in
    headers = next(reader)

    # Initialiseer de dictionary met de kolomnamen als sleutels en lege lijsten als waarden
    for header in headers:
        data[header] = []

    # Voeg de rijen toe aan de juiste sleutel (kolom) in de dictionary
    for row in reader:
        for i, value in enumerate(row):
            data[headers[i]].append(value)

# Print de dictionary om de gegevens te zien
print(data)

### CSV BESTAND INLEZEN NAAR TABULATE

import csv
from tabulate import tabulate

# Vervang 'personeeldata.csv' door het pad naar jouw CSV-bestand
bestand = 'data\olympics-economics.csv'

# Maak een lege lijst voor de data
data = []

# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Lees de header (kolomnamen) in
    headers = next(reader)

    # Voeg de rijen toe aan de data lijst
    for row in reader:
        data.append(row)

# Toon de gegevens in een nette tabel met tabulate
print(tabulate(data, headers=headers, tablefmt='grid'))


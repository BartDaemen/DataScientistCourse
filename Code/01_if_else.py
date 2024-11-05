# Schrijf een programma om te zien of een getal deelbaar is door 2

getal = input("Geef een getal in")

if int(getal)%2 ==0:
    print(getal, "is een even getal")
else:
    print(getal, "is een oneven getal")

#Schrijf een programma waarin de gebruiker euro kan omzetten naar dollar of pond doe de conversie(rond af op 2 cijfers)

euro = input("Geef bedrag in euro")
dollar = float(euro) * 1.11
print(round(dollar,2))

#Schrijf een programma dat de brandstofprijs geeft, de gebruiker kiest tussen diesel of benzine, de gebruiker geeft het aantal liter in. Brandstofprijzen zijn hardcoded

liter = int(input("Geef het aantal liter"))
keuze = input("Tank je diesel of benzine?")
if keuze.upper() == "DIESEL":
    print(liter*2)
elif keuze.upper() == "BENZINE":
    print(liter*1)
else:
    print("ongeldige keuze")

### deelbaar geoptimaliseerd 
getal = int(input("geef een getal in\n"))
deelbaar = []

for x in range(1,getal+1):
    if getal%x == 0:
        deelbaar.append(x)
print(f"{getal} is deelbaar door {deelbaar}")

"""Schrijf een programma dat bepaald of een woord lang of kort is
Minder dan 4 letters: heel kort
Tussen 4 en 6 letters: kort
Tussen 6 en 10 letter: gemiddeld
Meer dan 10: Lang
"""

woord = input("geef je woord")
if len(woord) < 4:
    print("heel kort")
elif len(woord) < 6:
    print("kort")
elif len(woord) < 10:
    print("gemiddeld")
else:
    print("lang")

Schrijf een programma dat zegt of een hoek, stomp scherp of recht is.
uitbreiding hoek moet kleiner dan 360°

hoek = input("geef hoek op?")
if int(hoek) < 90:
    print("scherp")
elif int(hoek) == 90:
    print("recht")
else:
    print("stomp")

"""Schrijf een programma dat feedback geeft op het gemiddelde van 3 cijfer tussen 1 en 10
< 5 gemiddelde: gebuisd
Tussen 5 en 8, geslaagd
> 8 geslaagd met onderscheiding"""

gA=input("getalA")
gB=input("getalB")
gC=input("getalC")
gem = (int(gA) + int(gB) + int(gC)) / 3
if gem <5:
    print("gebuisd")
elif gem <8:
    print("geslaagd")
elif gem >= 8 :
   print("onderscheiding")
else: print("fout")

#schrijf een programma dat zegt een getal deelbaar is door 2, 3, 5, 7, 10

getal = int(input("geef een getal in"))
deelbaar = []
print(getal)
if getal%2 == 0:
    deelbaar.append(2)
if getal%5 == 0:
    deelbaar.append(5)
if getal%7 == 0:
    deelbaar.append(7)
if getal%10 == 0:
    deelbaar.append(10)

print(f"het getal {getal} is deelbaar door {deelbaar}")

# door welke getallen is een getal deelbaar?
def deelbaar(getal):
    delers = [2,3,5,7,10,100]
    for i in delers:
        if getal%i ==0:
            print(f"getals is deelbaar door {i}")

deelbaar(700)


"""Schrijf een functie dat 100 willekeurige getallen genereerd van 10 tot 200.
Gegenereerd Getal 1,5,9,13 … komen in lijst_1
Gegenereerd Getal 2,6,10,14 … komen in lijst_2
Gegenereerd Getal 3,7,11,15 … komen in lijst_3
Gegenereerd Getal 4,8,12,16 … komen in lijst_4
"""

import random

lijst = [["lijst_1:"],["lijst_2:"],["lijst_3:"],["lijst_4:"]]
for i in range(0,100):
    x = random.randint(10,200)
    if x%4==1:
        lijst[0].append(x)
    elif x%4==2:
        lijst[1].append(x)
    elif x%4==3:
        lijst[2].append(x)
    elif x%4==0:
        lijst[3].append(x)

for rij in lijst:
    for _ in rij:
        print(_, end="\t")
    print("")

#Schrijf een programma dat 3 getallen met elkaar optelt

getal1 = input("Geef eerste getal")
getal2 = input ("Geef tweede getal")
getal3 = input("Geef derde getal")
som = int(getal1) + int(getal2) + int(getal3)
print("de som van de drie getallen is", som)

#Schrijf een dat het gemiddelde van 4 ingegeven getallen geeft

X1 = input("Geef eerste getal")
X2 = input ("Geef tweede getal")
X3 = input("Geef derde getal")
X4 = input("Geef vierde getal")
gemiddelde = (int(X1) + int(X2) + int(X3) + int(X4)) / 4
print("het gemiddelde van de vier getallen is", gemiddelde)

#Schrijf een programma dat omtrek van een rechthoek toont
basis = 4
hoogte = 5
omtrek = (basis + hoogte)*2
print("de omtrek van de rechthoek is", omtrek)

#Schrijf een programma dat de inhoud van een balk berekent
l = 5
b = 6
h = 5
inhoud = l*b*h
print("de inhoud van de balk is", inhoud)

#Schrijf een programma dat de inhoud van een kegel berekent
import math
straal = input("geef de straal in")
hoogte_kegel = input("geef de hoogte in")
kegel = int(straal)*math.pi*1/3*int(hoogte_kegel)
print(kegel)

# Naar boven of beneden afronden

import math
x=4.2343242
print(math.floor(x))
print(math.ceil(x))
#naar boven of beneden afronden

print(round(x,2))
#variabele, aantal decimalen

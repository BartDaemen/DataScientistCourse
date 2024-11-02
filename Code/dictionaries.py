#Aanmaken van: dict = {:}

data = {"naam":"Bart", "leeftijd":42} #key - value
print(type(data)) # <class 'dict'>
print(data)

print(data["naam"])
print(data["leeftijd"])

for item in data.keys():
    print(item)


for item in data.values():
    print(item)

for k,v in data.items():
    print(k,v)

#item toevoegen

data["woonplaats"] = "Pelt"

for k,v in data.items():
    print(k,v)

#verwijderen
data.pop("naam")

for k,v in data.items():
    print(k,v)

#item wijzigen:

data["woonplaats"]= "3900"



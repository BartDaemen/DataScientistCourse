###  **** JUISTE MODULES LADEN ****

	# import csv: csv wordt geïmporteerd om het CSV-bestand te kunnen inlezen
	# from tabulate import tabulate: tabulate wordt geïmporteerd om de gegevens als tabel weer te geven.

import csv
from tabulate import tabulate

### **** CSV INLADEN ****
	# bronbestand geeft het pad aan naar het CSV-bestand dat ingelezen moet worden.

bronbestand = 'imdb_movie_dataset.csv'

	# data is een lege lijst waarin de rijen van het CSV-bestand worden opgeslagen. 
	# headers is een lege lijst waarin de kolomnamen worden opgeslagen (de eerste regel van het bestand).
	# indien geen headers in bestand, handmatig definiëren, bijv. headers=["naam", "geslacht", "leeftijd"]

data = []
headers = []

	# Het CSV-bestand wordt geopend in leesmodus ('r') met UTF-8 encoding (is een standaard encoding).
	# csv.reader(file) leest het bestand regel voor regel
	# headers = next(reader) leest de eerste rij, die de kolomnamen bevat, en slaat deze op in de headers-lijst.

with open(bronbestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        data.append(row)

### **** DATA TONEN ****

	# toon_data() is een functie die tabulate() gebruikt om data te tonen als een tabel
	# tabulate(data, headers=headers, tablefmt='grid') formatteert de data als een tabel met een "grid"-stijl met headers bovenaan
	# andere tableformats: 'plain', 'simple', 'grid', 'fancy_grid', 'html', ...
	
def toon_data():
    print(tabulate(data, headers=headers, tablefmt='grid')) 

	# toon_data(): Deze regel roept de toon_data()-functie aan, die de tabel afdrukt met de gegevens uit het CSV-bestand.

toon_data()

### **** NIEUWE RIJ TOEVOEGEN ****

	# def rij_toevoegen(): De functie rij_toevoegen wordt gedefinieerd.
	# nieuwe_rij = []: nieuwe_rij is een lege lijst. Elk veld dat de gebruiker invoert, wordt aan deze lijst toegevoegd.
	# for header in headers: Doorloopt elke kolomnaam (header) in de headers-lijst. headers bevat de kolomnamen van de dataset
	# nieuwe_rij.append(waarde): De ingevoerde waarde wordt aan de nieuwe_rij-lijst toegevoegd. 
	# data.append(nieuwe_rij): Nadat alle kolommen zijn ingevuld, wordt nieuwe_rij toegevoegd aan data

def rij_toevoegen():
    nieuwe_rij = []
    print("\nVoer de gegevens in voor de nieuwe rij:")
    for header in headers:
        waarde = input(f"Voer {header} in: ")
        nieuwe_rij.append(waarde)
    data.append(nieuwe_rij)
    toon_data()

rij_toevoegen()

### **** RIJ VERWIJDEREN ****

	# def verwijder_rij(): De functie verwijder_rij wordt gedefinieerd. 
	# zoekterm = input(f"Voer het item in dat je wenst te verwijderen: "): Deze regel vraagt de gebruiker om een zoekterm in te voeren. 
	# index_te_verwijderen = None: Deze variabele wordt geïnitialiseerd met None. Als de zoekterm gevonden wordt, wordt index_te_verwijderen de positie (index) van de gevonden rij.
	# for i, row in enumerate(data): Doorloopt elke rij (row) in data, waarbij i de index van de rij is.
	# if zoekterm in row: Controleert of de zoekterm in de huidige rij (row) voorkomt.
	# index_te_verwijderen = i en break: Als de zoekterm wordt gevonden, slaat de code de index van de rij (i) op in index_te_verwijderen en stopt de zoeklus (break)
	# break omdat de rij die verwijderd moet worden is gevonden.
	
	# if index_te_verwijderen is not None: Controleert of index_te_verwijderen een waarde heeft gekregen (de zoekterm is gevonden in data).
	# print(f"item gevonden en verwijderd: {data[index_te_verwijderen]}"): Laat een bericht zien met de inhoud van de rij die gevonden is en verwijderd zal worden.
	# del data[index_te_verwijderen]: Verwijdert de rij uit data op basis van de gevonden index.
	# toon_data(): Roept een functie aan om de bijgewerkte dataset te tonen.
	# else: Als index_te_verwijderen None is (de zoekterm werd niet gevonden), drukt de code het bericht af "Geen item gevonden met de opgegeven naam.".

def verwijder_rij():
    print("\nHuidige lijst:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    zoekterm = input(f"Voer het item in dat je wenst te verwijderen: ")
    index_te_verwijderen = None
    for i, row in enumerate(data):
        if zoekterm in row: # alternatief als je enkel in bepaalde kolom wil zoeken: row[0] == zoekterm
            index_te_verwijderen = i
            break

    if index_te_verwijderen is not None:
        print(f"item gevonden en verwijderd: {data[index_te_verwijderen]}")
        del data[index_te_verwijderen]
        toon_data()

    else:
        print("Geen item gevonden met de opgegeven naam.")

verwijder_rij()

### **** RIJEN FILTEREN ****
	# gefilterde_data wordt geïnitialiseerd als een lege lijst om de gefilterde rijen op te slaan.
	# De gebruiker wordt gevraagd om een kolomnaam (filter) en een filterwaarde (filter_waarde).
	# if filter not in headers:gecontroleerd of de opgegeven kolomnaam (filter) daadwerkelijk bestaat in de headers van de dataset. 
	# Als de kolomnaam niet geldig is, wordt een foutmelding getoond en stopt de functie.
	# kolom_index = headers.index(filter): index van de kolom bepaald op basis van de kolomnaam. Deze index wordt gebruikt om te verwijzen naar de juiste kolom in elke rij.
	# for rij in data: Voor elke rij vergelijkt if rij[kolom_index] == filter_waarde de waarde in de kolom met filter_waarde. Als ze overeenkomen, wordt de rij toegevoegd aan gefilterde_data.

def toon_data_met_kenmerk():
    gefilterde_data = []
    
    filter = input(f"Geef de kolom waarin je wilt filteren ({', '.join(headers)}): ")
    filter_waarde = input("Geef de waarde van het kenmerk om te filteren: ")
    
    if filter not in headers:
        print("Deze kolom bestaat niet in de data.")
        return
    
    kolom_index = headers.index(filter)
    
    for rij in data:
        if rij[kolom_index] == filter_waarde:
            gefilterde_data.append(rij)

    if gefilterde_data:
        print(f"\nItems met kenmerk '{filter_waarde}' in kolom '{filter}':")
        print(tabulate(gefilterde_data, headers=headers, tablefmt="grid"))
    else:
        print(f"\nGeen items gevonden met kenmerk '{filter_waarde}' in kolom '{filter}'.")

toon_data_met_kenmerk()

### **** ITEMS AANPASSEN ****
	# zoekterm = input("Geef de ID van de rij die je wilt aanpassen: "):vraagt de gebruiker om de ID van de rij die ze willen aanpassen.

def pas_item_aan():
    print("\nHuidige lijst:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    zoekterm = input("Geef de ID van de rij die je wilt aanpassen: ")

    # index_te_aanpassen wordt ingesteld op None om aan te geven dat we nog geen rij hebben gevonden om aan te passen.
    index_aan_te_passen = None


# Met enumerate(data) doorloop je elke rij in data, waarbij i de index is en row de inhoud van de rij.
# if row[0] == zoekterm controleert of de eerste kolom van de rij (row[0]) overeenkomt met de ingevoerde zoekterm. 
# Dit gaat ervan uit dat de ID zich in de eerste kolom bevindt [0]. Pas aan indien andere kolom.
# Als er een match is, wordt de index (i) opgeslagen in index_te_aanpassen en wordt de loop onderbroken met break.

    for i, row in enumerate(data):
        if row[0] == zoekterm:
            index_aan_te_passen = i
            break

    if index_aan_te_passen is not None:
        item_aan_te_passen = input(f"Welke element wil je aanpassen? ({', '.join(headers)}): ")

        if item_aan_te_passen not in headers:
            print("Ongeldige kolomnaam. Probeer opnieuw.")
            return

        nieuwe_input = input(f"Voer het nieuwe {item_aan_te_passen} in: ")

    # kolom_index wordt ingesteld op de index van de opgegeven kolomnaam, zodat we deze kunnen gebruiken om de waarde in data bij te werken.
        kolom_index = headers.index(item_aan_te_passen)

    # De waarde in data op de gevonden index (index_te_aanpassen) en de specifieke kolom (kolom_index) wordt vervangen door de nieuwe waarde (nieuwe_input).
        data[index_aan_te_passen][kolom_index] = nieuwe_input
        print(f"{item_aan_te_passen} is aangepast naar: {nieuwe_input}")
    else:
        print("Geen item gevonden met de opgegeven ID.")

pas_item_aan()

### **** RIJEN SORTEREN ****
	# sorteer_kenmerk: De functie vraagt de gebruiker om de naam van de kolom waarop ze willen sorteren.
	# kenmerk_index = hier wordt de index van de opgegeven kolomnaam (sorteer_kenmerk) in de lijst van headers opgeslagen in de variabele kenmerk_index. 
	# Dit is nodig om te weten welke waarde in elke rij gebruikt moet worden voor de sorteervolgorde.
	# sorted: De sorted() functie sorteert de data-lijst op basis van de waarden in de opgegeven kolom. 
	# De key parameter specificeert dat de sortering moet plaatsvinden op basis van de waarde in de kolom die overeenkomt met kenmerk_index.
	# lambda: lambda x: x[kenmerk_index] is een anonieme functie die elke rij (x) accepteert en de waarde in de kolom op kenmerk_index retourneert. Dit is de waarde waarop de sortering wordt uitgevoerd.

def sorteer_op_kenmerk():
    sorteer_kenmerk = input(f"Geef de kolom waarop je wil sorteren ({', '.join(headers)}): ")
    kenmerk_index = headers.index(sorteer_kenmerk)

    gesorteerde_data = sorted(data, key=lambda x: x[kenmerk_index]) # voeg ", reverse=True terug op aflopend te sorteren

    print("\nGesorteerde lijst op {sorteer_kenmerk}:")
    print(tabulate(gesorteerde_data, headers=headers, tablefmt='grid'))
    return gesorteerde_data

sorteer_op_kenmerk()

### *** DATA WEGSCHRIJVEN ***
	# exportfile = : Hier wordt de naam van het exportbestand gedefinieerd. In dit geval zal de data worden opgeslagen in een bestand genaamd "data_sorted.csv". 
	# Dit bestand wordt in de huidige werkdirectory gemaakt of overschreven als het al bestaat.
	# with open(exportfile, mode='w', newline='', encoding='utf-8') as file: 
		# mode='w': Dit geeft aan dat het bestand geopend moet worden voor schrijven. Als het bestand al bestaat, wordt het overschreven.
		# newline='': Dit voorkomt extra lege regels bij het schrijven naar een CSV-bestand, wat een veelvoorkomend probleem kan zijn bij het werken met CSV in Python.
	# writer.writerow(headers): Deze regel schrijft de kolomnamen (headers) naar de eerste rij van het CSV-bestand. 
	# writerow() schrijft een enkele rij, en headers is een lijst met de namen van de kolommen.
	# writer.writerows(exportdata): (exportdata) naar het CSV-bestand geschreven. writerows() schrijft meerdere rijen in één keer

def schrijf_data_weg():
    exportfile = "data_sorted.csv"
    exportdata = sorteer_op_kenmerk()
    with open(exportfile, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Schrijf de headers
        writer.writerow(headers)

        # Schrijf alle data
        writer.writerows(exportdata)
    print("\nDe bijgewerkte gegevens zijn succesvol opgeslagen in het bestand.")

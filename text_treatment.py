""" Programme python de prétraitement des données
Auteurs : Gabriel PRIEUR, Adrien RIVET
"""

"""----------IMPORTATTION DES MODULES ET FONCTIONS EXTERNES----------"""
import os


"""----------DECLARATION DES FONCTIONS UTILISATEUR----------"""

# Fonction : Extraire les noms des présidents depuis les noms des fichiers dans le dossier "speeches"
# Pour cela, cette fonction supprime l'extension ".jpg", le numéro et la chaîne de caracyères "Nomination_"
def extract_president_name(file_name):
    file_name_without_extension = file_name[:-4]
    file_name_elements = file_name_without_extension.split("_")
    name = file_name_elements[-1]
    last_character = name[-1]
    if "0" <= last_character <= "9":
        name = name[:-1]
    return name

# Fonction : Prétraiter les textes
# Pour cela, cette fonction met tous les caractères alphabétiques en minuscule, supprime les caractères spéciaux, sépare chaque token d'un espace et s'assure qu'il n'y ait pas 2 espaces de suite
def text_formating(file_name):
    with open(f"speeches\\{file_name}", "r") as f, open(f"cleaned\\cleaned_{file_name}", "w+") as f2:
        last_character = ""
        for ligne in f:
            for character in ligne:
                if 97 <= ord(character) <= 122:
                    f2.write(character)
                    last_character = character
                elif 65 <= ord(character) <= 90:
                    f2.write(chr(ord(character)+32))
                    last_character = chr(ord(character)+32)
                elif 0 <= ord(character) <= 64 or 91 <= ord(character) <= 96 or 123 <= ord(character) <= 127:
                    if last_character != " ":
                        f2.write(" ")
                        last_character = " "
                else:
                    f2.write(character)
                    last_character = character


"""----------CORPS DU PROGRAMME PRINCIPAL----------"""

# Extraire les noms des fichiers textes du dossier "speeches"
folder_path = "speeches"
files_list = os.listdir(folder_path)

# Extraire les noms des présidents depuis les noms des fichiers
president_name_list = []
for file in files_list:
    president_name = extract_president_name(file)
    if president_name not in president_name_list:
        president_name_list.append(president_name)

# Créer un dictionnaire qui associe un prénom au nom de chaque président
presidents_dict = {
    "Chirac": "Jacques",
    "Giscard dEstaing": "Valéry",
    "Hollande": "François",
    "Macron": "Emmanuel",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas"}

# Afficher l'association du nom/prénom de chaque président
print("Liste des noms des présidents :")
firstname = ""
for name in president_name_list:
    if name in presidents_dict:
        firstname = presidents_dict[name]
    print(f"{firstname} {name}")

# Prétraiter les textes
for file in files_list:
    text_formating(file)

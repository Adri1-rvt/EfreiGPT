""" Programme python de prétraitement des données
Programmeurs : Gabriel PRIEUR, Adrien RIVET
Version : 1.2
"""

"""----------IMPORTATION DES MODULES ET FONCTIONS EXTERNES----------"""
import os

"""----------DECLARATION DES FONCTIONS UTILISATEUR----------"""

# Fonction : extraire les noms des présidents depuis les noms des fichiers dans le dossier "speeches"
# Fonctionnement : supprimer l'extension ".jpg", le numéro et la chaîne de caractères "Nomination_" pour conserver uniquement le nom de famille du président. Ensuite, associer chaque nom à un prénom grâce à un dictionnaire
# Argument d'entrée : nom de fichier
# Sortie : nom complet du président
def extract_president_name(file_name):
    """
    :param file_name:
    :return: full_name
    """
    file_name_without_extension = file_name[:-4]   # Supprimer l'extension ".txt"
    file_name_elements_list = file_name_without_extension.split("_")   # Séparer la chaîne à partir du "_"
    name = file_name_elements_list[-1]   # Conserver le nom du président
    last_character = name[-1]
    full_name = ""
    if "0" <= last_character <= "9":
        name = name[:-1]   # Supprimer le numéro à la suite du nom s'il y en a un
    presidents_dict = {   # Créer un dictionnaire associant chaque nom de président à son prénom
        "Chirac": "Jacques",
        "Giscard dEstaing": "Valéry",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Mitterrand": "François",
        "Sarkozy": "Nicolas"}
    firstname = presidents_dict[name]
    full_name = firstname + " " + name   # Associer le prénom et le nom du président
    return full_name

# Fonction : prétraiter les textes
# Fonctionnement : mettre tous les caractères alphabétiques en minuscule, supprimer les caractères spéciaux, séparer chaque token d'un espace et s'assurer qu'il n'y ait pas 2 espaces de suite
# Argument d'entrée : nom de fichier
def text_formating(file_name):
    """
    :param file_name:
    """
    with open(f"speeches\\{file_name}", "r") as f, open(f"cleaned\\cleaned_{file_name}", "w+") as fcleaned:
        last_character = ""   # Créer une variable qui s'assurera qu'il n'y ai pas 2 espaces de suite
        for line in f:
            for character in line:
                if 97 <= ord(character) <= 122:
                    fcleaned.write(character)   # Réécrire le caractère s'il s'agit d'une minuscule
                    last_character = character
                elif 65 <= ord(character) <= 90:
                    fcleaned.write(chr(ord(character)+32))   # Conversion en minuscule puis écriture du caractère s'il s'agit d'une majuscule
                    last_character = chr(ord(character)+32)
                elif 0 <= ord(character) <= 64 or 91 <= ord(character) <= 96 or 123 <= ord(character) <= 127:
                    if last_character != " ":   # Vérifier que le dernier caractère ne soit pas déjà un espace
                        fcleaned.write(" ")   # Convertir en espace puis écrir s'il s'agit d'un caractère spécial
                        last_character = " "
                else:
                    fcleaned.write(character)   # Réécrire le caractère s'il s'agit d'un caractère avec accent
                    last_character = character


"""----------CORPS DU PROGRAMME PRINCIPAL----------"""

# Extraire les noms des fichiers textes présents dans le dossier "speeches"
file_name_list = os.listdir("speeches")

# Prétraiter les textes
for file in file_name_list:
    text_formating(file)

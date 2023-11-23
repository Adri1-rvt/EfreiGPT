""" Programme python principal
Auteurs : Gabriel PRIEUR, Adrien RIVET
"""


"""----------IMPORTATTION DES MODULES ET FONCTIONS EXTERNES----------"""
import time

"""----------DECLARATION DES FONCTIONS UTILISATEUR----------"""


"""----------CORPS DU PROGRAMME PRINCIPAL----------"""


print("""
  ______  __          _    _____ _____ _______ 
 |  ____|/ _|        (_)  / ____|  __ \__   __|
 | |__  | |_ _ __ ___ _  | |  __| |__) | | |   
 |  __| |  _| '__/ _ \ | | | |_ |  ___/  | |   
 | |____| | | | |  __/ | | |__| | |      | |   
 |______|_| |_|  \___|_|  \_____|_|      |_| v1.1
""")
print("-----Bonjour et bienvenue sur EfreiGPT !-----")

time.sleep(1)

message = "Que désirez-vous faire ?"
for letter in message:
    print(letter, end="")
    time.sleep(0.1)
print()
time.sleep(1)
fonctionality_list = ["Afficher la liste des mots les moins importants dans le corpus de documents",
                      "Afficher le mot ayant le score TF-IDF le plus élevé",
                      "Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac",
                      "Indiquer les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois",
                      "Indiquer le premier président à parler du climat et/ou de l’écologie",
                      "Hormis les mots dits « non importants », quels sont les mots que tous les présidents ont évoqués"]
cpt = 1
for fonctionnality in fonctionality_list:
    print(f"{cpt}- {fonctionnality}")
    cpt += 1
    time.sleep(0.5)

print("---------------------------------------------")
number = int(input("Tapez le numéro choisi : "))
while number <= 0 or number > 6:
    number = int(input("Tapez le numéro choisi : "))

if number == 1:
    print(f"Vous avez choisi : {fonctionality_list[1]}\n"+
          "Réponse :")
elif number == 2:
    print(f"Vous avez choisi : {fonctionality_list[2]}\n"+
          "Réponse :")
elif number == 3:
    print(f"Vous avez choisi : {fonctionality_list[3]}\n"+
          "Réponse :")
elif number == 4:
    print(f"Vous avez choisi : {fonctionality_list[4]}\n"+
          "Réponse :")
elif number == 5:
    print(f"Vous avez choisi : {fonctionality_list[5]}\n"+
          "Réponse :")
elif number == 6:
    print(f"Vous avez choisi : {fonctionality_list[6]}\n"+
          "Réponse :")

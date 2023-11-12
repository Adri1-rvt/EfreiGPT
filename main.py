""" Programme python principal
Auteurs : Gabriel PRIEUR, Adrien RIVET
Version : 2
"""

"""----------IMPORTATTION DES MODULES ET FONCTIONS EXTERNES----------"""
import tfidf_matrice_calculation

"""----------DECLARATION DES FONCTIONS UTILISATEUR----------"""


"""----------CORPS DU PROGRAMME PRINCIPAL----------"""


print("""
  ______  __          _    _____ _____ _______ 
 |  ____|/ _|        (_)  / ____|  __ \__   __|
 | |__  | |_ _ __ ___ _  | |  __| |__) | | |   
 |  __| |  _| '__/ _ \ | | | |_ |  ___/  | |   
 | |____| | | | |  __/ | | |__| | |      | |   
 |______|_| |_|  \___|_|  \_____|_|      |_|   
""")
print("-----Bonjour et bienvenue sur EfreiGPT !-----")

fonctionality1 = "Afficher la liste des mots les moins importants dans le corpus de documents"
fonctionality2 = "Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé"
fonctionality3 = "Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac"
fonctionality4 = "Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois"
fonctionality5 = "Indiquer le premier président à parler du climat et/ou de l’écologie"
fonctionality6 = "Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués"


print("Que désirez-vous faire ?\n",
      f"1- {fonctionality1}\n",
      f"2- {fonctionality2}\n",
      f"3- {fonctionality3}\n",
      f"4- {fonctionality4}\n",
      f"5- {fonctionality5}\n",
      f"6- {fonctionality6}")
print("---------------------------------------------")
number = int(input("Tapez le numéro choisi : "))
while number <= 0 or number > 6:
    number = int(input("Tapez le numéro choisi : "))

if number == 1:
    print(f"Vous avez choisi : {fonctionality1}\n"+
          "Réponse :")

    # Obtenir la matrice TF-IDF
    tfidf_matrix = tfidf_matrice_calculation.tfidf_matrix("cleaned")

elif number == 2:
    print(f"Vous avez choisi : {fonctionality2}\n"+
          "Réponse :")
elif number == 3:
    print(f"Vous avez choisi : {fonctionality3}\n"+
          "Réponse :")
elif number == 4:
    print(f"Vous avez choisi : {fonctionality4}\n"+
          "Réponse :")
elif number == 5:
    print(f"Vous avez choisi : {fonctionality5}\n"+
          "Réponse :")
elif number == 6:
    print(f"Vous avez choisi : {fonctionality6}\n"+
          "Réponse :")

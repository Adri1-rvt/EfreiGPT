""" Programme python principal
Programmeurs : Gabriel PRIEUR, Adrien RIVET
Version : 1.2
"""

"""----------IMPORTATION DES MODULES ET FONCTIONS EXTERNES----------"""
import os   # import du module Operating System pour avoir accès aux documents
import time   # import du module time pour créer des animations d'écriture
from text_treatment import text_formating
from tfidf_matrice_calculation import tfidf_matrix, idf_calculation
from fonctionnalites import (
    fonctionnalite1, fonctionnalite2, fonctionnalite3, fonctionnalite4, fonctionnalite5, fonctionnalite6
)
from chat_functions import (
    tokenize_question, intersection_terms, tfidf_vector, most_relevant_document, generate_response, refine_response
)


"""----------CORPS DU PROGRAMME PRINCIPAL----------"""

if __name__ == '__main__':
    # Prétraiter les textes
    for file in os.listdir("speeches"):
        text_formating(file)

    # Obtenir la matrice TF-IDF globale
    tfidf_matrix_result = tfidf_matrix("cleaned")

    # Obtenir la liste des noms de fichiers
    file_names = os.listdir("speeches")

    # ASCII art du magnifique logo du Chatbot
    print("""
     ______  __          _    _____ _____ _______ 
    |  ____|/ _|        (_)  / ____|  __ \__   __|
    | |__  | |_ _ __ ___ _  | |  __| |__) | | |   
    |  __| |  _| '__/ _ \ | | | |_ |  ___/  | |   
    | |____| | | | |  __/ | | |__| | |      | |   
    |______|_| |_|  \___|_|  \_____|_|      |_| v1.2     
        """)
    print("=======================================================\n",
          "Développeurs  :  Gabriel PRIEUR, Adrien RIVET\n",
          "Version       :  v1.2\n",
          "Dernière maj  :  18/12/2023",)
    print("=======================================================\n")
    time.sleep(0.5)

    # Afficher le message d'introduction
    message = ("Bienvenue sur EfreiGPT, le chatBot si bien programmé que son code ne vous Efrei pas ! \nQue désirez-vous faire ?")
    cpt = 1
    for letter in message:
        print(letter, end="")
        cpt += 1
        if cpt % 4 == 0:
            time.sleep(0.1)   # Faire une animation d'affichage
    print()
    time.sleep(0.5)
    print("[1] Accéder au mode Chatbot pour poser une question")
    time.sleep(0.5)
    print("[2] Accéder à des fonctionnalités pré-rédigées")
    time.sleep(0.5)
    print("-------------------------------------------------------")
    number = int(input("Tapez le numéro de la fonctionnalité choisie : "))
    while number <= 0 or number > 2:
        number = int(input("Numéro invalide. Tapez 1 ou 2 : "))

    # Si l'utilisateur tape 1, passer en mode ChatBot
    if number == 1:
        while True:
            question = input("Posez votre question : ")

            if question == "STOP":
                break

            # Tokenisation de la question
            question_words = tokenize_question(question)
            # Intersection des tokens de la question avec ceux du corpus
            common_terms = intersection_terms(question_words, "cleaned")
            # Calcul du vecteur TF-IDF de la question
            idf_scores = idf_calculation("cleaned")
            question_vector = tfidf_vector(question_words, idf_scores)
            # Calcul du document le plus pertinent
            most_relevant_doc = most_relevant_document(question_vector, tfidf_matrix_result, file_names)
            # Récupération du mot avec le score TF-IDF le plus élevé dans la question
            highest_tfidf_word = max(question_vector, key=question_vector.get)
            # Génération de la réponse
            response = generate_response(most_relevant_doc, highest_tfidf_word)
            # Affinage de la réponse
            question_words_list = question.split(" ")
            question_starter = question_words_list[0]

            # Afficher la réponse
            answer = refine_response(question_starter, response)
            if answer != None:
                for letter in answer:
                    print(letter, end="")
                    cpt += 1
                    if cpt % 4 == 0:
                        time.sleep(0.1)
            else:
                print("La question ne semble pas avoir de réponse dans ma base de données")
            print()
            print("-------------------------------------------------------")

    # Si l'utilisateur tape 2, passer en mode questions pré-rédigées
    if number == 2:

        fonctionality_list = ["Afficher la liste des mots les moins importants dans le corpus de documents",
                              "Afficher le mot ayant le score TF-IDF le plus élevé",
                              "Indiquer le mot le plus répété par le président Chirac",
                              "Indiquer les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois",
                              "Indiquer le premier président à parler du climat et/ou de l’écologie",
                              "Hormis les mots dits « non importants », afficher les mots que tous les présidents ont évoqués"]
        question_cpt = 1
        text = "Voici la liste des questions pré-rédigées :"
        cpt = 1
        for letter in text:
            print(letter, end="")
            cpt += 1
            if cpt % 4 == 0:
                time.sleep(0.1)
        print()
        for fonctionnality in fonctionality_list:
            print(f"[{question_cpt}] {fonctionnality}")   # Lister les fonctionnalités
            question_cpt += 1
            time.sleep(0.5)

        while True:
            print("-------------------------------------------------------")
            number = int(input("Tapez le numéro de la question choisie : "))
            while number <= 0 or number > 7:
                number = int(input("Tapez le numéro choisi : "))
            if number == 7:
                break

            # Obtenir la matrice TF-IDF
            tfidf_matrix_result = tfidf_matrix("cleaned")

            # Exécuter la fonctionnalité choisie
            if number == 1:
                fonctionnalite1(tfidf_matrix_result)
            elif number == 2:
                fonctionnalite2(tfidf_matrix_result)
            elif number == 3:
                fonctionnalite3()
            elif number == 4:
                fonctionnalite4(tfidf_matrix_result)
            elif number == 5:
                fonctionnalite5()
            elif number == 6:
                fonctionnalite6(tfidf_matrix_result)

print("\n=======================================================")
print("Merci et à bientôt sur EfreiGPT !")

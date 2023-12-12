""" Programme python principal
Auteurs : Gabriel PRIEUR, Adrien RIVET
Version : 1.2
"""

"""----------IMPORTATTION DES MODULES ET FONCTIONS EXTERNES----------"""
import os
import time
from text_treatment import text_formating
from tfidf_matrice_calculation import tfidf_matrix, idf_calculation
from fonctionnalites import (
    fonctionnalite1, fonctionnalite2, fonctionnalite3, fonctionnalite4, fonctionnalite5, fonctionnalite6
)
from chat_functions import (
    tokenize_question, intersection_terms, tfidf_vector,
    cosine_similarity, most_relevant_document, generate_response, refine_response
)


"""----------CORPS DU PROGRAMME PRINCIPAL----------"""

if __name__ == '__main__':
    # Prétraiter les textes
    for file in os.listdir("speeches"):
        text_formating(file)

    # Obtenir la matrice TF-IDF
    tfidf_matrix_result = tfidf_matrix("cleaned")

    # Obtenez la liste des noms de fichiers
    file_names = os.listdir("speeches")

    # ASCII art du logo du Chatbot
    print("""
     ______  __          _    _____ _____ _______ 
    |  ____|/ _|        (_)  / ____|  __ \__   __|
    | |__  | |_ _ __ ___ _  | |  __| |__) | | |   
    |  __| |  _| '__/ _ \ | | | |_ |  ___/  | |   
    | |____| | | | |  __/ | | |__| | |      | |   
    |______|_| |_|  \___|_|  \_____|_|      |_| v1.2     
        """)
    print("-----Bonjour et bienvenue sur EfreiGPT !-----")
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

    print("1- Accéder au mode Chatbot pour poser une question")
    time.sleep(0.5)
    print("2- Accéder à des fonctionnalités pré-rédigées")
    time.sleep(0.5)
    print("---------------------------------------------")
    number = int(input("Tapez le numéro de la fonctionnalité choisie : "))
    while number <= 0 or number > 2:
        number = int(input("Numéro invalide. Tapez le numéro choisi : "))

    if number == 1:
        question = str(input("Posez votre question : "))

        # Tokenisation de la question
        question_words = tokenize_question(question)
        print(question_words)

        # Intersection avec le corpus
        common_terms = intersection_terms(question_words, "cleaned")
        print(common_terms)

        # Calcul du vecteur TF-IDF de la question
        idf_scores = idf_calculation("cleaned")
        question_vector = tfidf_vector(question_words, idf_scores)
        print(question_vector)

        # Calcul du document le plus pertinent
        most_relevant_doc = most_relevant_document(question_vector, tfidf_matrix_result, file_names)
        print(most_relevant_doc)

        # Récupération du mot avec le score TF-IDF le plus élevé dans la question
        highest_tfidf_word = max(question_vector, key=question_vector.get)
        print(highest_tfidf_word)

        # Génération de la réponse
        response = generate_response(most_relevant_doc, highest_tfidf_word)
        print(response)

        # Affinage de la réponse
        question_starter = " ".join(question_words[:2])
        refined_response = refine_response(response, question_starter)

        print(refined_response)



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
            print(f"{question_cpt}- {fonctionnality}")   # Lister les fonctionnalités
            question_cpt += 1
            time.sleep(0.5)

        while True:
            print("---------------------------------------------")
            number = int(input("Tapez le numéro de la question choisie : "))
            while number <= 0 or number > 6:
                number = int(input("Tapez le numéro choisi : "))

            # Obtenir la matrice TF-IDF
            tfidf_matrix_result = tfidf_matrix("cleaned")

            # Fonctionnalités
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

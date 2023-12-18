""" Programme python des fonctionnalités pré-rédigées
Programmeurs : Gabriel PRIEUR, Adrien RIVET
Version : 1.2
"""

"""----------IMPORTATION DES MODULES ET FONCTIONS EXTERNES----------"""
from tfidf_matrice_calculation import tf_calculation
from text_treatment import extract_president_name
import os
import time

"""----------DECLARATION DES FONCTIONS UTILISATEUR----------"""

# Fonction : afficher la liste des mots les moins importants dans le corpus de documents
# Fonctionnement : faire une liste avec les mots ayant un score TF-IDF = 0, puis les afficher s'ils sont = 0 dans tous les documents et qu'ils apparaissent donc 8 fois dans la liste
# Argument d'entrée : matrice TF-IDF
def fonctionnalite1(tfidf_matrix_result):
    """
    :param tfidf_matrix_result:
    """
    print("Question choisie : Afficher la liste des mots les moins importants dans le corpus de documents")
    print("Réponse :", end=" ")
    L = []
    for tfidf_scores in tfidf_matrix_result:
        for word in tfidf_scores:
            if tfidf_scores[word] == 0:
                L.append(word)
    answer = "Les mots les moins importants sur le corpus de documents sont : "
    for element in set(L):
        answer += f'"{element}", '
    cpt = 1
    for letter in answer:
        print(letter, end="")
        cpt += 1
        if cpt % 4 == 0:
            time.sleep(0.1)
    print()

# Fonction : afficher le mot ayant le score TF-IDF le plus élevé
# Fonctionnement : parcourir l'entièreté de la matrice TF-IDF et afficher le mot dont la valeur est la plus élevée
# Argument d'entrée : matrice TF-IDF
def fonctionnalite2(tfidf_matrix_result):
    """
    :param tfidf_matrix_result:
    """
    print("Question choisie : Afficher le mot ayant le score TF-IDF le plus élevé")
    print("Réponse :", end=" ")
    max_tfidf = 0
    max_word = ""
    for tfidf_scores in tfidf_matrix_result:
        for word in tfidf_scores:
            if tfidf_scores[word] > max_tfidf:
                max_tfidf = tfidf_scores[word]
                max_word = word
    answer = f'Le mot ayant le score TF-IDF le plus élevé est le mot "{max_word}", qui a un score TF-IDF égal à {max_tfidf} (énorme !).'
    cpt = 1
    for letter in answer:
        print(letter, end="")
        cpt += 1
        if cpt % 4 == 0:
            time.sleep(0.1)
    print()

# Fonction : indiquer le mot le plus répété par le président Chirac
# Fonctionnement : parcourir l'ensemble des discours de Chirac, créer un dictionnaire de chacun des mots prononcé et afficher le mot dont la valeur est la plus grande
def fonctionnalite3():
    print("Question choisie : Indiquer le mot le plus répété par le président Chirac")
    print("Réponse :", end=" ")
    most_repeated_frequency = 0
    most_repeated_word = ""
    text_list = os.listdir("cleaned")
    most_repeated_frequency_final = 0
    for text in text_list:
        if "Chirac" in text:
            with open(f"cleaned\\{text}", "r") as f:
                word_frequency = {}
                elements = f.read()
                words = elements.split()
                for word in words:
                    if word in word_frequency:
                        word_frequency[word] += 1
                    else:
                        word_frequency[word] = 1
                for word, frequency in word_frequency.items():
                    if frequency > most_repeated_frequency:
                        most_repeated_frequency = frequency
                        most_repeated_word = word
                most_repeated_frequency_final += most_repeated_frequency
    answer = f'Le mot le plus répété par le président Chirac est le mot "{most_repeated_word}", qu\'il a prononcé exactement {most_repeated_frequency_final} fois.'
    cpt = 1
    for letter in answer:
        print(letter, end="")
        cpt += 1
        if cpt % 4 == 0:
            time.sleep(0.1)
    print()

# Fonction : indiquer les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois
# Fonctionnement : parcourir les dicours des présidents, détecter lorsque le mot "nation" a été prononcé, compter le nombre de fois où le mot a été prononcé par chaque président et afficher celui qui l'a le plus dit
# Argument d'entrée : matrice TF-IDF
def fonctionnalite4(tfidf_matrix_result):
    """
    :param tfidf_matrix_result:
    """
    print("Question choisie : Indiquer les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois")
    print("Réponse :", end=" ")
    nation_pronounced = {}
    maximum = 0
    text_list = os.listdir("cleaned")
    for text_name in text_list:
        with open(f"cleaned\\{text_name}", "r") as f:
            tf = tf_calculation(f)
            if "nation" in tf.keys():
                president_name = extract_president_name(text_name)
                if president_name in nation_pronounced:
                    nation_pronounced[president_name] += tf["nation"]
                else:
                    nation_pronounced[president_name] = tf["nation"]
                if nation_pronounced[president_name] >= maximum:
                    maximum = nation_pronounced[president_name]
                    president = president_name
    answer = f'Les présidents qui ont parlé de la « Nation » sont '
    for president_name in nation_pronounced.keys():
        answer += f"{president_name}, "
    answer += f"\nC'est le président {president} qui a répété le plus de fois le mot \"Nation\" en le prononçant {maximum} fois."
    cpt = 1
    for letter in answer:
        print(letter, end="")
        cpt += 1
        if cpt % 4 == 0:
            time.sleep(0.1)
    print()

# Fonction : indiquer le premier président à parler du climat et/ou de l’écologie
# Fonctionnement : parcourir les discours des présidents, détecter quand les mot "écologie" ou "climat" apparaissent et afficher le premier président à en avoir parlé historiquement
def fonctionnalite5():
    print("Question choisie : Indiquer le premier président à parler du climat et/ou de l’écologie")
    print("Réponse :", end=" ")
    search_word = "climat"
    search_word2 = "écologie"
    text_list = os.listdir("cleaned")
    ecological_president = ""
    for text_name in text_list:
        with open(f"cleaned\\{text_name}", "r") as f:
            document = f.read()
            word_list = document.split()
            if (search_word in word_list) or (search_word2 in word_list):
                if ecological_president == "":
                    ecological_president = extract_president_name(text_name)
                else:
                    presidents_order = {
                        "Valéry Giscard dEstaing": 1,
                        "François Mitterrand": 2,
                        "Jacques Chirac": 3,
                        "Nicolas Sarkozy": 4,
                        "François Hollande": 5,
                        "Emmanuel Macron": 6}
                    name = extract_president_name(text_name)
                    if presidents_order[name] < presidents_order[ecological_president]:
                        ecological_president = extract_president_name(text_name)
    answer = f"Le premier président à parler du climat et/ou de l’écologie est le président {ecological_president}."
    cpt = 1
    for letter in answer:
        print(letter, end="")
        cpt += 1
        if cpt % 4 == 0:
            time.sleep(0.1)
    print()

# Fonction : hormis les mots dits « non importants », afficher les mots que tous les présidents ont évoqués
# Fonctionnement : regarder les mots que tous les présidents ont prononcé et enlever les mots dont le score TF-IDF = 0 dans tous les documents
# Argument d'entrée : matrice TF-IDF
def fonctionnalite6(tfidf_matrix_result):
    """
    :param tfidf_matrix_result:
    """
    print("Question choisie : Hormis les mots dits « non importants », afficher les mots que tous les présidents ont évoqués")
    print("Réponse :", end=" ")
    common_words = {}
    text_list = os.listdir("cleaned")
    # Fonction : rassembler les discours des présidents qui en ont prononcé plusieurs en un seul
    def concat_files(file1_path, file2_path, output_path, file):
        """
        :param file1_path:
        :param file2_path:
        :param output_path:
        :param file:
        """
        with open(file1_path, 'r') as f, open(file2_path, 'r') as f2:
            content1 = f.read()
            content2 = f2.read()
        global_content = content1 + content2
        with open(output_path, 'w+') as output_file:
            output_file.write(global_content)
        text_list2.append(file)
    text_list2 = []
    file1_path = 'cleaned\\cleaned_Nomination_Chirac1.txt'
    file2_path = 'cleaned\\cleaned_Nomination_Chirac2.txt'
    output_path = 'cleaned_glob\\global_Chirac.txt'
    file = 'global_Chirac.txt'
    file3_path = 'cleaned\\cleaned_Nomination_Mitterrand1.txt'
    file4_path = 'cleaned\\cleaned_Nomination_Mitterrand2.txt'
    output_path2 = 'cleaned_glob\\global_Mitterand.txt'
    file2 = 'global_Mitterand.txt'

    concat_files(file1_path, file2_path, output_path, file)
    concat_files(file3_path, file4_path, output_path2, file2)

    for text_name in text_list:
        with open(f"cleaned\\{text_name}", "r") as f:
            document = f.read()
            word_list = document.split()
            for word in set(word_list):
                if word in common_words.keys():
                    common_words[word] += 1
                else:
                    common_words[word] = 1
    for text_name in text_list2:
        with open(f"cleaned_glob\\{text_name}", "r") as f:
            document = f.read()
            word_list = document.split()
            for word in set(word_list):
                if word in common_words.keys():
                    common_words[word] += 1
                else:
                    common_words[word] = 1
    L = []
    for tfidf_scores in tfidf_matrix_result:
        for word in tfidf_scores:
            if tfidf_scores[word] == 0:
                L.append(word)
    non_important_word = {}
    for element in L:
        if element in non_important_word.keys():
            non_important_word[element] += 1
        else:
            non_important_word[element] = 1
    M = []
    for element in non_important_word:
        if non_important_word[element] == 8:
            M.append(element)
    answer = "Hormis les mots dits « non importants », les mots que tous les présidents ont évoqués sont : "
    for word in common_words:
        if common_words[word] == 8 and word not in M:
            answer += f'"{word}", '
    cpt = 1
    for letter in answer:
        print(letter, end="")
        cpt += 1
        if cpt % 4 == 0:
            time.sleep(0.1)
    print()

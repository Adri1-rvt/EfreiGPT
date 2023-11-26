""" Programme python la créaction de la matrice TF-IDF
Auteurs : Gabriel PRIEUR, Adrien RIVET
Version : 1.1
"""

"""----------IMPORTATTION DES MODULES ET FONCTIONS EXTERNES----------"""
import math
import os
from text_treatment import extract_president_name

"""----------DECLARATION DES FONCTIONS UTILISATEUR----------"""

# Fonction : calculer les scores TF
# Fonctionnement : diviser les textes (traités au préalable) en mot, compter les occurrences de chaque mot et les stocker dans un dictionnaire
# Argument d'entrée : fichier
# Sortie : dictionnaire de la matrice TF du fichier
def tf_calculation(f):
    file_content = f.read()
    words_list = file_content.split()   # Diviser le texte en mot à partir des espaces
    occurrences = {}
    for word in words_list:
        if word in occurrences:
            occurrences[word] += 1   # Si le mot est déjà dans le dictionnaire, ajouter 1 à sa valeur
        else:
            occurrences[word] = 1   # Si le mot n'est pas déjà dans le dictionnaire, l'ajouter et mettre sa valeur à 1
    return occurrences

# Fonction : calculer les scores IDF
# Fonctionnement : compter le nombre de documents du corpus contenant chaque mot, calculer le nombre total de documents, puis calculer l'IDF de chaque mot
# Argument d'entrée : répertoire du fichier contenant les fichiers traités
# Sortie : dictionnaire de la matrice IDF
def idf_calculation(corpus_dir):
    word_count = {}
    number_of_files = len(os.listdir(corpus_dir))   # Compter le nombre de fichiers
    for file_name in os.listdir(corpus_dir):
        with open(f"{corpus_dir}\\{file_name}", 'r') as f:
            file_content = f.read()
            words_list = file_content.split()   # Diviser le texte en mot à partir des espaces
            unique_words = set(words_list)   # Eliminer les doublons en transformant la liste en set
            for word in unique_words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    idf = {}
    words = list(word_count.keys())   # Faire une liste avec les clés du dictionnaire
    counts = list(word_count.values())   # Faire une liste avec les valeurs du dictionnaire
    for i in range(len(words)):
        word = words[i]
        count = counts[i]
        idf[word] = math.log(number_of_files / count)   # Calculer le score IDF et l'enregistrer dans un dictionnaire
    return idf

# Fonction : calculer les scores TF-IDF
# Fonctionnement : utiliser les fonctions de calcul de score TF et de score IDF, faire le calcul TF-IDF = TF*IDF pour chaque mot et enregistrer le score TF-IDF final dans un dictionnaire
# Argument d'entrée : répertoire du fichier contenant les fichiers traités
# Sortie : matrice TF-IDF, un tableau contenant des dictionnaires de scores TF-IDF pour chaque mot du corpus
def tfidf_matrix(corpus_dir):
    tfidf_matrix = []
    idf_scores = idf_calculation(corpus_dir)   # Récupérer le score IDF
    for filename in os.listdir(corpus_dir):
        with open(f"{corpus_dir}\\{filename}", 'r') as f:
            tf_scores = tf_calculation(f)   # Récupérer le score TF du document
            tfidf_scores = {}
            for word in tf_scores:
                tf = tf_scores[word]   # Récupérer le score TF du mot dans le document
                idf = idf_scores[word]   # Récupérer le score IDF du mot
                tfidf_scores[word] = tf * idf   # Calculer le score TF-IDF
            tfidf_matrix.append(tfidf_scores)   # Remplir le tableau avec le dictionnaire de scores TF-IDF du document
    return tfidf_matrix


"""----------CORPS DU PROGRAMME PRINCIPAL----------"""

# Obtenir la matrice TF-IDF
tfidf_matrix_result = tfidf_matrix("cleaned")

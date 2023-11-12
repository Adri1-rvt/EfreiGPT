""" Programme python la créaction de la matrice TF-IDF
Auteurs : Gabriel PRIEUR, Adrien RIVET
"""

"""----------IMPORTATTION DES MODULES ET FONCTIONS EXTERNES----------"""
import math
import os


"""----------DECLARATION DES FONCTIONS UTILISATEUR----------"""

# Fonction : Calculer les scores TF
# Pour cela, cette fonction divise les textes (traités au préalable) en mot, compte les occurrences de chaque mot et les stocke dans un dictionnaire
def tf_calculation(f):
    content = f.read()
    words = content.split()
    occurrences = {}

    for word in words:
        if word in occurrences:
            occurrences[word] += 1
        else:
            occurrences[word] = 1

    return occurrences

# Fonction : Calculer les scores IDF
# Pour cela, cette fonction compte le nombre de documents du corpus contenant chaque mot, calcule le nombre total de documents, puis calcule l'IDF de chaque mot
def idf_calculation(corpus_dir):
    word_doc_count = {}
    total_number_of_files = len(os.listdir(corpus_dir))
    for filename in os.listdir(corpus_dir):
        with open(f"{corpus_dir}\\{filename}", 'r') as file:
            document = file.read()
            words_list = document.split()
            unique_words = set(words_list)

            for word in unique_words:
                if word in word_doc_count:
                    word_doc_count[word] += 1
                else:
                    word_doc_count[word] = 1

    idf = {}
    words = list(word_doc_count.keys())
    counts = list(word_doc_count.values())

    for i in range(len(words)):
        word = words[i]
        count = counts[i]
        idf[word] = math.log(total_number_of_files / count)

    return idf


# Fonction : Calculer les scores TF-IDF
# Pour cela, cette fonction utilise les fonctions de calcul de score TF et de score IDF, fais la calcul TF-IDF = TF*IDF pour chaque mot et enregistre le score TF-IDF final dans un dictionnaire
def tfidf_matrix(corpus_dir):
    tf_matrix = []
    idf_scores = idf_calculation(corpus_dir)

    for filename in os.listdir(corpus_dir):
        with open(f"{corpus_dir}\\{filename}", 'r') as file2:
            tf_scores = tf_calculation(file2)
            tfidf_scores = {}
            for word in tf_scores:
                tf = tf_scores[word]
                idf = idf_scores[word]
                tfidf_scores[word] = tf * idf
            tf_matrix.append(tfidf_scores)

    return tf_matrix


"""----------CORPS DU PROGRAMME PRINCIPAL----------"""

# Obtenir la matrice TF-IDF
tfidf_matrix_result = tfidf_matrix("cleaned")
print(tfidf_matrix_result)

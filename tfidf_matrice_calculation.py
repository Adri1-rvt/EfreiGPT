""" Programme python la créaction de la matrice TF-IDF
Auteurs : Gabriel PRIEUR, Adrien RIVET
"""

"""----------IMPORTATTION DES MODULES ET FONCTIONS EXTERNES----------"""
import math
import os
from text_treatment import extract_president_name

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
    for file_name in os.listdir(corpus_dir):
        with open(f"{corpus_dir}\\{file_name}", 'r') as f:
            document = f.read()
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
        with open(f"{corpus_dir}\\{filename}", 'r') as f:
            tf_scores = tf_calculation(f)
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





"""FONCTIONNALITES A DEVELOPPER"""

#1 Afficher la liste des mots les moins importants dans le corpus de documents
print("\n----------------------------------------------------------------------")
L = []
for tfidf_scores in tfidf_matrix_result:
    for word in tfidf_scores:
        if tfidf_scores[word] == 0:
            L.append(word)
print("Les mots les moins importants sur le corpus de documents sont :", end=" ")

for element in set(L):
    print(f'"{element}",', end=" ")
print()

"""A modifier, le code estime qu'un mot est non-important si son score tfidf = 0 dans un document, or il faut que ce soit le cas dans chaque document"""



#2 Afficher le mot ayant le score TF-IDF le plus élevé
print("\n2----------------------------------------------------------------------")
max_tfidf = 0
max_word = ""
for tfidf_scores in tfidf_matrix_result:
    for word in tfidf_scores:
        if tfidf_scores[word] > max_tfidf:
            max_tfidf = tfidf_scores[word]
            max_word = word

print(f'Le mot ayant le score TF-IDF le plus élevé est le mot "{max_word}", qui a un score TF-IDF égal à {max_tfidf}.')



#3 Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac
print("\n3----------------------------------------------------------------------")
most_repeated_frequency = 0
most_repeated_word = ""

text_list = os.listdir("cleaned")
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

print(f'''Le mot le plus répété par le président Chrirac est le mot "{most_repeated_word}", qu'il a prononcé {most_repeated_frequency} fois.''')



#4 Indiquer les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois
print("\n4----------------------------------------------------------------------")
L = []
maximum = 0
text_list = os.listdir("cleaned")
for text_name in text_list:
    with open(f"cleaned\\{text_name}", "r") as f:
        tf = tf_calculation(f)
        if "nation" in tf.keys():
            president_name = extract_president_name(text_name)
            L.append(president_name)
            if tf["nation"] >= maximum:
                maximum = tf["nation"]
                president = president_name
cpt = 1
print("Les présidents qui ont parlé de la « Nation » sont",end=" ")
for president_name in set(L):
    if cpt == len(set(L))-1:
        print(f"{president_name} et", end=" ")
    elif cpt != len(set(L)):
        print(f"{president_name},", end=" ")
    else:
        print(f"{president_name}.")
    cpt += 1
print(f"C'est le président {president} qui l'a répété le plus de fois.")

"""A modifier : pour les présidents qui ont plusieurs textes, il faut additionner les 2"""



#5 Indiquer le premier président à parler du climat et/ou de l’écologie
print("\n5----------------------------------------------------------------------")
search_word = "climat"
search_word2 = "écologie"
text_list = os.listdir("cleaned")
for text_name in text_list:
    with open(f"cleaned\\{text_name}", "r") as f:
        document = f.read()
        word_list = document.split()
        if (search_word in word_list) or (search_word2 in word_list):
            ecological_president = extract_president_name(text_name)
print(f"Le premier président à parler du climat et/ou de l’écologie est le président {ecological_president}.")

"""A modifier : faire liste odre présidents dans le temps"""



#6 Hormis les mots dits « non importants », quels sont les mots que tous les présidents ont évoqués
print("\n6----------------------------------------------------------------------")
common_words = {}
text_list = os.listdir("cleaned")
for text_name in text_list:
    with open(f"cleaned\\{text_name}", "r") as f:
        document = f.read()
        word_list = document.split()
        for word in set(word_list):
            if word in common_words.keys():
                common_words[word] += 1
            else:
                common_words[word] = 1

print("Hormis les mots dits « non importants », les mots que tous les présidents ont évoqués sont :", end=" ")
for word in common_words:
    if common_words[word] == 8:
        print(f'"{word}",', end=" ")

"""A modifier : pour les présidents qui ont plusieurs textes, il faut additionner les 2"""
"""A modifier : enlever les mots non-importants de la liste"""
""" Programme python des fonctions du chatbot
Programmeurs : Gabriel PRIEUR, Adrien RIVET
Version : 1.2
"""

"""----------IMPORTATION DES MODULES ET FONCTIONS EXTERNES----------"""
import math
import os

"""----------DECLARATION DES FONCTIONS UTILISATEUR----------"""

# Fonction : transformer la question en liste de tokens
# Fonctionnement : séparer la question en liste de caractère, supprimer les caractères spéciaux, convertir les majuscules en minuscules puis reconvertir le tout en mot pour séparer en liste de mots
# Argument d'entrée : chaine de caractères constituée de la question
# Sortie : tableau de tokens
def tokenize_question(question):
    """
    :param question:
    :return: word_list
    """
    letter_list_cleaned = []
    letter_list = list(question)
    for character in letter_list:
        if 97 <= ord(character) <= 122:
            letter_list_cleaned.append(character)
            last_character = character
        elif 65 <= ord(character) <= 90:
            letter_list_cleaned.append(chr(ord(character) + 32))
            last_character = chr(ord(character) + 32)
        elif 0 <= ord(character) <= 64 or 91 <= ord(character) <= 96 or 123 <= ord(character) <= 127:
            if last_character != " ":
                letter_list_cleaned.append(" ")
                last_character = " "
        else:
            letter_list_cleaned.append(character)
            last_character = character
    while letter_list_cleaned and letter_list_cleaned[-1] == " ":
        del letter_list_cleaned[-1]
    question = "".join(letter_list_cleaned)
    word_list = question.split(" ")
    return word_list

# Fonction : trouver les tokens présents dans la question et dans le corpus
# Fonctionnement : supprimer les doublons de la question et faire l'intersection des mots de la question avec les mots du corpus à l'aide du type set
# Arguments d'entrée : liste des mots de la question, répertoire du dossier contenant les fichiers traités
# Sortie : liste des mots présents à la fois dans la question et dans le corpus de documents
def intersection_terms(question_words, corpus_directory):
    """
    :param question_words:
    :param corpus_directory:
    :return: list(common_terms)
    """
    question_set = set(question_words)
    corpus = read_documents(corpus_directory)
    corpus_words = []
    for document in corpus:
        for word in document.split():
            corpus_words.append(word)
    corpus_set = set(corpus_words)
    common_terms = question_set & corpus_set
    return list(common_terms)

# Fonction : calcule le score TF-IDF de la question
# Fonctionnement : supprimer les doublons puis calculer le score TF-IDF de la question à partir du score TF de la question et du score IDF global
# Arguments d'entrée : liste de mots de la question, score IDF
# Sortie : score TF-IDF de la question
def tfidf_vector(words, idf_scores):
    """
    :param words:
    :param idf_scores:
    :return: tf_vector
    """
    tf_vector = {}
    question_words = set(words)
    for word in question_words:
        tf = words.count(word) / len(words)
        if word in idf_scores:
            tf_vector[word] = tf * idf_scores[word]
        else:
            tf_vector[word] = 0
        if word == "comment":
            tf_vector[word] = 0
    return tf_vector

# Fonction : calculer les nomes des vecteurs
# Fonctionnement : itérer à travers les valeurs du vecteur, élever chaque valeur au carré, les additionner, et prendre la racine carrée du résultat
# Argument d'entrée : vecteur
# Sortie : norme du vecteur
def norm(vector):
    """
    :param vector:
    :return: math.sqrt(squared_sum)
    """
    squared_sum = 0
    for value in vector.values():
        squared_sum += value ** 2
    return math.sqrt(squared_sum)

# Fonction : calculer la similarité
# Fonctionnement : calculer le produit scalaire des éléments correspondants des vecteurs, normaliser les vecteurs et renvoyer la similarité cosinus résultante
# Argument d'entrée : vecteurs
# Sortie : similarité cosinus entre les vecteurs
def cosine_similarity(vector_a, vector_b):
    """
    :param vector_a:
    :param vector_b:
    :return: dot_prod / (norm_a * norm_b)
    """
    common_words = set(vector_a.keys()) & set(vector_b.keys())
    if not common_words:
        return 0
    dot_prod = 0
    for word in common_words:
        dot_prod += vector_a[word] * vector_b[word]
    norm_a = norm(vector_a)
    norm_b = norm(vector_b)
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_prod / (norm_a * norm_b)

# Fonction : claculer le document le plus pertinent
# Fonctionnement : calculer our chaque élément de la matrice TF-IDF la similitude et associer le document le plus pertinent
# Argument d'entrée : vecteur de la question, matrice TF-IDF, nom de fichier
# Sortie : fichier le plus important
def most_relevant_document(question_vector, tfidf_matrix, file_names):
    """
    :param question_vector:
    :param tfidf_matrix:
    :param file_names:
    :return:
    """
    similarities = {}
    for i, document_vector in enumerate(tfidf_matrix):
        similarity = cosine_similarity(question_vector, document_vector)
        similarities[file_names[i]] = similarity
    return max(similarities, key=similarities.get)

# Fonction : générer une réponse
# Fonctionnement : trouver une phrase dans le document pertinent qui contient le mot qui a le score TF-IDF le plus élevé
# Argument d'entrée : fuchier le plus pertinent, mot au plus haut score TF-IDF
# Sortie : phrase réponse
def generate_response(most_relevant_doc, highest_tfidf_word):
    """
    :param most_relevant_doc:
    :param highest_tfidf_word:
    :return: sentence
    """
    with open(f"speeches\\{most_relevant_doc}", 'r') as f:
        document_content = f.read()
        sentences = document_content.split('.')
        for sentence in sentences:
            if highest_tfidf_word in sentence:
                return sentence
    return None

# Fonction : affiner la réponse
# Fonctionnement : regarder le commencement de la question et commencer la réponse avec une formule cohérente
# Argument d'entrée : premier mot de la question, réponse
# Sortie : réponse affinée
def refine_response(question_starter, response):
    """
    :param response:
    :param question_starter:
    :return: response
    """
    if question_starter == "Comment":
        return f"Après analyse, {response[1].lower()}{response[2:]}."
    elif question_starter == "Pourquoi":
        return f"Car, {response[1].lower()}{response[2:]}."
    elif question_starter == "Peux-tu":
        return f"Oui, bien sûr!, {response[1].lower()}{response[2:]}."

# Fonction : faire une liste contenant le contenu des fichier textes
# Fonctionnement : parcourir les fichiers, les lire et stocker leur contenu dans une liste
# Argument d'entrée : nom du dossier contenant les fichiers
# Sortie : liste des contenus des textes
def read_documents(directory):
    """
    :param directory:
    :return: corpus
    """
    corpus = []
    for filename in os.listdir(directory):
        with open(f"cleaned\\{filename}", 'r') as f:
            document = f.read()
            corpus.append(document)
    return corpus
""" Programme python des fonctions du chatbot
Auteurs : Gabriel PRIEUR, Adrien RIVET
Version : 1.2
"""

"""----------IMPORTATTION DES MODULES ET FONCTIONS EXTERNES----------"""
import math
import os

"""----------DECLARATION DES FONCTIONS UTILISATEUR----------"""

def tokenize_question(question):
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

def intersection_terms(question_words, corpus_directory):
    question_set = set(question_words)
    corpus = read_documents(corpus_directory)
    corpus_words = [word for document in corpus for word in document.split()]
    corpus_set = set(corpus_words)
    common_terms = question_set.intersection(corpus_set)
    return list(common_terms)

def tfidf_vector(words, idf_scores):
    tf_vector = {}
    unique_question_words = set(words)
    for word in unique_question_words:
        tf = words.count(word) / len(words)
        tf_vector[word] = tf * idf_scores.get(word, 0)
    return tf_vector

def dot_product(vector_a, vector_b):
    return sum(vector_a[word] * vector_b[word] for word in vector_a)

def norm(vector):
    return math.sqrt(sum(value ** 2 for value in vector.values()))

def cosine_similarity(vector_a, vector_b):
    common_words = set(vector_a.keys()) & set(vector_b.keys())
    if not common_words:
        return 0
    dot_prod = sum(vector_a[word] * vector_b[word] for word in common_words)
    norm_a = norm(vector_a)
    norm_b = norm(vector_b)
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_prod / (norm_a * norm_b)

def most_relevant_document(question_vector, tfidf_matrix, file_names):
    similarities = {}
    for i, document_vector in enumerate(tfidf_matrix):
        similarity = cosine_similarity(question_vector, document_vector)
        similarities[file_names[i]] = similarity
    return max(similarities, key=similarities.get)

def generate_response(most_relevant_doc, highest_tfidf_word):
    with open(f"speeches\\{most_relevant_doc}", 'r') as f:
        document_content = f.read()
        sentences = document_content.split('.')
        for sentence in sentences:
            if highest_tfidf_word in sentence:
                return sentence
    return None

def refine_response(response, question_starter):
    if response:
        response = response.capitalize()
        response += "."
        if question_starter.lower() in ["comment", "pourquoi", "peux-tu"]:
            response = question_starter.get(question_starter.lower(), "") + " " + response
    return response

def read_documents(directory):
    corpus = []
    for filename in os.listdir(directory):
        with open(f"cleaned\\{filename}", 'r') as f:
            document = f.read()
            corpus.append(document)
    return corpus
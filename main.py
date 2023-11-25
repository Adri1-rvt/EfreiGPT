""" Programme python principal
Auteurs : Gabriel PRIEUR, Adrien RIVET
"""

"""----------IMPORTATTION DES MODULES ET FONCTIONS EXTERNES----------"""
import os
import time
from text_treatment import text_formating
from text_treatment import extract_president_name
from tfidf_matrice_calculation import tf_calculation
from tfidf_matrice_calculation import tfidf_matrix


"""----------CORPS DU PROGRAMME PRINCIPAL----------"""

# Prétraiter les textes
for file in os.listdir("speeches"):
    text_formating(file)

# ASCII art du logo du Chatbot
print("""
  ______  __          _    _____ _____ _______ 
 |  ____|/ _|        (_)  / ____|  __ \__   __|
 | |__  | |_ _ __ ___ _  | |  __| |__) | | |   
 |  __| |  _| '__/ _ \ | | | |_ |  ___/  | |   
 | |____| | | | |  __/ | | |__| | |      | |   
 |______|_| |_|  \___|_|  \_____|_|      |_| v1.1
""")
print("-----Bonjour et bienvenue sur EfreiGPT !-----")
time.sleep(0.5)

# Afficher le message d'introduction
message = ("Bienvenue sur EfreiGPT, le chatBot si bien programmé que son code ne vous Efrei pas ! \nQue désirez-vous faire ?")
for letter in message:
    print(letter, end="")
    time.sleep(0.1)
print()
time.sleep(1)
fonctionality_list = ["Afficher la liste des mots les moins importants dans le corpus de documents",
                      "Afficher le mot ayant le score TF-IDF le plus élevé",
                      "Indiquer le mot le plus répété par le président Chirac",
                      "Indiquer les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois",
                      "Indiquer le premier président à parler du climat et/ou de l’écologie",
                      "Hormis les mots dits « non importants », afficher les mots que tous les présidents ont évoqués"]
cpt = 1
for fonctionnality in fonctionality_list:
    print(f"{cpt}- {fonctionnality}")
    cpt += 1
    time.sleep(0.5)

print("---------------------------------------------")
number = int(input("Tapez le numéro choisi : "))
while number <= 0 or number > 6:
    number = int(input("Tapez le numéro choisi : "))

# Obtenir la matrice TF-IDF
tfidf_matrix_result = tfidf_matrix("cleaned")






#Fonctionnalité 1 : Afficher la liste des mots les moins importants dans le corpus de documents
if number == 1:
    print(f"Vous avez choisi : {fonctionality_list[0]}\n"+
          "Réponse :", end=" ")
    L = []
    for tfidf_scores in tfidf_matrix_result:
        for word in tfidf_scores:
            if tfidf_scores[word] == 0:
                L.append(word)
    answer = "Les mots les moins importants sur le corpus de documents sont : "
    for letter in answer:
        print(letter, end="")
        time.sleep(0.1)
    non_important_word = {}
    for element in L:
        if element in non_important_word.keys():
            non_important_word[element] += 1
        else:
            non_important_word[element] = 1
    for element in non_important_word:
        if non_important_word[element] == 8:
            answer = f'"{element}", '
            for letter in answer:
                print(letter, end="")
                time.sleep(0.1)


    print()


#Fonctionnalité 2 : Afficher le mot ayant le score TF-IDF le plus élevé
elif number == 2:
    print(f"Vous avez choisi : {fonctionality_list[1]}\n"+
          "Réponse :", end=" ")
    max_tfidf = 0
    max_word = ""
    for tfidf_scores in tfidf_matrix_result:
        for word in tfidf_scores:
            if tfidf_scores[word] > max_tfidf:
                max_tfidf = tfidf_scores[word]
                max_word = word
    answer = f'Le mot ayant le score TF-IDF le plus élevé est le mot "{max_word}", qui a un score TF-IDF égal à {max_tfidf}.'
    for letter in answer:
        print(letter, end="")
        time.sleep(0.1)


#Fonctionnalité 3 : Indiquer le mot le plus répété par le président Chirac
elif number == 3:
    print(f"Vous avez choisi : {fonctionality_list[2]}\n"+
          "Réponse :", end=" ")
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
    answer = f'''Le mot le plus répété par le président Chrirac est le mot "{most_repeated_word}", qu'il a prononcé exactement {most_repeated_frequency} fois.'''
    for letter in answer:
        print(letter, end="")
        time.sleep(0.1)


#Fonctionnalité 4 : Indiquer les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de fois
elif number == 4:
    print(f"Vous avez choisi : {fonctionality_list[3]}\n"+
          "Réponse :", end=" ")
    L = {}
    maximum = 0
    text_list = os.listdir("cleaned")
    for text_name in text_list:
        with open(f"cleaned\\{text_name}", "r") as f:
            tf = tf_calculation(f)
            if "nation" in tf.keys():
                president_name = extract_president_name(text_name)
                # Check if the president is already in the dictionary
                if president_name in L:
                    L[president_name] += tf["nation"]
                else:
                    L[president_name] = tf["nation"]
                # Update the maximum count
                if L[president_name] >= maximum:
                    maximum = L[president_name]
                    president = president_name
    answer = "Les présidents qui ont parlé de la « Nation » sont "
    for letter in answer:
        print(letter, end="")
        time.sleep(0.1)
    for president_name in L.keys():
        answer = f"{president_name}, "
        for letter in answer:
            print(letter, end="")
            time.sleep(0.1)
    answer = f"""\nC'est le président {president} qui a répété le plus de fois le mot "Nation" en le prononçant {maximum} fois."""
    for letter in answer:
        print(letter, end="")
        time.sleep(0.1)


#Fonctionnalité 5 : Indiquer le premier président à parler du climat et/ou de l’écologie
elif number == 5:
    print(f"Vous avez choisi : {fonctionality_list[4]}\n"+
          "Réponse :", end=" ")
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
    for letter in answer:
        print(letter, end="")
        time.sleep(0.1)


#Fonctionnalité 6 : Hormis les mots dits « non importants », afficher les mots que tous les présidents ont évoqués

elif number == 6:
    print(f"Vous avez choisi : {fonctionality_list[5]}\n"+
          "Réponse :", end=" ")
    common_words = {}
    text_list = os.listdir("cleaned")


    def concat_files(file1_path, file2_path, output_path, file):
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

    file3_path = 'cleaned\\cleaned_Nomination_Mitterrand1.txt1.txt'
    file4_path = 'cleaned\\cleaned_Nomination_Mitterrand2.txt.txt'
    output_path2 = 'cleaned_glob\\global_Mitterand.txt'
    file2 = 'global_Mitterand.txt'

    concat_files(file1_path, file2_path, output_path, file)
    concat_files(file1_path, file2_path, output_path, file2)

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
    for letter in answer:
        print(letter, end="")
        time.sleep(0.1)
    for word in common_words:
        if common_words[word] == 8 and word not in M:
            answer = f'"{word}", '
            for letter in answer:
                print(letter, end="")
                time.sleep(0.1)

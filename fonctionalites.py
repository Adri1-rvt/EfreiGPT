import os
import time
from text_treatment import text_formating
from text_treatment import extract_president_name
from tfidf_matrice_calculation import tf_calculation
from tfidf_matrice_calculation import tfidf_matrix



# Fonction : afficher la liste des mots les moins importants dans le corpus de documents
                # Fonctionnement : faire une liste avec les mots ayant un score TF-IDF = 0, puis les afficher s'ils sont = 0 dans tous les documents et qu'ils apparaissent donc 8 fois dans la liste
                def fonctionnality1():
                    print(f"Vous avez choisi : {fonctionality_list[0]}\n"+
                          "Réponse :", end=" ")
                    L = []
                    for tfidf_scores in tfidf_matrix_result:
                        for word in tfidf_scores:
                            if tfidf_scores[word] == 0:
                                L.append(word)
                    answer = "Les mots les moins importants sur le corpus de documents sont : "
                    cpt = 1
                    for letter in answer:
                        print(letter, end="")
                        cpt += 1
                        if cpt % 4 == 0:
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
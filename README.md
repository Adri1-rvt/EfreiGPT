<h1 align="center">
  <br>
  <a><img src="images\\logo.png" alt="Markdownify" width="200"></a>
  <br>
  EfreiGPT
  <br>
</h1>

<h4 align="center">Bienvenue sur EfreiGPT, le chatBot si bien programmé que son code ne vous Efrei pas !</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#utilisation">Utilisation</a> •
  <a href="#télécharger">Télécharger</a> •
  <a href="#crédits">Crédits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

## Description

EfreiGPT est une  application python conçue pour répondre à vos question sur des textes. Pour cela, il dispose d'un corpus de documents contenant les discours d'investiture des 6 derniers présidents de la République Française lors des 8 derniers mandats présidentiels.
<br>Les incroyables fonctionnalités d'EfreiGPT :
- Afficher la liste des mots les moins importants dans le corpus de documents
- Afficher le mot ayant le score TD-IDF le plus élevé 
- Indiquer le mot le plus répété par le président Chirac et le nombre de fois où il l'a prononcé
- Indiquer les noms des présidents qui ont parlé de la « Nation » et celui qui l’a répété le plus de
fois 
- Indiquer le premier président à parler du climat et/ou de l’écologie 
- Hormis les mots dits « non importants », quels sont les mots que tous les présidents ont évoqués.

Liste des composants du projet :
- Le fichier python principal : main.py -> à exécuter pour lancer le programme
- Le fichier python de prétraitement des textes : text_treatment.py
- Le fichier python de calcul de la matrice TF-IDF : tfidf_matrice_calculation.py
- Un fichier README.md -> le fichier sur lequel vous vous trouvez actuellement !
- Un fichier texte qui contient la license du projet -> LICENSE.txt 


## Utilisation

Pour utiliser EfreiGPT, rien de plus simple ! Il vous suffit de suivre quelques étapes faciles :
- Assurez-vous que Python est installé sur votre machine : Avant de pouvoir exécuter notre code Python, vous devez vous assurer que le langage de programmation Python est bien installé sur votre système. Pour vérifier cela, ouvrez votre terminal préféré (l'invite de commande Windows par défaut fait l'affaire) et tapez "python --version". Si Python n'est pas déjà installé, téléchargez-le depuis le site officiel (https://www.python.org/) et suivez les instructions d'installation.
- Téléchargez ou clonez le code source : Assurez-vous d'avoir une copie du code source de notre projet sur votre ordinateur. Vous pouvez le télécharger depuis GitHub, voir : <a href="#télécharger">Télécharger</a>.
- Exécutez le code : Après avoir téléchargé le dossier avec les éléments de notre projet, vous pouvez exécuter le code source du projet. Vous devrez chercher le fichier principal du projet, "main.py". Pour l'exécuter, vous avez plusieurs possibilités :
    - Utiliser un IDE (conseillé pour avoir le meilleur affichage) : ouvrir le répertoire du projet dans un IDE (comme PyCharm par exemple), cliquer sur le fichier "main.py" et l'exécuter. Le code sera exécuté directement dans la console de votre IDE préféré.
    - Utiliser un terminal : depuis un terminal, naviguer jusqu'au répertoire du projet à l'aide de la commande "cd", puis tapez "python main.py". Le code sera exécuté directement dans votre terminal.

Commandes utilisées :

```bash
# Vérifier si python est installé sur votre machine
$ python --version

# Se déplacer dans le repertoir du projet (exemple)
$ cd Desktop\\'Python Project'

# Lancer le code
$ python main.py
```

> **Note**
> Selon votre système d'exploitation ou le terminal utilisé, les commandes peuvent être différentes.


## Télécharger

Vous pouvez télécharger notre code source depuis notre page GitHub accessible via ce lien : [Télécharger](https://github.com/Adri1-rvt/pychatbot-prieur-rivet-f) 
<br>Pour cela, ouvrez le lien ci-dessus, puis cliquez sur le bonton vert en haut à droite de la page GitHub "Code". 
Sélectionnez ensuite "Download ZIP". 
<br>Une fois votre fichier zip téléchargé, il ne vous reste plus qu'à le décompresser (avec WinRaR par exemple) pour pouvoir utiliser le code source !


## Crédits

Ce projet a été réalisé par 2 programmeurs de grand talent :
- Gabriel PRIEUR
- Adrien RIVET

Nous sommes tous 2 étudiants en première année de prépa intégrée à Efrei Paris, grande école d'ingénieur du numérique.

## Contact
Si vous avez des questions ou besoin d'informations, n'hésitez pas à nous contacter via Teams ou par mail :<br>
Gabriel PIREUR (gabriel.prieur@efrei.net)<br>
Adrien RIVET (adrien.rivet@efrei.net)<br>
Nous échangerons avec vous avec grand plaisir !

## License

EfreiGPT - Tous droits réservés<br>
<a href="LICENSE.txt">License</a> 

```bash
___________ _____               .__    _____________________________
\_   _____// ____\______   ____ |__|  /  _____/\______   \__    ___/
 |    __)_\   __\\_  __ \_/ __ \|  | /   \  ___ |     ___/ |    |
 |        \|  |   |  | \/\  ___/|  | \    \_\  \|    |     |    |
/_______  /|__|   |__|    \___  |__|  \______  /|____|     |____|
        \/                    \/             \/
```
---

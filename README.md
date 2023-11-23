
<h1 align="center">
  <br>
  <a><img src="images\\logo.png" alt="Markdownify" width="200"></a>
  <br>
  EfreiGPT
  <br>
</h1>

<h4 align="center">Bienvenue sur EfreiGPT, le chatBot dont le code est si clair qu'il ne vous Efrei pas !</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#utilisation">Utilisation</a> •
  <a href="#télécharger">Télécharger</a> •
  <a href="#crédits">Crédits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

## Description

EfreiGPT est une incroyable application python conçue pour répondre à des questions à partir d'un corpus de 8 textes, qui contiennent les discours d'investiture des 6 derniers présidents de la république francaise.
<br>L'entièreté de notre programme est codé à la main est optimisé au maximum sans utiliser de fonctions prédéfinies.
<br>Les incroyables fonctionnalités d'EfreiGPT :
- Afficher la liste des mots les moins importants dans le corpus de documents. Un mot est dit non important,
si son TD-IDF = 0 dans tous les fichiers. 
- Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé 
- Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac 
- Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de
fois 
- Indiquer le premier président à parler du climat et/ou de l’écologie 
- Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués.

Liste des composants du projet :
- Des scipts python :
  - Le fichier python principal : main.py -> à exécuter pour lancer le programme
  - Le fichier python de prétraitement des textes
  - Le fichier python de calcul de la matrice TF-IDF
- Un fichier texte README -> le fichier sur lequel vous vous trouvez actuellement !
- Un fichier LICENSE.txt
- Un dossier contenant des images
- Deux dossiers contenants des fichiers textes


## Utilisation

Pour utiliser EfreiGPT, rien de plus simple ! Il vous suffit de suivre quelques étapes :
- Assurez-vous tout d'abord que Python est installé sur votre machine : Avant de pouvoir exécuter notre magnifique code Python, vous devez vous assurer que le langage de programmation Python est bien installé sur votre système. Pour vérifier cela, ouvrez votre terminal préféré (l'invite de commande Windows par défaut fait l'affaire) et tapez "python --version". Si Python n'est pas déjà installé, téléchargez-le depuis le site officiel (https://www.python.org/) et suivez les instructions d'installation.
- Téléchargez ou clonez le code source : Assurez-vous d'avoir une copie de la dernière version du code source de notre projet sur votre ordinateur. Vous pouvez le télécharger depuis GitHub : <a href="#télécharger">Télécharger</a>.
- Exécutez le code : Après avoir téléchargé le dossier avec les éléments de notre projet, vous pouvez exécuter le code source du projet. Vous devrez pour cela chercher le fichier principal du projet, "main.py". Pour l'exécuter, vous avez plusieurs possibilités :
    - Utiliser un IDE : ouvrez le répertoire du projet dans un IDE (comme PyCharm par exemple), puis cliquez sur le fichier "main.py" et exécutez-le. Le code sera exécuté directement dans la console de votre IDE préféré.
    - Utiliser un terminal : depuis un terminal, naviguez jusqu'au répertoire du projet à l'aide de la commande "cd", puis tapez "python main.py". Le code sera exécuté directement dans votre terminal.

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

Vous pouvez télécharger notre code source depuis notre page GitHub : [Télécharger](https://github.com/Adri1-rvt/pychatbot-prieur-rivet-f) 
<br>Pour cela, ouvrez le lien ci-dessus, puis cliquez sur le bonton vert en haut à droite de la page GitHub "Code". 
Sélectionnez ensuite "Download ZIP". <br>Une fois votre fichier zip téléchargé, il ne vous reste plus qu'à le décompresser (avec WinRaR par exemple) pour pouvoir utiliser le code source !


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
     |    __)_\   __\ _  __ \_/ __ \|  | /   \  ___ |     ___/ |    |
     |        \|  |   |  | \/\  ___/|  | \    \_\  \|    |     |    |
    /_______  /|__|   |__|    \___  |__|  \______  /|____|     |____|
            \/                    \/             \/
```

---

Fonctionnalité cachée : Notre chatBot a de l'humour ! Demandez-lui de vous faire une blague et il se fera un plaisir d'égayer votre journée !
<br>Pour cela, posez-lui une question avec le mot "blague" dedans.
# -*-coding:Utf-8 -*

############################################
# Changer le répertoire de travail courant #
############################################

import os
os.chdir("/var/www/html/openclassrooms-apprenez-a-programmer-en-python/autres/fichiers")

###########################
# Lecture dans un fichier #
###########################

# Ouverture du fichier
mon_fichier = open("fichier.txt", "r") # open(chemin, mode) : mode = "r" (read), "w" (write), "a" (append)

# Fermer le fichier
mon_fichier.close()

# Lire l'intégralité du fichier
mon_fichier = open("fichier.txt", "r")
contenu = mon_fichier.read()
print(contenu) # C'est le contenu du fichier. Spectaculaire non ?
mon_fichier.close()

############################
# Écriture dans un fichier #
############################

# Écrire une chaîne
mon_fichier = open("fichier.txt", "w") # Argh j'ai tout écrasé !
mon_fichier.write("Premier test d'écriture dans un fichier via Python") # renvoie le nombre de caractères écrites : 50
mon_fichier.close()

# Écrire d'autres types de données (il faut d'abord les convertir en chaine de caractères car write ne prend que les chaines)
mon_fichier = open("fichier.txt", "w") # Argh j'ai tout écrasé !
score = 400 # Un score pris au hasard (entier)
score = str(score) # on converti le score en chaine de caractères
mon_fichier.write(score) # renvoie le nombre de caractères écrites : 50
mon_fichier.close()

# Le mot-clé with : Cela signifie simplement que, si une exception se produit, le fichier sera tout de même fermé à la fin du bloc.
with open('fichier.txt', 'r') as mon_fichier:
    texte = mon_fichier.read()

############################################
# Enregistrer des objets dans des fichiers #
############################################

# Tout d'abord, il faut importer le module pickle
import pickle

# Enregistrer un objet dans un fichier
score = {
    "joueur 1":    5,
    "joueur 2":   35,
    "joueur 3":   20,
    "joueur 4":    2
}
with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)

# Récupérer nos objets enregistrés
with open('donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    print(score_recupere)


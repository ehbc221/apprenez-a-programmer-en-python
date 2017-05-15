# -*-coding:Utf-8 -*

#########################################
# Que sont les expressions régulières ? #
#########################################

# Rechercher au début ou à la fin de la chaîne
^cha # chaine commençant par cha
q$ # une chaine qui se termine par q

# Nombre d'occurences
abc* # 'ab', 'abc', 'abcc', 'abcccccc'
abc+ # 'abc', 'abcc', 'abccc'
abc? # 'ab', 'abc'
E{4} # signifie 4 fois la lettre E majuscule
E{2,4} # signifie de 2 à 4 fois la lettre E majuscule
E{,5} # signifie de 0 à 5 fois la lettre E majuscule
E{8,} # signifie 8 fois minimum la lettre E majuscule
[A-Z]{5} # 5 lettres majuscules qui se suivent dans une chaîne
(cha){2,5} # 'cha' répétée entre deux et cinq fois. Les séquences 'cha' doivent se suivre naturellement

# Caractères
[abcd] # l'une des lettres parmi a, b, c et d

# Classes de caractères
[A-Za-a0-9] # une lettre, majuscule ou minuscule, ou un chiffre

################
# Le module re #
################

import re

############################
# Chercher dans une chaîne #
############################

if re.match(expression, chaine) is not None:
    # Si l'expression est dans la chaîne
    # Ou alors, plus intuitivement
if re.match(expression, chaine):

#######################################################
# Valider une chaîne : exemple de numéro téléphonique #
#######################################################

# Regex : numéro téléphone Sénégal
^7[0678][ .-]?[0-9]{3}([ -/]?[0-9]{2}){2}

# Exemple : numérode téléphone comme suit :
0X XX XX XX XX
0X-XX-XX-XX-XX
0X.XX.XX.XX.XX
0XXXXXXXXX
# Le regex donne
^0[0-9]([ .-]?[0-9]{2}){4}$

# Pratique : numero de téléphone
import re
chaine = ""
expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
while re.search(expression, chaine) is None:
    chaine = input("Saisissez un numéro de téléphone (valide) :")

############################
# Remplacer une expression #
############################

re.sub(r"(ab)", r" \1 ", "abcdef")
' ab cdef'# On se contente ici de remplacer 'ab' par ' ab '

#################################
# Donner des noms à nos groupes #
#################################

texte = """
    nom='Task1', id=8
    nom='Task2', id=31
    nom='Task3', id=127"""
print(re.sub(r"id=(?P<id>[0-9]+)", r"id[\g<id>]", texte))
nom='Task1', id[8]
nom='Task2', id[31]
nom='Task3', id[127]
...

#############################
# Des expressions compilées #
#############################

chn_mdp = r"^[A-Za-z0-9]{6,}$"
exp_mdp = re.compile(chn_mdp)
mot_de_passe = ""
while exp_mdp.search(mot_de_passe) is None:
    mot_de_passe = input("Tapez votre mot de passe : ")

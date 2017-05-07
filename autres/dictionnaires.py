# -*-coding:Utf-8 -*

#########################
# Créer un dictionnaire #
#########################

mon_dictionnaire = dict() # Soit
mon_dictionnaire = {} # Ou bien
mon_dictionnaire["pseudo"] = "Prolixe" # {'pseudo': 'Prolixe'}
mon_dictionnaire["mot de passe"] = "*" # {'mot de passe': '*', 'pseudo': 'Prolixe'}
mon_dictionnaire["pseudo"] = "6pri1" # {'mot de passe': '*', 'pseudo': '6pri1'}

# Autre test (comme les listes)
test_dictionnaire = {}
test_dictionnaire[0] = "a"
test_dictionnaire[1] = "e"
test_dictionnaire[2] = "i"
test_dictionnaire[3] = "o"
test_dictionnaire[4] = "u"
test_dictionnaire[5] = "y" # test_dictionnaire : {0: 'a', 1: 'e', 2: 'i', 3: 'o', 4: 'u', 5: 'y'}

# Echiquier : clé - tuple
echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc" # À droite de la tour
echiquier['c', 1] = "fou blanc" # À droite du cavalier
echiquier['d', 1] = "reine blanche" # À droite du fou
# ... Première ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion
# ... Seconde ligne des blancs

# Dictionnaire déjà remplis
placard = {"chemise":3, "pantalon":6, "tee-shirt":7}

########################################
# Supprimer des clés d'un dictionnaire #
########################################

# Avec del
placard = {"chemise":3, "pantalon":6, "tee shirt":7}
del placard["chemise"]

# Avec pop : renvoie la valeur supprimée
placard = {"chemise":3, "pantalon":6, "tee shirt":7}
placard.pop("chemise") # 3

##############################
# Dictionnaires et fonctions #
##############################

def fete():
    print("C'est la fête.")
def oiseau():
    print("Fais comme l'oiseau...")
fonctions = {}
fonctions["fete"] = fete # on ne met pas les parenthèses
fonctions["oiseau"] = oiseau
fonctions["oiseau"] # <function oiseau at 0x00BA5198> : on ne peut appeler une fonction sans les parenthèses
fonctions["oiseau"]() # Fais comme l'oiseau...

############################
# Les méthodes de parcours #
############################

# Parcours des clés : 1ère méthode
fruits = {"pommes":21, "melons":3, "poires":31}
for cle in fruits:
    print(cle) # melons poires pommes

# Parcours des clés : 2ème méthode : keys()
fruits = {"pommes":21, "melons":3, "poires":31}
for cle in fruits.keys():
    print(cle) # melons poires pommes

# Parcours des valeurs : values()
fruits = {"pommes":21, "melons":3, "poires":31}
for valeur in fruits.values():
    print(valeur) # 3 31 21

# Parcours des valeurs : values() : avec condition if
fruits = {"pommes":21, "melons":3, "poires":31}
if 21 in fruits.values():
    print("Un des fruits se trouve dans la quantité 21.") # Un des fruits se trouve dans la quantité 21.

# Parcours des clés et valeurs simultanément
fruits = {"pommes":21, "melons":3, "poires":31}
for cle, valeur in fruits.items():
    print("La clé {} contient la valeur {}.".format(cle, valeur))

###############################################
# Les dictionnaires et paramètres de fonction #
###############################################

# Récupérer les paramètres nommés dans un dictionnaire>>> def fonction_inconnue(**parametres_nommes):
def fonction_inconnue(**parametres_nommes):
    """Fonction permettant de voir comment récupérer les paramètres nommés
    dans un dictionnaire"""
    print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))
fonction_inconnue() # J'ai reçu en paramètres nommés : {}
fonction_inconnue(p=4, j=8) # J'ai reçu en paramètres nommés : {'p': 4, 'j': 8}

# Accepter n'importe quel type de paramètres, nommés ou non, dans n'importe quel ordre, dans n'importe quelle quantité
def fonction_inconnue(*en_liste, **en_dictionnaire): #  les paramètres non nommés se retrouveront dans la variable en_liste et les paramètres nommés dans la variable en_dictionnaire

# Transformer un dictionnaire en paramètres nommés d'une fonction
parametres = {"sep":" >> ", "end":" -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres) # Voici >> un >> exemple >> d'appel -

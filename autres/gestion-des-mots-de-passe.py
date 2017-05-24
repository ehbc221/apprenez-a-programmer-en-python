# -*-coding:Utf-8 -*

########################################################
# Réceptionner un mot de passe saisi par l'utilisateur #
########################################################

from getpass import getpass
mot_de_passe = getpass("Tapez votre mot de passe : ")

############################
# Chiffrer un mot de passe #
############################

# Chiffrer un mot de passe
import hashlib

# Choisir un algorithme : algorithms_available ou hashlib.algorithms_guaranteed. Exemple : hashlib.algorithms_guaranteed
import hashlib
hashlib.algorithms_guaranteed
{'sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5'}

# Utilisation d'un algorithme : SHA1 (chaîne-de-bytes) => utiliser b minuscule avant l'ouverture de votre chaîne
mot_de_passe = hashlib.sha1(b"mot de passe")
# Obtenir le chiffrement associé à cet objet : digest (renvoie un type bytes contenant notre mot de passe chiffré) et hexdigest (renvoie une chaîne str contenant une suite de symboles hexadécimaux => de 0 à 9 et de A à F)
mot_de_passe.hexdigest()
'b47ea832576a75814e13351dcc97eaa985b9c6b7'

########################################
# Test de vérification de mot de passe #
########################################

import hashlib
from getpass import getpass

chaine_mot_de_passe = b"azerty"
mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()

verrouille = True
while verrouille:
    entre = getpass("Tapez le mot de passe : ") # azerty
    # On encode la saisie pour avoir un type bytes
    entre = entre.encode()
    
    entre_chiffre = hashlib.sha1(entre).hexdigest()
    if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
    else:
        print("Mot de passe incorrect")

print("Mot de passe accepté...")

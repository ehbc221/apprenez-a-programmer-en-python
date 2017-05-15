# -*-coding:Utf-8 -*

##########
# Autres #
##########

"a" * 3 # "aaa"
# en plaçant un r avant le délimiteur qui ouvre notre chaîne, tous les caractères anti-slash qu'elle contient sont échappés
r'\n' # '\\n'

###############################################
# Les chaines de caractère: la méthode format #
###############################################

# Première syntaxe de la méthode format
prenom = "El Hadj Babacar"
nom = "Cissé"
print("Je m'appelle {0} {1}".format(prenom, nom))
# OU BIEN
date = "Dimanche 24 juillet 2011"
heure = "17:00"
print("Cela s'est produit le {}, à {}.".format(date, heure))
# Seconde syntaxe
# formatage d'une adresse
adresse = """
{no_rue}, {nom_rue}
 {code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)

###############################
# La concaténation de chaînes #
###############################

prenom = "El Hadj Babacar"
nom = "Cissé"
nom_entier = prenom + " " + nom
age = 21
# str + int => convertion
chaine = "Je m'appelle " + prenom + " " + nom + " et j'ai " + str(age) + " ans."
       break

##################################
# Les méthodes de la classe str #
#################################

chaine = str() # Crée une chaîne vide
# On aurait obtenu le même résultat en tapant chaine = ""
while chaine.lower() != "q":
    print("Tapez 'Q' pour quitter...")
    chaine = input()

print("Merci !")

########################
# Sélection de chaînes #
########################

presentation = "salut"
presentation[0:2] # On sélectionne les deux premières lettres (sa)
presentation[2:len(presentation)] # On sélectionne la chaîne sauf les deux premières lettres (lut)
presentation[:2] # Du début jusqu'à la troisième lettre non comprise (sa)
presentation[2:] # De la troisième lettre (comprise) à la fin (lut)
# Pour le remplacement d'une lettre(ex: s par S), on doit procéder ainsi
presentation = "S" + presentation[1:]

#######################################
# Accéder aux caractères d'une chaîne #
#######################################

chaine = "Hello"
chaine[0] # première lettre (H)
chaine[-1] # dernière lettre (o)
chaine[-2] # avant dernière lettre (l)

# -*-coding:Utf-8 -*


############################
# Permutter deux variables #
############################

a = 5
b = 3
a,b = b,a

######################
# La fonction type() #
######################

print (type(a))

#######################
# La fonction print() #
#######################

print("a =", a, "et b =", b)

#####################################
# Forme complète (if, elif et else) #
#####################################

nombre = 21
if nombre > 0:
    print("a est positif")
elif nombre < 0:
    print("a est négatif")
else: # if a == 0
    print("a est nul")

###########################################################################
# Mettre en pause notre programme(ou bien os.system("pause") sur Windows) #
###########################################################################

input("Appuyez sur ENTREE pour continuer...")

################################
# Les mots-clés and, or et not #
################################

if a >= 2 and a <= 8:
    print("a est dans l'intervalle {2, 8}.")
else:
    print("a n'est pas dans l'intervalle.")
majeur = False
if majeur is not True:
    print("Majeur =", majeur, ", vous n'êtes pas encore majeur")

###################
# La boucle while #
###################

nb = 7
i = 0
while i < 10:
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1

#################
# La boucle for #
#################

chaine = "Bonjour les ZER0S"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print(lettre)
    else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
        print("*")

#######################
# Le mot-clé continue #
#######################

i = 1
while i < 20: # Tant que i est inférieure à 20
    if i % 3 == 0:
        i += 4 # On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue # On retourne au while sans exécuter les autres lignes
    print("La variable i =", i)
    i += 1 # Dans le cas classique on ajoute juste 1 à i

###########################################################################################
# Les fonctions: docstring (chaîne d'aide), on peut voir ce message en tapant help(table) #
###########################################################################################

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb
    
    (max >= 0)"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
# Appel de la fonction
table(8, 11)

######################################################
# Appeler les paramètres d'une fonction par leur nom #
######################################################

def fonc(a=1, b=2, c=3, d=4, e=5):
    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)
# Appel de la fonction
fonc(d=8, b=5, e=1)

########################
# L'instruction return #
########################

def carre(valeur):
    return valeur * valeur
# Appel de la fonction
valeur = carre(5)
print("Le carré de 5 est", valeur)

########################
# Les fonctions lambda #
########################

x = 5
y = 12
somme = lambda x, y: x + y
print("La somme de", x, "et", y, "donne", somme(x, y))

#####################
# La méthode import #
#####################

import math
racine = math.sqrt(16)
print("La racine carré de 16 est", racine)

#########################################
# Utiliser un espace de noms spécifique #
#########################################

import math as mathematiques
mathematiques.sqrt(25)

#####################################################
# Une autre méthode d'importation : from … import … #
#####################################################

from math import fabs
fabs(-5)
fabs(2)

###############################################
# Les exceptions : forme minimale du bloc try #
###############################################

annee = input("Donnez un nombre pour tester la convertion: ")
try:
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année.")

####################################################
# Les exceptions : forme plus complète du bloc try #
####################################################

try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else: # exécuter une action si aucune erreur ne survient dans le bloc
    print("Le résultat obtenu est", resultat)
finally: # Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non
    print("Fin du bloc try")

##################################
# Les exceptions : le mot-clé as #
##################################

try:
    5 / 0
except ZeroDivisionError as exception_retournee:
    print("Voici l'erreur :", exception_retournee)

####################################
# Les exceptions : le mot-clé pass #
####################################

try:
    5 / 0
except ZeroDivisionError:
    pass

##################
# Les assertions #
##################

nombre = input("Saisissez un nombre supérieur à 0 :")
try:
    nombre = int(nombre) # Conversion du nombre
    assert nombre > 0 # On test l'assertion suivante: le nombre est strictement positif
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError: # Si l'assertion est fausse, on lève une erreur d'assertion
    print("Le nombre saisi est inférieur ou égal à 0.")

###############################
# Lever une exception : raise #
###############################

annee = input("Saisissezune année :") # L'utilisateur saisit l'année
try:
    annee = int(annee) # On tente de convertir l'année
    if annee <= 0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")

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

#########################
# Taille d'une séquence #
#########################

len(sequence) # sequence peut etre une chaine de caractères, un tableau, ...

#################################
# Méthode de parcours par while #
#################################

chaine = "Salut"
i = 0 # On appelle l'indice 'i' par convention
while i < len(chaine):
    print(chaine[i]) # On affiche le caractère à chaque tour de boucle
    i += 1

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

##############
# Les listes #
##############

ma_liste = list() # initialisation 1
ma_liste = [] # initialisation 2
ma_liste = ['c', 'f', 'm']
ma_liste[0] # On accède au premier élément de la liste (c)
ma_liste[2] # Troisième élément (m)
ma_liste[1] = 'Z' # On remplace 'f' par 'Z'
ma_liste # ['c', 'Z', 'm']
# Ajouter un élément à la fin de la liste
ma_liste.append("O") # ['c', 'Z', 'm', O]
# Insérer un élément dans la liste
ma_liste.insert(2, "a") # insérer "a" à la 2ème position : ['c', 'Z', 'a', 'm', 'O']
# Concatener 2 listes
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
ma_liste1.extend(ma_liste2) # 1ère méthode : on insère ma_liste2 à la fin de ma_liste1 : [3, 4, 5, 8, 9, 10]
ma_liste1 = [3, 4, 5]
ma_liste1 + ma_liste2 # 2ème méthode (juste pour l'affichage car ne modifie pas la liste, renvoie juste les 2 listes): [3, 4, 5, 8, 9, 10]
ma_liste1 += ma_liste2 # 3ème méthode : dentique à extend : [3, 4, 5, 8, 9, 10]
# Suppression d'éléments d'une liste
ma_liste = ['c', 'Z', 'a', 'm', 'O']
del ma_liste[0] # Avec del : l'indice de l'élément à supprimer ('c')
ma_liste.remove('m') # Avec remove : l'élément lui meme

##########################
# Le parcours des listes #
##########################

# 1ère méthode
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

i = 0 # Notre indice pour la boucle while
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1 # On incrémente i, ne pas oublier !
# 2ème méthode : cette méthode est cependant préférable
for elt in ma_liste: # elt va prendre les valeurs successives des éléments de ma_liste
    print(elt)
# La fonction enumerate
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, elt in enumerate(ma_liste): # i l'indice, elt l'élément en cours
    print("À l'indice {} se trouve {}.".format(i, elt))

##################################
# Un petit coup d'œil aux tuples #
##################################

tuple_vide = ()
tuple_non_vide = (1,) # est équivalent à ci dessous
tuple_non_vide = 1,
tuple_avec_plusieurs_valeurs = (1, 2, 5)
# Affectation multiple
a, b = 3, 4
# Une fonction renvoyant plusieurs valeurs
def decomposer(entier, divise_par):
    """Cette fonction retourne la partie entière et le reste de
    entier / divise_par"""

    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste
partie_entiere, reste = decomposer(20, 3) # partie_entiere = 6 et reste = 2

###########################
# Entre chaînes et listes #
###########################

# Des chaînes aux listes : split("séparateur")
ma_chaine = "Bonjour à tous"
ma_chaine.split(" ") # ['Bonjour', 'à', 'tous']
# Des listes aux chaînes : "séparateur".join(liste_à_fusionner)
ma_liste = ['Bonjour', 'à', 'tous']
" ".join(ma_liste) # 'Bonjour à tous'
# Exemple :
def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.
    De plus, on va remplacer le point décimal par la virgule"""
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])

###########################################################################
# Les fonctions dont on ne connaît pas à l'avance le nombre de paramètres #
###########################################################################

def fonction_inconnue(*parametres):
    """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""
    print("J'ai reçu : {}.".format(parametres))
fonction_inconnue() # J'ai reçu : ().
fonction_inconnue(33) # J'ai reçu : (33,).
fonction_inconnue('a', 'e', 'f') # J'ai reçu : ('a', 'e', 'f').
var = 3.5
fonction_inconnue(var, [4], "...") # J'ai reçu : (3.5, [4], '...').

########################################
# Exemple : fonction identique à print #
########################################

def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction chargée de reproduire le comportement de print.
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés. 
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :
    print(chaine, end='')"""
    # Les paramètres sont sous la forme d'un tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilités, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en chaîne
    # Sinon on va avoir quelques problèmes lors du join
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # La liste des paramètres ne contient plus que des chaînes de caractères
    # À présent on va constituer la chaîne finale
    chaine = sep.join(parametres)
    # On ajoute le paramètre fin à la fin de la chaîne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')

###################################################
# Transformer une liste en paramètres de fonction #
###################################################

liste_des_parametres = [1, 4, 9, 16, 25, 36]
print(*liste_des_parametres) # 1 4 9 16 25 36

###############################
# Les compréhensions de liste #
###############################

# Parcours simple
liste_origine = [0, 1, 2, 3, 4, 5]
[nb * nb for nb in liste_origine] # [0, 1, 4, 9, 16, 25], nb * nb revient à écrire nb ** 2
# Filtrage avec un branchement conditionnel
liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[nb for nb in liste_origine if nb % 2 == 0] # [2, 4, 6, 8, 10]
# Filtrer et modifier une liste (partie 1)
qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21] # Par exemple 15 pommes, 3 melons...
[nb_fruits - qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits > qtt_a_retirer] # [8, 11, 14]
# Filtrer et modifier une liste (partie 2)
inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]
# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
# On trie l'inventaire inversé dans l'ordre décroissant
inventaire_inverse.sort(reverse=True)
# Et on reconstitue l'inventaire
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in inventaire_inverse]

####################
# Le mot-clé break #
###################

while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
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

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

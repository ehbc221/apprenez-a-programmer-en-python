# -*-coding:Utf-8 -*


# Permutter deux variables
a = 5
b = 3
a,b = b,a


# La fonction type()
print (type(a))


# La fonction print()
print("a =", a, "et b =", b)


# Forme complète (if, elif et else)
nombre = 21
if nombre > 0:
    print("a est positif")
elif nombre < 0:
    print("a est négatif")
else: # if a == 0
    print("a est nul")


# Mettre en pause notre programme(ou bien os.system("pause") sur Windows)
input("Appuyez sur ENTREE pour continuer...")


# Les mots-clés and, or et not
if a >= 2 and a <= 8:
    print("a est dans l'intervalle {2, 8}.")
else:
    print("a n'est pas dans l'intervalle.")
majeur = False
if majeur is not True:
    print("Majeur =", majeur, ", vous n'êtes pas encore majeur")


# La boucle while
nb = 7
i = 0
while i < 10:
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1


# La boucle for
chaine = "Bonjour les ZER0S"
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print(lettre)
    else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
        print("*")


# Le mot-clé continue
i = 1
while i < 20: # Tant que i est inférieure à 20
    if i % 3 == 0:
        i += 4 # On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
        continue # On retourne au while sans exécuter les autres lignes
    print("La variable i =", i)
    i += 1 # Dans le cas classique on ajoute juste 1 à i


# Les fonctions: docstring (chaîne d'aide), on peut voir ce message en tapant help(table)
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


# Appeler les paramètres d'une fonction par leur nom
def fonc(a=1, b=2, c=3, d=4, e=5):
    print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)
# Appel de la fonction
fonc(d=8, b=5, e=1)


# L'instruction return
def carre(valeur):
    return valeur * valeur
# Appel de la fonction
valeur = carre(5)
print("Le carré de 5 est", valeur)


# Les fonctions lambda
x = 5
y = 12
somme = lambda x, y: x + y
print("La somme de", x, "et", y, "donne", somme(x, y))


# La méthode import
import math
racine = math.sqrt(16)
print("La racine carré de 16 est", racine)


# Utiliser un espace de noms spécifique
import math as mathematiques
mathematiques.sqrt(25)


# Une autre méthode d'importation : from … import …
from math import fabs
fabs(-5)
fabs(2)





# Le mot-clé break
while 1: # 1 est toujours vrai -> boucle infinie
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break

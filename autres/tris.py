# -*-coding:Utf-8 -*

#################
# Deux méthodes #
#################

# Méthode de liste : sort (Elle travaille sur la liste-même et change donc son ordre, si c'est nécessaire.)
prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
prenoms.sort()
prenoms # ['Albert', 'André', 'Jacques', 'Laure', 'Sophie', 'Victoire']

# Fonction sorted (Elle ne modifie pas l'objet d'origine, mais en retourne un nouveau.)
prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
sorted(prenoms) # ['Albert', 'André', 'Jacques', 'Laure', 'Sophie', 'Victoire']
prenoms # ['Jacques', 'Laure', 'André', 'Victoire', 'Albert', 'Sophie']

##############################
# Aperçu des critères de tri #
##############################

sorted([1, 8, -2, 15, 9]) # [-2, 1, 8, 9, 15]
sorted(["1", "8", "-2", "15", "9"]) # ['-2', '1', '15', '8', '9']

################################
# Trier avec des clés précises #
################################

etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]
sorted(etudiants) # Trie par rapport à la 1ère colonne
[
    ('Charles', 12, 15),
    ('Clément', 14, 16),
    ('Damien', 12, 15),
    ('Oriane', 14, 18),
    ('Thomas', 11, 12)
]
# L'argument key : Trie par rapport à une clé (colonne) bien précise
sorted(etudiants, key=lambda colonnes: colonnes[2])
[
    ('Thomas', 11, 12), 
    ('Charles', 12, 15), 
    ('Damien', 12, 15), 
    ('Clément', 14, 16),
    ('Oriane', 14, 18)
]

############################
# Trier une liste d'objets #
############################

# Notre classe Etudiant
class Etudiant:
    
    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(self.prenom, self.age, self.moyenne)

# Notre liste d'étudiants
etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

# Affichons notre liste d'étudiants
etudiants
[
    <Étudiant Clément (âge=14, moyenne=16)>,
    <Étudiant Charles (âge=12, moyenne=15)>,
    <Étudiant Oriane (âge=14, moyenne=18)>,
    <Étudiant Thomas (âge=11, moyenne=12)>,
    <Étudiant Damien (âge=12, moyenne=15)>
]

# Nous ne pouvons pas trier notre liste d'étudiants directement
sorted(etudiants)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: Etudiant() < Etudiant()

# On a 2 façons de trier notre objet Etudiant : définir la méthode spéciale __lt__ ou utiliser l'argument key

# Avec key:
sorted(etudiants, key=lambda etudiant: etudiant.moyenne)
[
    <Étudiant Thomas (âge=11, moyenne=12)>,
    <Étudiant Charles (âge=12, moyenne=15)>,
    <Étudiant Damien (âge=12, moyenne=15)>,
    <Étudiant Clément (âge=14, moyenne=16)>,
    <Étudiant Oriane (âge=14, moyenne=18)>
]

# Trier dans l'ordre inverse
sorted(etudiants, key=lambda etudiant: etudiant.age, reverse=True)
[
    <Étudiant Clément (âge=14, moyenne=16)>,
    <Étudiant Oriane (âge=14, moyenne=18)>,
    <Étudiant Charles (âge=12, moyenne=15)>,
    <Étudiant Damien (âge=12, moyenne=15)>,
    <Étudiant Thomas (âge=11, moyenne=12)>
]

###################################################################
# Plus rapide et plus efficace : Les fonctions du module operator #
###################################################################

#############################
# Trier une liste de tuples #
#############################

etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]
# Il faut d'abord importer la fonction itemgetter du module operator, puis l'utiliser pour trier notre liste d'étudiants (par moyenne)
from operator import itemgetter
sorted(etudiants, key=itemgetter(2))
[
    ('Thomas', 11, 12), 
    ('Charles', 12, 15), 
    ('Damien', 12, 15), 
    ('Clément', 14, 16),
    ('Oriane', 14, 18)
]

############################
# Trier une liste d'objets #
############################
class Etudiant:
    
    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(self.prenom, self.age, self.moyenne)

# Notre liste d'étudiants
etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

# Il faut d'abord importer la fonction itemgetter du module operator, puis l'utiliser pour trier notre liste d'étudiants (par moyenne)
from operator import attrgetter
sorted(etudiants, key=attrgetter("moyenne"))

##################################
# Trier selon plusieurs critères #
##################################

# On a juste a préciser ces différents, séparés par des virgules, à l'appel de la fonction attrgetter
sorted(etudiants, key=attrgetter("age", "moyenne"))
[
    <Étudiant Thomas (âge=11, moyenne=12)>,
    <Étudiant Charles (âge=12, moyenne=15)>,
    <Étudiant Damien (âge=12, moyenne=15)>,
    <Étudiant Clément (âge=14, moyenne=16)>,
    <Étudiant Oriane (âge=14, moyenne=18)>
]

####################
# Chaînage de tris #
####################

class LigneInventaire:
    
    """Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.

    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return "<Ligne d'inventaire {} ({}X{})>".format(self.produit, self.prix, self.quantite)

# Création de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("banane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24)
]

# Trier cette liste par prix et par quantité
from operator import attrgetter
sorted(inventaire, key=attrgetter("prix", "quantite"))
[
    <Ligne d'inventaire banane (0.9X21)>,
    <Ligne d'inventaire pomme rouge (1.2X19)>,
    <Ligne d'inventaire poire (1.2X24)>,
    <Ligne d'inventaire orange (1.4X24)>
]

# Trier par prix croissant et par quantité décroissante : on fait deux tris en utilisant la propriété de stabilité.
# La subtilité, c'est que l'on va trier d'abord par notre second critère et ensuite par notre premier
inventaire.sort(key=attrgetter("quantite"), reverse=True) # On aurait aussi pu utiliser la méthode sorted
sorted(inventaire, key=attrgetter("prix"))
[
    <Ligne d'inventaire banane (0.9X21)>,
    <Ligne d'inventaire poire (1.2X24)>,
    <Ligne d'inventaire pomme rouge (1.2X19)>,
    <Ligne d'inventaire orange (1.4X24)>
]

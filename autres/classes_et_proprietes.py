# -*-coding:Utf-8 -*

##########################
# Nos premiers attributs #
##########################

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    class Personne:
        """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self.lieu_residence = "Paris"

# Test
bernard = Personne("Micado", "Bernard")
bernard.nom # 'Micado'
bernard.prenom # 'Bernard'
bernard.age # 33
# Bernard déménage…
bernard.lieu_residence = "Berlin"
bernard.lieu_residence # 'Berlin'

#######################
# Attributs de classe #
#######################

class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    
    objets_crees = 0 # Le compteur vaut 0 au départ
    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1

# Test
Compteur.objets_crees # 0
a = Compteur() # On crée un premier objet
Compteur.objets_crees # 1
b = Compteur()
Compteur.objets_crees # 2

############################
# Les méthodes, la recette #
############################

class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    
    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""
    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire
    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        la surface du tableau"""

        
        print(self.surface)
    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""

# Test
tab = TableauNoir()
tab.lire()
tab.ecrire("Salut tout le monde.")
tab.ecrire("La forme ?")
tab.lire()
# Salut tout le monde.
# La forme ?
tab.effacer()
tab.lire() #

######################
# Méthodes de classe #
######################

class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    
    objets_crees = 0 # Le compteur vaut 0 au départ
    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1
    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créés"""
        print("Jusqu'à présent, {} objets ont été créés.".format(
                cls.objets_crees))
    combien = classmethod(combien)

# Tests
Compteur.combien() # Jusqu'à présent, 0 objets ont été créés.
a = Compteur()
Compteur.combien() # Jusqu'à présent, 1 objets ont été créés.
b = Compteur()
Compteur.combien() # Jusqu'à présent, 2 objets ont été créés.

######################
# Méthodes statiques #
######################

class Test:
    """Une classe de test tout simplement"""
    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe.")
    afficher = staticmethod(afficher)

###################
# La fonction dir #
###################

class Test:
    """Une classe de test tout simplement"""
    def __init__(self):
        """On définit dans le constructeur un unique attribut"""
        self.mon_attribut = "ok"
    
    def afficher_attribut(self):
        """Méthode affichant l'attribut 'mon_attribut'"""
        print("Mon attribut est {0}.".format(self.mon_attribut))

# Créons un objet de la classe Test
un_test = Test()
un_test.afficher_attribut() # Mon attribut est ok.
dir(un_test)
# ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', 'afficher_attribut', 'mon_attribut']

# L'attribut spécial __dict__
un_test = Test()
un_test.__dict__ # {'mon_attribut': 'ok'}

# Modifier la valeur de l'attribut
un_test.__dict__["mon_attribut"] = "plus ok"
un_test.afficher_attribut() # Mon attribut est plus ok.

##################
# Les propriétés #
##################

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""

    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris" # Notez le souligné _ devant le nom
    def _get_lieu_residence(self):
    """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'lieu_residence'"""
        
        
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence
    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format(self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

# Tests
jean = Personne("Micado", "Jean")
jean.nom # 'Micado'
jean.prenom # 'Jean'
jean.age # 33
jean.lieu_residence # On accède à l'attribut lieu_residence ! 'Paris'
jean.lieu_residence = "Berlin" # Attention, il semble que Jean déménage à Berlin.
jean.lieu_residence # On accède à l'attribut lieu_residence ! 'Berlin'

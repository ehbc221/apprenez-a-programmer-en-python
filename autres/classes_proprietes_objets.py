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

######################
# Édition de l'objet #
######################

class Exemple:
    """Un petit exemple de classe"""
    def __init__(self, nom):
        """Exemple de constructeur"""
        self.nom = nom
        self.autre_attribut = "une valeur"
# Tests
mon_objet = Exemple("un premier exemple")

# Destruction de l'objet #
def __del__(self):
        """Méthode appelée quand l'objet est supprimé"""
        print("C'est la fin ! On me supprime !")

#######################################################
# Représentation de l'objet : 1ère méthode : __repr__ #
#######################################################

class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({}), prénom({}), âge({})".format(self.nom, self.prenom, self.age)
# Tests
p1 = Personne("Micado", "Jean")
# 1ère méthode
p1 # Personne: nom(Micado), prénom(Jean), âge(33)
# 2ème méthode
repr(p1) # Personne: nom(Micado), prénom(Jean), âge(33)

######################################################
# Représentation de l'objet : 2ème méthode : __str__ #
######################################################

class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "{} {}, âgé de {} ans".format(self.prenom, self.nom, self.age)
# Test
p1 = Personne("Micado", "Jean")
print(p1) # Jean Micado, âgé de 33 ans
chaine = str(p1)
chaine # 'Jean Micado, âgé de 33 ans'

######################################
# Accès aux attributs de notre objet #
######################################

# Méthode 1 : __getattr__
 class Protege:
    """Classe possédant une méthode particulière d'accès à ses attributs :
    Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""

    def __init__(self):
        """On crée quelques attributs par défaut"""
        self.a = 1
        self.b = 2
        self.c = 3
    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte"""

        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))
# Tests
pro = Protege()
pro.a # 1
pro.c # 3
pro.e # Alerte ! Il n'y a pas d'attribut e ici !

# Méthode 2 : __setattr__
def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""

        object.__setattr__(self, nom_attr, val_attr)
        self.enregistrer()

# Méthode 3 : __delattr__
def __delattr__(self, nom_attr):
        """On ne peut supprimer d'attribut, on lève l'exception
        AttributeError"""
        
        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")
# Oubien passer par :
object.__delattr__(self, 'nom')

##################
# Un petit bonus #
##################

# Voici quelques fonctions qui font à peu près ce que nous avons fait mais en utilisant des chaînes de caractères pour les noms d'attributs.
objet = MaClasse() # On crée une instance de notre classe
getattr(objet, "nom") # Semblable à objet.nom
setattr(objet, "nom", val) # = objet.nom = val ou objet.__setattr__("nom", val)
delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
hasattr(objet, "nom") # Renvoie True si l'attribut "nom" existe, False sinon

#############################
# Les méthodes de conteneur #
#############################

# Accès aux éléments d'un conteneur #

class ZDict:
    """Classe enveloppe d'un dictionnaire"""
    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}
    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        
        return self._dictionnaire[index]
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        
        self._dictionnaire[index] = valeur
    def __delitem__(self, index):
        """Cette méthode est appelée quand on fait del objet[index], ou objet[index].__delitem__
        On appelle la méthode __delattr__ de la classe object de Python"""
        object.__delattr__(self, self._dictionnaire[index])
    def __repr__(self, index):
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "Voici l'attribut {} du dictionnaire.".format(self._dictionnaire[index])
    def __repr__(self, index):
        """Méthode permettant d'afficher plus joliment notre objet() cette fois ci avec la méthode str)"""
        return "Voici l'attribut {} du dictionnaire.".format(self._dictionnaire[index])

##############################
# Les méthodes mathématiques #
##############################

class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes
    et de secondes"""
    
    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min # Nombre de minutes
        self.sec = sec # Nombre de secondes
    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec)
    def __add__(self, objet_a_ajouter):
            """L'objet à ajouter est un entier, le nombre de secondes"""
            nouvelle_duree = Duree()
            # On va copier self dans l'objet créé pour avoir la même durée
            nouvelle_duree.min = self.min
            nouvelle_duree.sec = self.sec
            # On ajoute la durée
            nouvelle_duree.sec += objet_a_ajouter
            # Si le nombre de secondes >= 60
            if nouvelle_duree.sec >= 60:
                nouvelle_duree.min += nouvelle_duree.sec // 60
                nouvelle_duree.sec = nouvelle_duree.sec % 60
            # On renvoie la nouvelle durée
            return nouvelle_duree
    def __radd__(self, objet_a_ajouter):
        """Cette méthode est appelée si on écrit 4 + objet et que
        le premier objet (4 dans cet exemple) ne sait pas comment ajouter
        le second. On se contente de rediriger sur __add__ puisque,
        ici, cela revient au même : l'opération doit avoir le même résultat,
        posée dans un sens ou dans l'autre"""
        
        return self + objet_a_ajouter
    def __iadd__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        # On travaille directement sur self cette fois
        # On ajoute la durée
        self.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        # On renvoie self
        return self
# Tests
d1 = Duree(12, 8)
print(d1) # 12:08
# Pour ajout : méthode 1
d2 = d1 + 54 # d1 + 54 secondes
# Méthode 2
d2 = d1.__add__(54)
print(d2) # 13:02
d1 = Duree(8, 5)
d1 += 128
print(d1) # 10:13

###############################
# Les méthodes de comparaison #
###############################

# def __methode__(self, objet_a_comparer): (methode = eq/ne/gt/ge/lt/le) => voir Les méthodes de comparaison.png
# Exemples : durée
def __eq__(self, autre_duree):
        """Test si self et autre_duree sont égales"""
        return self.sec == autre_duree.sec and self.min == autre_duree.min
def __gt__(self, autre_duree):
        """Test si self > autre_duree"""
        # On calcule le nombre de secondes de self et autre_duree
        nb_sec1 = self.sec + self.min * 60
        nb_sec2 = autre_duree.sec + autre_duree.min * 60
        return nb_sec1 > nb_sec2

####################################
# La méthode spéciale __getstate__ #
####################################

class Temp:
    """Classe contenant plusieurs attributs, dont un temporaire"""
    
    def __init__(self):
        """Constructeur de notre objet"""
        self.attribut_1 = "une valeur"
        self.attribut_2 = "une autre valeur"
        self.attribut_temporaire = 5
   
    def __getstate__(self):
        """Renvoie le dictionnaire d'attributs à sérialiser"""
        dict_attr = dict(self.__dict__)
        dict_attr["attribut_temporaire"] = 0
        return dict_attr

###########################
# La méthode __setstate__ #
###########################

...
    def __setstate__(self, dict_attr):
        """Méthode appelée lors de la désérialisation de l'objet"""
        dict_attr["attribut_temporaire"] = 0
        self.__dict__ = dict_attr

 

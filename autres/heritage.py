# -*-coding:Utf-8 -*

#####################
# L'héritage simple #
#####################

class A:
    """Classe A, pour illustrer notre exemple d'héritage"""
    pass # On laisse la définition vide, ce n'est qu'un exemple

class B(A):
    """Classe B, qui hérite de A.
    Elle reprend les mêmes méthodes et attributs (dans cet exemple, la classe
    A ne possède de toute façon ni méthode ni attribut)"""
    
    pass

####################################################################################################################################
# Les méthodes et les attributs de la classe mère ne seront disponibles dans la classe fille que si ils n'y ont pas été redéfinies #
####################################################################################################################################

class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        self.nom = nom
        self.matricule = matricule
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

# Tests
agent = AgentSpecial("Fisher", "18327-121")
agent.nom # 'Fisher'
print(agent) # Agent Fisher, matricule 18327-121
agent.prenom
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'AgentSpecial' object has no attribute 'prenom'

####################################################################################################################################
# Mais on peut aussi se servir de la notation MaClasse.ma_methode(mon_objet) pour appeler une méthode précise d'une classe précise #
####################################################################################################################################

class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self, nom)
        self.matricule = matricule
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

# Tests
agent = AgentSpecial("Fisher", "18327-121")
agent.nom # 'Fisher'
print(agent) # Agent Fisher, matricule 18327-121
agent.prenom # 'Martin'

#################################
# Deux fonctions très pratiques #
#################################

# issubclass : vérifie si une classe est une sous-classe d'une autre classe
issubclass(AgentSpecial, Personne) # AgentSpecial hérite de Personne : True
issubclass(AgentSpecial, object) # True
issubclass(Personne, object) # True
issubclass(Personne, AgentSpecial) # Personne n'hérite pas d'AgentSpecial : False

# isinstance : permet de savoir si un objet est issu d'une classe ou de ses classes filles
agent = AgentSpecial("Fisher", "18327-121")
isinstance(agent, AgentSpecial) # Agent est une instance d'AgentSpecial : True
isinstance(agent, Personne) # Agent est une instance héritée de Personne : True

#######################
# L'héritage multiple #
#######################

# Syntaxe
class MaClasseHeritee(MaClasseMere1, MaClasseMere2):

########################################
# Création d'exceptions personnalisées #
########################################

# Nos exceptions doivent hériter d'une exception built-in proposée par Python. On utilisera plus fréquemment :
#   BaseException : pour modéliser une exception qui ne sera pas foncièrement une erreur, par exemple une interruption dans le traitement de votre programme.
#   Exception : la classe mère de toutes les exceptions « d'erreurs ».

####################
# Exception simple #
####################

class MonException(Exception):
    """Exception levée dans un certain contexte… qui reste à définir"""
    def __init__(self, message):
        """On se contente de stocker le message d'erreur"""
        self.message = message
    def __str__(self):
        """On renvoie le message"""
        return self.message

# Tests
raise MonException("OUPS... j'ai tout cassé")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MonException: OUPS... j'ai tout cassé

########################################
# Exceptions avec plusieurs paramètres #
########################################

class ErreurAnalyseFichier(Exception):
    """Cette exception est levée quand un fichier (de configuration)
    n'a pas pu être analysé.
    
    Attributs :
        fichier -- le nom du fichier posant problème
        ligne -- le numéro de la ligne posant problème
        message -- le problème proprement dit"""
    
    def __init__(self, fichier, ligne, message):
        """Constructeur de notre exception"""
        self.fichier = fichier
        self.ligne = ligne
        self.message = message
    def __str__(self):
        """Affichage de l'exception"""
        return "[{}:{}]: {}".format(self.fichier, self.ligne, \
                self.message)

# Tests
raise ErreurAnalyseFichier("plop.conf", 34,
...         "Il manque une parenthèse à la fin de l'expression")
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
__main__.ErreurAnalyseFichier: [plop.conf:34]: il manque une parenthèse à la fin de l'expression

# -*-coding:Utf-8 -*

###########################
# Exemples de déclaration #
###########################

# Exemple avec décorateur
@decorateur
def fonction(...):
    ...

# Exemple équivalent, sans décorateur
def fonction(...):
    ...
fonction = decorateur(fonction)

#########################
# Format le plus simple #
#########################

def mon_decorateur(fonction):
    """Premier exemple de décorateur"""
    print("Notre décorateur est appelé avec en paramètre la fonction {0}".format(fonction))
    return fonction

@mon_decorateur
def salut():
    """Fonction modifiée par notre décorateur"""
    print("Salut !")
# Résultat : le décorateur est éxecuté lors de la définition de la fonction, par de l'appel à la fonction
# Notre décorateur est appelé avec en paramètre la fonction <function salut at 0x00BA5198>

##############################################
# Modifier le comportement de notre fonction #
##############################################

def mon_decorateur(fonction):
    """Notre décorateur : il va afficher un message avant l'appel de la
    fonction définie"""
    
    def fonction_modifiee():
        """Fonction que l'on va renvoyer. Il s'agit en fait d'une version
        un peu modifiée de notre fonction originellement définie. On se
        contente d'afficher un avertissement avant d'exécuter notre fonction
        originellement définie"""
        
        print("Attention ! On appelle {0}".format(fonction))
        return fonction()
    return fonction_modifiee

@mon_decorateur
def salut():
    print("Salut !")

# Tests
salut()
# Attention ! On appelle <function salut at 0x00BA54F8>
# Salut !
salut
# <function fonction_modifiee at 0x00BA54B0>

###############################################################
# Autre éxemple de décorateur : chargé de lever une exception #
###############################################################

def obsolete(fonction_origine):
    """Décorateur levant une exception pour noter que la fonction_origine
    est obsolète"""
    
    def fonction_modifiee():
        raise RuntimeError("la fonction {0} est obsolète !".format(fonction_origine))
    return fonction_modifiee

#############################################
# Exemple de décorateur avec des paramètres #
#############################################

# Un exemple
@decorateur(parametre)
def fonction(...):
    ...

# Revient au même que
def fonction(...):
    ...
fonction = decorateur(parametre)(fonction)

#####################################
# Un décorateur avec des paramètres #
#####################################

"""Pour gérer le temps, on importe le module time
On va utiliser surtout la fonction time() de ce module qui renvoie le nombre
de secondes écoulées depuis le premier janvier 1970 (habituellement).
On va s'en servir pour calculer le temps mis par notre fonction pour
s'exécuter"""

import time

def controler_temps(nb_secs):
    """Contrôle le temps mis par une fonction pour s'exécuter.
    Si le temps d'exécution est supérieur à nb_secs, on affiche une alerte"""
    
    def decorateur(fonction_a_executer):
        """Notre décorateur. C'est lui qui est appelé directement LORS
        DE LA DEFINITION de notre fonction (fonction_a_executer)"""
        
        def fonction_modifiee():
            """Fonction renvoyée par notre décorateur. Elle se charge
            de calculer le temps mis par la fonction à s'exécuter"""
            
            tps_avant = time.time() # Avant d'exécuter la fonction
            valeur_renvoyee = fonction_a_executer() # On exécute la fonction
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'exécuter".format(fonction_a_executer, tps_execution))
            return valeur_renvoyee
        return fonction_modifiee
    return decorateur

# Tests
@controler_temps(4)
def attendre():
    input("Appuyez sur Entrée...")

attendre() # Je vais appuyer sur Entrée presque tout de suite
Appuyez sur Entrée...
attendre() # Cette fois, j'attends plus longtemps
Appuyez sur Entrée...
La fonction <function attendre at 0x00BA5810> a mis 4.14100003242 pour s'exécuter

# Exemple
@controler_temps(4)
def attendre(...)
    ...

# Revient au même que
def attendre(...):
    ...
attendre = controler_temps(4)(attendre)

#################################################
# Tenir compte des paramètres de notre fonction #
#################################################

...
        def fonction_modifiee(*parametres_non_nommes, **parametres_nommes):
            """Fonction renvoyée par notre décorateur. Elle se charge
            de calculer le temps mis par la fonction à s'exécuter"""
            
            tps_avant = time.time() # avant d'exécuter la fonction
            ret = fonction_a_executer(*parametres_non_nommes, **parametres_nommes)
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'exécuter".format( \
                        fonction_a_executer, tps_execution))
            return ret

###########################################################
# Des décorateurs s'appliquant aux définitions de classes #
###########################################################

def decorateur(classe):
    print("Définition de la classe {0}".format(classe))
    return classe

@decorateur
class Test:
    pass
# Résultat à l'éxecution du programme, pas à l'appel de la fonction
Définition de la classe <class '__main__.Test'>

###########################
# Chaîner nos décorateurs #
###########################

@decorateur1
@decorateur2
def fonction():

###########################
# Exemples d'applications #
###########################

#########################
# Les classes singleton #
#########################

def singleton(classe_definie):
    instances = {} # Dictionnaire de nos instances singletons
    def get_instance():
        if classe_definie not in instances:
            # On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance

# Tests
@singleton
class Test:
    pass
a = Test()
b = Test()
a is b # True

###############################################
# Contrôler les types passés à notre fonction #
###############################################

def controler_types(*a_args, **a_kwargs):
    """On attend en paramètres du décorateur les types souhaités. On accepte
    une liste de paramètres indéterminés, étant donné que notre fonction
    définie pourra être appelée avec un nombre variable de paramètres et que
    chacun doit être contrôlé"""
    
    def decorateur(fonction_a_executer):
        """Notre décorateur. Il doit renvoyer fonction_modifiee"""
        def fonction_modifiee(*args, **kwargs):
            """Notre fonction modifiée. Elle se charge de contrôler
            les types qu'on lui passe en paramètres"""
            
            # La liste des paramètres attendus (a_args) doit être de même
            # Longueur que celle reçue (args)
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas égal au nombre reçu")
            # On parcourt la liste des arguments reçus et non nommés
            for i, arg in enumerate(args):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type {1}".format(i, a_args[i]))
            
            # On parcourt à présent la liste des paramètres reçus et nommés
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {0} n'a aucun type précisé".format(repr(cle)))
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("l'argument {0} n'est pas de type" {1}".format(repr(cle), a_kwargs[cle]))
            return fonction_a_executer(*args, **kwargs)
        return fonction_modifiee
    return decorateur

# Tests
@controler_types(int, int)
def intervalle(base_inf, base_sup):
    print("Intervalle de {0} à {1}".format(base_inf, base_sup))

intervalle(1, 8) # Intervalle de 1 à 8
intervalle(5, "oups!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 24, in fonction_modifiee
TypeError: l'argument 1 n'est pas du type <class 'int'>

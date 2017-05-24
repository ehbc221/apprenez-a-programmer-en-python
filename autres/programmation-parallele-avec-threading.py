# -*-coding:Utf-8 -*

#######################
# Création de threads #
#######################

import random
import sys
from threading import Thread
import time

class Afficheur(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1

# Création des threads
thread_1 = Afficheur("1")
thread_2 = Afficheur("2")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

# Résultat : 1221121212122121211221122212121221121211

####################################
# Accès simultané à des ressources #
####################################

import random
import sys
from threading import Thread
import time

class Afficheur(Thread):

    """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 5:
            for lettre in self.mot:
                sys.stdout.write(lettre)
                sys.stdout.flush()
                attente = 0.2
                attente += random.randint(1, 60) / 100
                time.sleep(attente)
            i += 1

# Création des threads
thread_1 = Afficheur("canard")
thread_2 = Afficheur("TORTUE")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

# Résultat : cTORanaTUrEdcTaOnRarTdUcEanTaOrRdTcUaEnTaORrdTcanUaErdTORTUE

####################################################################################
# Les locks à la rescousse : synchronisation des threads avec les locks (<<lock>>) #
####################################################################################

import random
import sys
from threading import Thread, RLock
import time

verrou = RLock()

class Afficheur(Thread):

    """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 5:
            with verrou: # On utilise là encore un context manager pour indiquer quand bloquer le lock. Le lock se débloque à la fin du bloc with
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            i += 1

# Création des threads
thread_1 = Afficheur("canard")
thread_2 = Afficheur("TORTUE")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

# Résultat : canardcanardTORTUETORTUEcanardcanardcanardTORTUETORTUETORTUE

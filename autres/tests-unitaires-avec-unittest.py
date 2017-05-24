# -*-coding:Utf-8 -*

########################################
# Premiers exemples de tests unitaires #
########################################

#################
# random.choice #
#################

import random
import unittest

class RandomTest(unittest.TestCase):
    
    """Test case utilisé pour tester les fonctions du module 'random'."""

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, liste)

# Test : NB => L'appel à unittest.main ferme la console Python
unittest.main()

##################
# random.shuffle #
##################

import random
import unittest

class RandomTest(unittest.TestCase):
    
    """Test case utilisé pour tester les fonctions du module 'random'."""

    # Autres méthodes de test
    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        liste = list(range(10))
        random.shuffle(liste)
        liste.sort()
        # assertEqual qui prend deux arguments en paramètre et vérifie le test si les arguments sont identiques
        self.assertEqual(liste, list(range(10)))

# Test : NB => L'appel à unittest.main ferme la console Python
unittest.main()

#################
# random.sample #
#################

import random
import unittest

class RandomTest(unittest.TestCase):
    
    """Test case utilisé pour tester les fonctions du module 'random'."""

    # Autres méthodes de test
    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        liste = list(range(10))
        extrait = random.sample(liste, 5)
        for element in extrait:
            self.assertIn(element, liste)

        with self.assertRaises(ValueError):
            random.sample(liste, 20)

# Test : NB => L'appel à unittest.main ferme la console Python
unittest.main()

############################
# Initialisation des tests #
############################

class RandomTest(unittest.TestCase):
    
    """Test case utilisé pour tester les fonctions du module 'random'."""

    # Autres méthodes de test
    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)

        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)

#########################################
# Récapitulatif complet du code de test #
#########################################

import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        self.liste = list(range(10))

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste)
        self.assertIn(elt, self.liste)

    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)))

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)

        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)

########################################
# Les principales méthodes d'assertion #
########################################

assertEqual(a, b) # a == b
assertNotEqual(a, b) # a != b
assertTrue(x) # x is True
assertFalse(x) # x is False
assertIs(a, b) # a is b
assertIsNot(a, b) # a is not b
assertIsNone(x) # x is None
assertIsNotNone(x) # x is not None
assertIn(a, b) # a in b
assertNotIn(a, b) # a not in b
assertIsInstance(a, b) # isinstance(a, b)
assertNotIsInstance(a, b) # not isinstance(a, b)
assertRaises(exception, fonction, *args, **kwargs) # Vérifie que la fonction lève l'exception attendue.

#######################################
# La découverte automatique des tests #
#######################################

# Lancement de tests unitaires depuis un répertoire
import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        self.liste = list(range(10))

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste)
        self.assertIn(elt, self.liste)

    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)))

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)

        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)

# Tests
python3 -m unittest
# Ou plus précisement
python3 -m unittest test_random.RandomTest.test_shuffle # nom_module.nom_classe.nom_methode

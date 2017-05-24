# -*-coding:Utf-8 -*

##################
# Le module math #
##################

import math

math.pow(5, 2) # 5 au carré
25.0
5 ** 2 # Pratiquement identique à pow(5, 2)
25
math.sqrt(25) # Racine carrée de 25 (square root)
5.0
math.exp(5) # Exponentielle
148.4131591025766
math.fabs(-3) # Valeur absolue
3.0

##############################################################################
# Un peu de trigonométrie. NB: les angles sont donnés et renvoyés en radians #
##############################################################################

math.degrees(angle_en_radians) # Convertit en degrés
math.radians(angle_en_degrés) # Convertit en radians

# Quelques fonctions
cos : cosinus
sin : sinus
tan : tangente
acos : arc cosinus
asin : arc sinus
atan : arc tangente

# Arrondir un nombre
math.ceil(2.3) # Renvoie le plus petit entier >= 2.3
3
math.floor(5.8) # Renvoie le plus grand entier <= 5.8
5
math.trunc(9.5) # Tronque 9.5
9

# Constantes
math.pi
math.e

##########################################
# Des fractions avec le module fractions #
##########################################

from fractions import Fraction

un_demi = Fraction(1, 2)
un_demi
Fraction(1, 2)
un_quart = Fraction('1/4')
un_quart
Fraction(1, 4)
autre_fraction = Fraction(-5, 30)
autre_fraction
Fraction(-1, 6)

# Fractions depuis un flottant
Fraction.from_float(0.5)
Fraction(1, 2)

# Sens inverse
float(un_quart)
0.25

# Manipuler les fractions
un_dixieme = Fraction(1, 10)
un_dixieme + un_dixieme + un_dixieme
Fraction(3, 10)

un_quart = Fraction(1, 4)
un_dixieme * un_quart
Fraction(1, 40)
un_dixieme + 5
Fraction(51, 10)
un_demi / un_quart
Fraction(2, 1)
un_quart / un_demi
Fraction(1, 2)

###################################
# Du pseudo-aléatoire avec random #
###################################

# La fonction random
import random
random.random()
0.9565461152605507

# randrange et randint
random.randrange(5, 10, 2) # Cette instruction va chercher à générer un nombre aléatoire entre 5 inclus et 10 non inclus, avec un écart de 2 entre chaque valeur. Elle va donc chercher dans la liste des valeurs [5, 7, 9].
random.randint(1, 6) # tirer au hasard un nombre entre 1 et 6

# choice
random.choice(['a', 'b', 'k', 'p', 'i', 'w', 'z']) # 'k'
liste = ['a', 'b', 'k', 'p', 'i', 'w', 'z']

# shuffle
random.shuffle(liste)
liste # ['p', 'k', 'w', 'z', 'i', 'b', 'a']

# sample
liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
random.sample(liste, 5) # ['b', 'a', 'c', 'j', 'e']
# Ou peut-être que cet exemple sera plus clair
$random.sample(range(1000), 10) # [389, 406, 890, 955, 837, 401, 971, 716, 954, 862]

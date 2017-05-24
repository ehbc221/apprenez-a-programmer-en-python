# -*-coding:Utf-8 -*

##################
# Les itérateurs #
##################

ma_chaine = "test"
iterateur_de_ma_chaine = iter(ma_chaine)
iterateur_de_ma_chaine # <str_iterator object at 0x00B408F0>
next(iterateur_de_ma_chaine) # 't'
next(iterateur_de_ma_chaine) # 'e'
next(iterateur_de_ma_chaine) # 's'
next(iterateur_de_ma_chaine) # 't'
next(iterateur_de_ma_chaine)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

#########################
# Créons nos itérateurs #
#########################

class RevStr(str):
    """Classe reprenant les méthodes et attributs des chaînes construites
    depuis 'str'. On se contente de définir une méthode de parcours
    différente : au lieu de parcourir la chaîne de la première à la dernière
    lettre, on la parcourt de la dernière à la première.
    
    Les autres méthodes, y compris le constructeur, n'ont pas besoin
    d'être redéfinies"""
    
    def __iter__(self):
        """Cette méthode renvoie un itérateur parcourant la chaîne
        dans le sens inverse de celui de 'str'"""
        
        return ItRevStr(self) # On renvoie l'itérateur créé pour l'occasion

class ItRevStr:
    """Un itérateur permettant de parcourir une chaîne de la dernière lettre
    à la première. On stocke dans des attributs la position courante et la
    chaîne à parcourir"""
    
    def __init__(self, chaine_a_parcourir):
       """On se positionne à la fin de la chaîne"""
        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)
    def __next__(self):
        """Cette méthode doit renvoyer l'élément suivant dans le parcours,
        ou lever l'exception 'StopIteration' si le parcours est fini"""
        
        if self.position == 0: # Fin du parcours
            raise StopIteration
        self.position -= 1 # On décrémente la position
        return self.chaine_a_parcourir[self.position]

# Tests
ma_chaine = RevStr("Bonjour")
ma_chaine # 'Bonjour'
for lettre in ma_chaine:
    print(lettre)
# Résultat
r
u
o
j
n
o
B

###################
# Les générateurs #
###################

# Les générateurs simples
def mon_generateur():
    """Notre premier générateur. Il va simplement renvoyer 1, 2 et 3"""
    yield 1
    yield 2
    yield 3

mon_generateur
<function mon_generateur at 0x00B494F8>
mon_generateur()
<generator object mon_generateur at 0x00B9DC88>
# on doit exécuter la fonction mon_generateur() pour obtenir un générateur
mon_iterateur = iter(mon_generateur())
next(mon_iterateur) # 1
next(mon_iterateur) # 2
next(mon_iterateur) # 3
next(mon_iterateur)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

# Tests 2
for nombre in mon_generateur(): # Attention on exécute la fonction mon_generateur(), pas mon_generateur
    print(nombre)
# Résultat
1
2
3

# Générateur nombre entier
def intervalle(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
    
    Note: borne_inf doit être inférieure à borne_sup"""
    
    borne_inf += 1
    while borne_inf < borne_sup:
        yield borne_inf
        borne_inf += 1

# Tests
for nombre in intervalle(5, 10):
    print(nombre)
# Résultat
6
7
8
9

#####################################
# Les générateurs comme co-routines #
#####################################

# Interrompre la boucle
generateur = intervalle(5, 20)
for nombre in generateur:
    if nombre > 17:
        generateur.close() # Interruption de la boucle

# Envoyer des données à notre générateur
def intervalle(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
    Notre générateur doit pouvoir "sauter" une certaine plage de nombres
    en fonction d'une valeur qu'on lui donne pendant le parcours. La
    valeur qu'on lui passe est la nouvelle valeur de borne_inf.
    
    Note: borne_inf doit être inférieure à borne_sup"""
    borne_inf += 1
    while borne_inf < borne_sup:
        valeur_recue = (yield borne_inf)
        if valeur_recue is not None: # Notre générateur a reçu quelque chose
            borne_inf = valeur_recue
        borne_inf += 1
# Tests
generateur = intervalle(10, 25)
for nombre in generateur:
    if nombre == 15: # On saute à 20
        generateur.send(20)
    print(nombre, end=" ")


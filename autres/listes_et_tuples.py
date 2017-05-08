# -*-coding:Utf-8 -*

##############
# Les listes #
##############

ma_liste = list() # initialisation 1
ma_liste = [] # initialisation 2
ma_liste = ['c', 'f', 'm']
ma_liste[0] # On accède au premier élément de la liste (c)
ma_liste[2] # Troisième élément (m)
ma_liste[1] = 'Z' # On remplace 'f' par 'Z'
ma_liste # ['c', 'Z', 'm']
# Ajouter un élément à la fin de la liste
ma_liste.append("O") # ['c', 'Z', 'm', O]
# Insérer un élément dans la liste
ma_liste.insert(2, "a") # insérer "a" à la 2ème position : ['c', 'Z', 'a', 'm', 'O']
# Concatener 2 listes
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
ma_liste1.extend(ma_liste2) # 1ère méthode : on insère ma_liste2 à la fin de ma_liste1 : [3, 4, 5, 8, 9, 10]
ma_liste1 = [3, 4, 5]
ma_liste1 + ma_liste2 # 2ème méthode (juste pour l'affichage car ne modifie pas la liste, renvoie juste les 2 listes): [3, 4, 5, 8, 9, 10]
ma_liste1 += ma_liste2 # 3ème méthode : dentique à extend : [3, 4, 5, 8, 9, 10]
# Suppression d'éléments d'une liste
ma_liste = ['c', 'Z', 'a', 'm', 'O']
del ma_liste[0] # Avec del : l'indice de l'élément à supprimer ('c')
ma_liste.remove('m') # Avec remove : l'élément lui meme

##########################
# Le parcours des listes #
##########################

# 1ère méthode
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

i = 0 # Notre indice pour la boucle while
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1 # On incrémente i, ne pas oublier !
# 2ème méthode : cette méthode est cependant préférable
for elt in ma_liste: # elt va prendre les valeurs successives des éléments de ma_liste
    print(elt)
# La fonction enumerate
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, elt in enumerate(ma_liste): # i l'indice, elt l'élément en cours
    print("À l'indice {} se trouve {}.".format(i, elt))

##################################
# Un petit coup d'œil aux tuples #
##################################

tuple_vide = ()
tuple_non_vide = (1,) # est équivalent à ci dessous
tuple_non_vide = 1,
tuple_avec_plusieurs_valeurs = (1, 2, 5)
# Affectation multiple
a, b = 3, 4
# Une fonction renvoyant plusieurs valeurs
def decomposer(entier, divise_par):
    """Cette fonction retourne la partie entière et le reste de
    entier / divise_par"""

    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste
partie_entiere, reste = decomposer(20, 3) # partie_entiere = 6 et reste = 2

###########################
# Entre chaînes et listes #
###########################

# Des chaînes aux listes : split("séparateur")
ma_chaine = "Bonjour à tous"
ma_chaine.split(" ") # ['Bonjour', 'à', 'tous']
# Des listes aux chaînes : "séparateur".join(liste_à_fusionner)
ma_liste = ['Bonjour', 'à', 'tous']
" ".join(ma_liste) # 'Bonjour à tous'
# Exemple :
def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.
    De plus, on va remplacer le point décimal par la virgule"""
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])

###########################################################################
# Les fonctions dont on ne connaît pas à l'avance le nombre de paramètres #
###########################################################################

def fonction_inconnue(*parametres):
    """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""
    print("J'ai reçu : {}.".format(parametres))
fonction_inconnue() # J'ai reçu : ().
fonction_inconnue(33) # J'ai reçu : (33,).
fonction_inconnue('a', 'e', 'f') # J'ai reçu : ('a', 'e', 'f').
var = 3.5
fonction_inconnue(var, [4], "...") # J'ai reçu : (3.5, [4], '...').

########################################
# Exemple : fonction identique à print #
########################################

def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction chargée de reproduire le comportement de print.
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés. 
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :
    print(chaine, end='')"""
    # Les paramètres sont sous la forme d'un tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilités, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en chaîne
    # Sinon on va avoir quelques problèmes lors du join
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # La liste des paramètres ne contient plus que des chaînes de caractères
    # À présent on va constituer la chaîne finale
    chaine = sep.join(parametres)
    # On ajoute le paramètre fin à la fin de la chaîne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')

###################################################
# Transformer une liste en paramètres de fonction #
###################################################

liste_des_parametres = [1, 4, 9, 16, 25, 36]
print(*liste_des_parametres) # 1 4 9 16 25 36

###############################
# Les compréhensions de liste #
###############################

# Parcours simple
liste_origine = [0, 1, 2, 3, 4, 5]
[nb * nb for nb in liste_origine] # [0, 1, 4, 9, 16, 25], nb * nb revient à écrire nb ** 2

# Filtrage avec un branchement conditionnel
liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[nb for nb in liste_origine if nb % 2 == 0] # [2, 4, 6, 8, 10]

# Filtrer et modifier une liste (partie 1)
qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21] # Par exemple 15 pommes, 3 melons...
[nb_fruits - qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits > qtt_a_retirer] # [8, 11, 14]

# Filtrer et modifier une liste (partie 2)
inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]
# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
# On trie l'inventaire inversé dans l'ordre décroissant
inventaire_inverse.sort(reverse=True)
# Et on reconstitue l'inventaire
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in inventaire_inverse]

# -*-coding:Utf-8 -*

###########################
# La portée des variables #
###########################

# Dans nos fonctions, quelles variables sont accessibles ?
# Quand une variable n'est pas déclarée dans la fonction, Python la cherche dans l'espace local où la fonction est appelée
a = 5
def print_a():
    """Fonction chargée d'afficher la variable a.
    Cette variable a n'est pas passée en paramètre de la fonction.
    On suppose qu'elle a été créée en dehors de la fonction, on veut voir
    si elle est accessible depuis le corps de la fonction"""

    print("La variable a = {0}.".format(a))
print_a() # La variable a = 5.
a = 8
print_a() # La variable a = 8.

# Qu'advient-il des variables définies dans un corps de fonction ?
# Elles ne sont pas accessibles à l'éxtérieur de la fonction
# une fonction ne peut modifier, par affectation, la valeur d'une variable extérieure à son espace local.
def set_var(nouvelle_valeur):
    """Fonction nous permettant de tester la portée des variables
    définies dans notre corps de fonction"""
    
    # On essaye d'afficher la variable var, si elle existe
    try:
        print("Avant l'affectation, notre variable var vaut {0}.".format(var))
    except NameError:
        print("La variable var n'existe pas encore.")
    var = nouvelle_valeur
    print("Après l'affectation, notre variable var vaut {0}.".format(var))
set_var(5) # La variable var n'existe pas encore. Après l'affectation, notre variable var vaut 5.
var # NameError: name 'var' is not defined

# Une fonction modifiant des objets
# Dans le corps de fonction, si vous faites parametre = nouvelle_valeur, le paramètre ne sera modifié que dans le corps de la fonction.
# Alors que si vous faites parametre.methode_pour_modifier(…), l'objet derrière le paramètre sera bel et bien modifié.
def ajouter(liste, valeur_a_ajouter):
    """Cette fonction insère à la fin de la liste la valeur que l'on veut ajouter"""
    liste.append(valeur_a_ajouter)
ma_liste=['a', 'e', 'i']
ajouter(ma_liste, 'o') # ['a', 'e', 'i', 'o']

# Et les références, dans tout cela ?
# On dit que ma_liste1 et ma_liste2 contiennent une référence vers le même objet :
# Si on modifie l'objet depuis une des deux variables, le changement sera visible depuis les deux variables.
ma_liste1 = [1, 2, 3]
ma_liste2 = ma_liste1
ma_liste2.append(4)
print(ma_liste2) # [1, 2, 3, 4]
print(ma_liste1) # [1, 2, 3, 4]

# Et si je veux modifier une liste sans toucher à l'autre ?
ma_liste1 = [1, 2, 3]
ma_liste2 = list(ma_liste1) # Cela revient à copier le contenu de ma_liste1
ma_liste2.append(4)
print(ma_liste2) # [1, 2, 3, 4]
print(ma_liste1) # [1, 2, 3]

# Comparer 2 objets et leurs réference (is)
ma_liste1 = [1, 2]
ma_liste2 = [1, 2]
ma_liste1 == ma_liste2 # On compare le contenu des listes : True
ma_liste1 is ma_liste2 # On compare leur référence : False

##########################
# Les variables globales #
##########################

# Utiliser concrètement les variables globales (global)
i = 4 # Une variable, nommée i, contenant un entier
def inc_i():
    """Fonction chargée d'incrémenter i de 1"""
    global i # Python recherche i en dehors de l'espace local de la fonction
    i += 1
i # 4
inc_i()
i # 5

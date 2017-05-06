# -*-coding:Utf-8 -*

from random import randrange
from math import ceil

# Solde du jouueur
solde = 1000
print("\nVotre solde est de:", solde, "$.")

# Jouer tant que le solde du compte nous le permet
game_over = False
while game_over == False:
    # Pour le numéro choisi
    validation = False
    while validation == False:
        validation = True
        numero_mise = input("\nDonnez le numéro sur lequel vous voulez miser (entre 0 et 49): ")
        try:
            numero_mise = int(numero_mise)
            assert numero_mise >= 0 and numero_mise <= 49
        except ValueError:
            validation = False
            print("Vous n'avez pas saisi un nombre.")
        except AssertionError:
            validation = False
            print("Le nombre saisi n'est pas compris entre 0 et 49.")

    # Pour la mise
    validation = False
    while validation == False:
        validation = True
        print("\nDonnez la somme que vous voulez miser sur le numéro", numero_mise, ": ")
        somme_mise = input()
        try:
            somme_mise = int(somme_mise)
            assert somme_mise <= solde
        
        except ValueError:
            validation =  False
            print("Vous n'avez pas saisi un nombre.")
        except AssertionError:
            validation = False
            print("Vous ne pouvez pas miser une somme supérieure à votre solde.")

    # Solde restant
    solde -= somme_mise
    print("Le solde restant :", solde)

    # Génération d'un nombre aléatoire(entre 0 et 49)
    input("\nMise et numéro enregistrés avec succès. Tapez ENTREE pour continuer...")
    roulette = randrange(50)
    print("\nLe numéro tiré par la roulette est :", roulette)

    # Mise à jour du solde du joueur
    if roulette == numero_mise:
        solde += somme_mise * 3
        print("Bravo, vous avez tiré le bon numéro")
    elif roulette % 2 == 0 and numero_mise % 2 == 0 or (roulette % 2 != 0 and numero_mise % 2 != 0):
        solde += ceil(somme_mise / 2)
        print("Ohh, vous n'avez pas choisi le bon numéro. Mais vous reprenez quand même la moitié de votre mise(le numéro misé et le numéro gagnant ont la même couleur).")
    else:
        print("Dommage, vous n'avez rien remporté sur ce tour.")

    # Affichage du nouveau solde
    print("Votre nouveau solde est de :", solde, "$.")

    # Vérifier si le jeu continue ou non
    if solde <= 0:
        game_over = True
        print("\nDésolé, votre solde n'est plus suffisant pour continuer. Merci d'avoir joué.")
        print("Solde final :", solde, "$.")
    else:
        game_over = False

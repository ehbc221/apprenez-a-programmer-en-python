# -*-coding:Utf-8 -*

#############################
# Accéder aux flux standard #
#############################

import sys
sys.stdin # L'entrée standard (standard input)
<_io.TextIOWrapper name='<stdin>' encoding='cp850'>
sys.stdout # La sortie standard (standard output)
<_io.TextIOWrapper name='<stdout>' encoding='cp850'>
sys.stderr # L'erreur standard (standard error)
<_io.TextIOWrapper name='<stderr>' encoding='cp850'>

sys.stdout.write("Un test\n")
Un test
8

##############################
# Modifier les flux standard #
##############################

fichier = open('sortie.txt', 'w')
sys.stdout = fichier
print("Quelque chose...")

# Retablir le flux normal
sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

# Connaître l'emplacement du répertoire courant de Python
import os
os.getcwd()

###############
# Les signaux #
###############

# Importer le module signal
import signal

# Intercepter un signal
signal.SIGINT # 2

#########################
# Intercepter un signal #
#########################

import signal
import sys

def fermer_programme(signal, frame):
    """Fonction appelée quand vient l'heure de fermer notre programme"""
    print("C'est l'heure de la fermeture !")
    sys.exit(0)

# Connexion du signal à notre fonction
signal.signal(signal.SIGINT, fermer_programme)

# Notre programme...
print("Le programme va boucler...")
while True: # CTRL + C opur arreter cette boucle infinie
    continue

#####################################################
# Interpréter les arguments de la ligne de commande #
#####################################################

# Interpréter les arguments de la ligne de commande sys.argv
import sys

if len(sys.argv) < 2:
    print("Précisez une action en paramètre")
    sys.exit(1)

action = sys.argv[1]

if action == "start":
    print("On démarre l'opération")
elif action == "stop":
    print("On arrête l'opération")
elif action == "restart":
    print("On redémarre l'opération")
elif action == "status":
    print("On affiche l'état (démarré ou arrêté ?) de l'opération")
else:
    print("Je ne connais pas cette action")

##############################
# Des options plus complexes #
##############################

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="le nombre à mettre au carré")
parser.add_argument("-v", "--verbose", action="store_true",
        help="augmente la verbosité")
args = parser.parse_args()

x = args.x
retour = x ** 2
if args.verbose:
    print("{} ^ 2 = {}".format(x, retour))
else:
    print(retour)

###############################################
# Exécuter une commande système depuis Python #
###############################################

# La fonction system
os.system("ls") # Sur Linux
os.system("dir") # Sur Windows

# La fonction popen
import os
cmd = os.popen("ls")
cmd
<os._wrap_close object at 0x7f81d16554d0>
cmd.read()
'fichier1.txt\nimage.png\n'                                                     

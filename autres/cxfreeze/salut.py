# -*-coding:Utf-8 -*

"""Ce fichier affiche simplement une ligne grâce à la fonction print."""

from sys import platform as _platform

print("Salut le monde !")

# Sous Windows il faut mettre ce programme en pause (inutile sous Linux)
if _platform == "win32":
    import os
    os.system("pause")

# Méthode 1 (terminal) : cxfreeze salut.py
# Méthode 2 (terminal) : créer le fichier sétup, puis taper : python3 setup.py build (voir ./setup.py)

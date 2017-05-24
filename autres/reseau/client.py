# -*-coding:Utf-8 -*

######################
# Création du client #
######################

import socket
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecter le client : connect(nom_d'hôte, numéro_du_port)
connexion_avec_serveur.connect(('localhost', 12800))

# Faire communiquer nos sockets : recevoir avec => recv (nombre de caractères à lire)
msg_recu = connexion_avec_serveur.recv(1024)
msg_recu # b"Je viens d'accepter la connexion"

# Fermer la connexion
connexion_avec_serveur.close()


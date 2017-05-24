# -*-coding:Utf-8 -*

#######################
# Crétaion du serveur #
#######################

import socket

# Construire notre socket : socket(socket.AF_INET : la famille d'adresses, ici ce sont des adresses Internet, socket.SOCK_STREAM : le type du socket, SOCK_STREAM pour le protocole TCP)
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecter le socket : bind(nom_hote, port)
connexion_principale.bind(('', 12800))

# Faire écouter notre socket : listen(nombre_maximum_de_connexions)
connexion_principale.listen(5)

# Accepter une connexion venant du client : acceptrenvoie deux information :
#                                               le socket connecté qui vient de se créer, celui qui va nous permettre de dialoguer avec notre client tout juste connecté
#                                               un tuple représentant l'adresse IP et le port de connexion du client
connexion_avec_client, infos_connexion = connexion_principale.accept()

# Vérifier les informations de connexion après que la méthode accept ne bloque plus (si elle a acceptée la connexion demandée par le client)
print(infos_connexion)
('127.0.0.1', 2901) # (adresse IP du client, port de sortie du client)

# Faire communiquer nos sockets : envoie avec => send (Les informations que vous transmettrez seront des chaînes de bytes, pas des str)
connexion_avec_client.send(b"Je viens d'accepter la connexion")

# Fermer la connexion
connexion_avec_client.close()

# -*-coding:Utf-8 -*

##################
# Le module time #
##################

import time
debut = time.time()
# On attend quelques secondes avant de taper la commande suivante
fin = time.time()
print(debut, fin) # 1297642195.45 1297642202.27
debut < fin # True
fin - debut # Combien de secondes entre debut et fin ?
6.812000036239624

################################################
# La date et l'heure de façon plus présentable #
################################################

# la fonction localtime du module time
time.localtime()
time.struct_time(tm_year=2011, tm_mon=2, tm_mday=14, tm_hour=3, tm_min=22, tm_sec=7, tm_wday=0, tm_yday=45, tm_isdst=0)
time.localtime(debut)
time.struct_time(tm_year=2011, tm_mon=2, tm_mday=14, tm_hour=1, tm_min=9, tm_sec=55, tm_wday=0, tm_yday=45, tm_isdst=0)
time.localtime(fin)
time.struct_time(tm_year=2011, tm_mon=2, tm_mday=14, tm_hour=1, tm_min=10, tm_sec=2, tm_wday=0, tm_yday=45, tm_isdst=0)

# Récupérer un timestamp depuis une date
print(debut) # 1297642195.45
temps = time.localtime(debut)
print(temps) # time.struct_time(tm_year=2011, tm_mon=2, tm_mday=14, tm_hour=1, tm_min=9, tm_sec=55, tm_wday=0, tm_yday=45, tm_isdst=0)
ts_debut = time.mktime(temps)
print(ts_debut) # 1297642195.0

# Mettre en pause l'exécution du programme pendant un temps déterminé
time.sleep(3.5) # Faire une pause pendant 3,5 secondes

# Formater un temps
time.strftime('%Y')
%A # Nom du jour de la semaine
%B # Nom du mois
%d # Jour du mois (de 01 à 31)
%H # Heure (de 00 à 23)
%M # Minute (entre 00 et 59)
%S # Seconde (de 00 à 59)
%Y # Année

######################
# Le module datetime #
######################

import datetime

########################
# Représenter une date #
########################

# Construire notre objet date
date = datetime.date(2010, 12, 25)
print(date) # 2010-12-25

# Autres méthodes de construction
import time
import datetime
aujourdhui = datetime.date.today()
aujourdhui # datetime.date(2011, 2, 14)
datetime.date.fromtimestamp(time.time()) # Équivalent à date.today
datetime.date(2011, 2, 14)

#########################
# Représenter une heure #
#########################

import datetime
datetime.time(hour, minute, second, microsecond, tzinfo)
# On construit une heure avec non pas trois mais cinq paramètres, tous optionnels :
hour (0 par défaut) : les heures, valeur comprise entre 0 et 23 ;
minute (0 par défaut) : les minutes, valeur comprise entre 0 et 59 ;
second (0 par défaut) : les secondes, valeur comprise entre 0 et 59 ;
microsecond (0 par défaut) : la précision de l'heure en micro-secondes, entre 0 et 1.000.000 ;
tzinfo (None par défaut) : l'information de fuseau horaire

###################################
# Représenter des dates et heures #
###################################

import datetime
datetime.datetime.now() # renvoie l'objet datetime avec la date et l'heure actuelles
datetime.fromtimestamp(timestamp) # renvoie la date et l'heure d'un timestamp précis
datetime.datetime(2011, 2, 14, 5, 8, 22, 359000)

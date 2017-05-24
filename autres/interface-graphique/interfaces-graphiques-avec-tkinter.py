# -*-coding:Utf-8 -*

###########################
# Présentation de Tkinter #
###########################

from Tkinter import *

######################################
# Votre première interface graphique #
######################################

"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from Tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(fenetre, text="Salut les Zér0s !")

# On affiche le label dans la fenêtre
champ_label.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

##############
# Les labels #
##############
champ_label = Label(fenetre, text="contenu de notre champ label")
champ_label.pack()

###############
# Les boutons #
##############
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()

#######################
# Une ligne de saisie #
#######################
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()
# il éxiste  également le widget Text qui représente un champ de texte à plusieurs lignes

######################
# Les cases à cocher #
######################
var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()
# On peut ensuite contrôler l'état de la case à cocher en interrogeant la variable var_case.get()
# Si la case est cochée, la valeur renvoyée par la variable sera 1. Si elle n'est pas cochée, ce sera 0.
# A l'instar d'un bouton, vous pouvez lier la case à cocher à une commande qui sera appelée quand son état change.

#####################
# Les boutons radio #
#####################
var_choix = StringVar()

choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()
# Pour récupérer la valeur associée au bouton actuellement sélectionné, interrogez la variable var_choix.get()

##########################
# Les listes déroulantes #
##########################
liste = Listbox(fenetre)
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")
liste.pack()
# Pour accéder à la sélection, utilisez la méthode curselection de la liste.
# Elle renvoie un tuple de chaînes de caractères, chacune étant la position de l'élément sélectionné.
# Par exemple, si liste.curselection() renvoie ('2',), c'est le troisième élément de la liste qui est sélectionné (Ciseau en l'occurrence).

#########################################
# Organiser ses widgets dans la fenêtre #
#########################################
cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)
message = Label(cadre, text="Notre fenêtre")
message.pack(side="top", fill=X)

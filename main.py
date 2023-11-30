from fonctions import *
mot_a_trouver = choisir_mot()
progression = initialisation_progression(mot_a_trouver)
affichage_tiret(progression)
erreur = 0
while erreur < 5:
    progression, erreur = update_progression(demander_choix(), mot_a_trouver, progression, erreur)
    dessin_pendu(erreur)
    affichage_tiret(progression)
print("perdu!")
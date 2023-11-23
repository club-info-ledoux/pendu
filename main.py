mot_a_trouver = choisir_mot()
progression = initialisation_progression(mot_a_trouver)
affichage_tiret(progression)
erreur = 0
while erreur < 5:
    demander_choix()
    
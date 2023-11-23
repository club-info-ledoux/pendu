def verifiaction(lettre_choisie):
    for i in range(len(mot_a_trouver)):
        if lettre_choisie == mot_a_trouver[i]:
            progression(lettr_choisie)
        else:
            erreur += 1

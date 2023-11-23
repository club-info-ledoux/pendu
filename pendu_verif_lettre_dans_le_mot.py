def verification(mot_a_trouver, lettre_choisie):
    global erreur
    lettre_bonne = []
    for i in range(len(mot_a_trouver)):
        if lettre_choisie == mot_a_trouver[i]:
            lettre_bonne.append(i)
    if lettre_bonne == []:
        erreur += 1
        return erreur
    return lettre_bonne

def deja_utilise(lettre_choisie, proposition):
    for a in range(len(lettre_choisie)):
        if proposition[a] == lettre_choisie:
            return False
        else:
            return True

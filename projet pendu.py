# Créé par Samson.webervillaumi, le 16/11/2023 en Python 3.7


def progression(lettre,mot,progression):
    positions_lettre = verification(mot,lettre)
    for pos in positions_lettre:
        progression[pos] = lettre
    return progression
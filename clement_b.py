# Créé par clement.brager, le 16/11/2023 en Python 3.7
#update tirert
def initialisation_progression(mot_a_trouver):
    progression="_"
    for i in range(len(mot_a_trouver)-1):
        progression+="_"
    return progression

def affichage_tiret(progression):
    affichage=""
    for n in range(len(progression)):
        affichage+= progression[n]+" "
    print("progression du mot: ")
    print(affichage)








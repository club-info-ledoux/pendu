# Créé par clement.mathieu, le 16/11/2023 en Python 3.7

#importation des modules


def lechoix():

    choix=input("Quelle lettre voulez vous essayer ? ")
    while len(choix)!=1 or choix.isalpha()==False:       #isalpha() envoie True si ce n'est que des lettres
        choix=input("N'entrez qu'une lettre")
    if choix.isupper()==False:                           #isupper() envoie True si les lettres sont toutes en majuscules
        choix=choix.upper()                              #upper() mets toutes le lettres en majuscules tout mettre en majuscules
    progression=choix
    return progression













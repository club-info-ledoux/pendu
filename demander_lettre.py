def demander_choix():
    choix=input("Quelle lettre voulez vous essayer ? ")
    while len(choix)!=1 or not choix.isalpha():       #isalpha() envoie True si ce n'est que des lettres
        choix=input("N'entrez qu'une lettre")
    choix=choix.upper()                              #upper() mets toutes le lettres en majuscules tout mettre en majuscules
    progression=choix
    return progression

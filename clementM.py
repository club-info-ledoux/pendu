# Créé par clement.mathieu, le 16/11/2023 en Python 3.7

#importation des modules


def lechoix():
    valide=False
    choix=input("Quelle lettre voulez vous essayer ? ")
    while not valide:
        if choix.isalpha() and choix.isupper():


                        #teste si ce sont tous des lettres.




#choix.isalpha() envoie True si ce n'est que des lettres
#choix.isupper() envoie True si les lettres sont toutes en majuscules
#upper() mets btoutes le lettres en majuscules tout mettre en majuscules.
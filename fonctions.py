import random

def choisir_mot():
    #choisir un mot aléatoir dans le fichier dico.txt
    fichier_dico = open("dico.txt", 'r', encoding='utf-8')
    liste_dico = fichier_dico.readlines()
    mot = random.choice(liste_dico)
    mot = mot.replace('\n', '')

    #remplacement des accents
    special_char = ["eéèëê", "uùüû", "oôö", "iîï", "aàäâ"]
    for letter in special_char:
        for accent in letter[1:]:
            if accent in mot:
                mot = mot.replace(accent, letter[0])

    #capitalisation du mot
    mot = mot.upper()
    return mot

def demander_choix():
    choix=input("Quelle lettre voulez vous essayer ? ")
    while len(choix)!=1 or not choix.isalpha():       #isalpha() envoie True si ce n'est que des lettres
        choix=input("N'entrez qu'une lettre")
    choix=choix.upper()                              #upper() mets toutes le lettres en majuscules tout mettre en majuscules
    progression=choix
    return progression


#update tirets
def initialisation_progression(mot_a_trouver):
    progression = "_"
    for i in range(len(mot_a_trouver)-1):
        progression += "_"
    return progression

def affichage_tiret(progression):
    affichage = ""
    for n in range(len(progression)):
        affichage += progression[n] + " "
    print("progression du mot: ")
    print(affichage)


#affichage dessin du pendu
#idée dessin
'''
  _____
  |    |
  |    ☠
__|__

'''
def dessin_pendu(erreur):
    if erreur == 1:
        print("_____")
    elif erreur == 2:
        print("""
  |
  |
__|__""")
    elif erreur == 3:
        print("""
  ______
  |
  |
__|__""")
    elif erreur == 4:
        print("""
  ______
  |    |
  |
__|__""")
    elif erreur == 5:
        print("""
  ______
  |    |
  |    ☠
__|__""")
    else:
        pass

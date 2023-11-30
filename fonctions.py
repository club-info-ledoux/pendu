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

def verification_lettre_deja_utilise(lettre_choisie, proposition):
    for a in range(len(lettre_choisie)):
        if proposition[a] == lettre_choisie:
            return False
        else:
            return True

#update tirets
def initialisation_progression(mot_a_trouver):
    progression = "_"
    for i in range(len(mot_a_trouver)-1):
        progression += "_"
    return list(progression)

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
        print("test")

def verification(mot_a_trouver, lettre_choisie, erreur):
    lettres_bonnes = []
    for i in range(len(mot_a_trouver)):
        if lettre_choisie == mot_a_trouver[i]:
            lettres_bonnes.append(i)
    if lettres_bonnes == []:
        erreur += 1
        return None, erreur
    return lettres_bonnes, erreur

def update_progression(lettre,mot,progression, erreur):
    positions_lettre, erreur = verification(mot,lettre,erreur)
    if positions_lettre:
        for pos in positions_lettre:
            progression[pos] = lettre
    return progression,erreur
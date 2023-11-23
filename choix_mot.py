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
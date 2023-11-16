import random

def choisir_mot():
    special_char = ["éèëê", "ùüû", "ôö", "îï", "àäâ"]
    fichier_dico = open("dico.txt", 'r')
    liste_dico = fichier_dico.readlines()
    mot = random.choice(liste_dico)
    mot = mot.replace('\n', '')
    for letter in special_char:
        pass
    mot = mot.upper()
    return mot

print(choisir_mot())

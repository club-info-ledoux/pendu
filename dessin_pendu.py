# Créé par elias.kuhm, le 16/11/2023 en Python 3.7

#creation d'un pendu en équipe
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

'''
test
'''
for i in range(1,5,1):
    dessin_pendu(i)
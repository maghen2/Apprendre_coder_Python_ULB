# Exercice UpyLab 7.5 - Parcours : rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier - Jacky Trinh
# Puissance 4 est un jeu de stratégie combinatoire abstrait dont le but est d’aligner une suite de quatre pions de même couleur sur une grille comptant six rangées et sept colonnes.

# Chaque joueur possède vingt-et-un pions d’une couleur (jaune ou rouge). À chaque tour, le joueur suivant doit placer un pion dans la colonne de son choix. Le pion tombe dans la position la plus basse possible.

# Le vainqueur est le premier qui a réussi à aligner horizontalement, verticalement ou diagonalement, de manière consécutive, quatre de ses pions.

# Écrire une fonction gagnant(grille) où grille est la grille de jeu sous forme de matrice.

# Cette matrice contient donc six listes de lignes contenant chacune sept éléments.

# La ligne à l’indice 0 représente le bas du jeu.

# Les éléments de cette matrice seront soit 'R', soit 'J' ou soit 'V' pour un emplacement encore vide.

# Cette fonction renverra 'R' si le joueur à la couleur rouge a gagné, 'J' si le joueur à la couleur jaune a gagné ou bien None si aucun joueur n’a gagné.

# Attention : à la fin de l'exécution de la fonction, la grille ne doit pas avoir été modifiée. 

# Exemple 1
# L’appel suivant de la fonction :

# gagnant([['V', 'V', 'V', 'J', 'R', 'R', 'J'],
#          ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
#          ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
#          ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
#          ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#          ['V', 'V', 'V', 'V', 'V', 'V', 'V']])
# doit retourner :

# 'J'
# Exemple 2
# L’appel suivant de la fonction :

# gagnant([['V', 'R', 'J', 'J', 'J', 'R', 'V'],
#          ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#          ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#          ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#          ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
#          ['V', 'V', 'V', 'V', 'V', 'V', 'V']])
# doit retourner :

# None
# Consignes
# Dans cet exercice, il vous est demandé d’écrire seulement la fonction gagnant. Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

# Vous pourrez supposer que la matrice passée à la fonction est valide, et qu’il n’y a pas à la fois une configuration gagnante pour chacune des couleurs.
def gagnant(grille):
    # Check horizontal
    for row in grille:
        for i in range(len(row) - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] != 'V':
                return row[i]
    
    # Check vertical
    for col in range(len(grille[0])):
        for i in range(len(grille) - 3):
            if grille[i][col] == grille[i+1][col] == grille[i+2][col] == grille[i+3][col] != 'V':
                return grille[i][col]
    
    # Check diagonal (top-left to bottom-right)
    for row in range(len(grille) - 3):
        for col in range(len(grille[0]) - 3):
            if grille[row][col] == grille[row+1][col+1] == grille[row+2][col+2] == grille[row+3][col+3] != 'V':
                return grille[row][col]
    
    # Check diagonal (bottom-left to top-right)
    for row in range(3, len(grille)):
        for col in range(len(grille[0]) - 3):
            if grille[row][col] == grille[row-1][col+1] == grille[row-2][col+2] == grille[row-3][col+3] != 'V':
                return grille[row][col]
    
    return None

# Test
print(gagnant([['V', 'V', 'V', 'J', 'R', 'R', 'J'],
         ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
         ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
         ['V', 'V', 'V', 'V', 'V', 'V', 'V']])) # 'J'

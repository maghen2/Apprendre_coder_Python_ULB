# Exercice UpyLab 3.18 - Parcours : vert bleu rouge
# Auteurs : Sébastien Hoarau - Thierry Massart - Isabelle Poirier
# Écrire un programme qui lit un nombre entier strictement positif n et imprime une pyramide de chiffres de hauteur n (sur n lignes complètes, c'est-à-dire toutes terminées par une fin de ligne).

# La première ligne imprime un “1” (au milieu de la pyramide).

# La ligne i commence par le chiffre i % 10 et tant que l’on n’est pas au milieu, le chiffre suivant a la valeur suivante ((i+1) % 10).

# Après le milieu de la ligne, les chiffres vont en décroissant modulo 10 (symétriquement au début de la ligne).

# Notons qu’à la dernière ligne, aucune espace n’est imprimée avant d’écrire les chiffres 0123....

n = int(input())

for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(i % 10, 0, -1):
        print(j, end="")
    for j in range(1, i % 10 + 1):
        print(j, end="")
    print()
# exo 6.18
# Avec le même tableau en 2 dimensions, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)
# Vous pouvez réutiliser la variable `size` qui a permis de construire le tableau en 2 dimensions
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

import random

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

l=[]
c=[]
rep=[]
for i in matrix:
    for z in i:
        if z<=50:
            rep.append(z)
            c.append(i.index(z))
            l.append(matrix.index(i))
        else:
            None

inf="Inférieur ou égal a 50: {}"
ligne="Ligne n°{}"
colonnes="Colonnes n°: {}"
print(inf.format(rep))
print(ligne.format(l))
print(colonnes.format(c))

# réponse 6.18


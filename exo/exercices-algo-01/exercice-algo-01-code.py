# code 1.1
# Il existe pleins d'algorithmes de tri de données plus ou moins efficaces.
# Un des algorithme le moins efficace est le tri bulle.
# Mais il a le mérite d'être « facile » à implémenter car il est très intuitif.
#
# 1. Prenez une liste de nombre.
# 2. Comparez le premier élément avec le second élément.
# 3. Si le premier élément est plus grand que le second, inversez leurs positions.
# 4. Passez à l'élément suivant et recommencez la comparaison.
# 5. Recommencez l'étape 4 jusqu'à la fin de la liste.
# 6. Si vous avez fini de parcourir la liste, recommencez depuis l'étape 2 jusqu'à ce qu'il n'y ait plus besoin d'intervertir aucun élément.
#
# « Facile », non ?
import random

#Liste RNG
randoml = []
for i in range(0,20):
    n = random.randint(1,100)
    randoml.append(n)
print(randoml)

#Fonction de tri par bulle , paramètre : list(int) , output : list(int)
def tribulle(L):
    a = True
    while a is True:
        a = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                a = True
                L[i] , L[i+1] = L[i+1] , L[i]
    return L

tribulle(randoml)
print(randoml)

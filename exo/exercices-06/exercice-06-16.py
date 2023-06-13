# exo 6.16
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16

def swap(L, pos1, pos2):
    for i, x in enumerate(L):
        if i == pos1:
            elem1 = x
        if i == pos2:
            elem2 = x
    L[pos1] = elem2
    L[pos2] = elem1
    return L

swap(my_list,0,1)
swap(my_list,2,3)
print(swap(my_list,4,5))
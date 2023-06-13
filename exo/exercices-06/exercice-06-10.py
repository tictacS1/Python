# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat
#
# ATTENTION : ne pas utiliser la fonction sum()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10

def listsum(L):
    sum= 0
    for i in L:
        sum += i
        i=i+1
    print(sum/6)

listsum(my_list)
# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat
#
# ATTENTION : ne pas utiliser la fonction sum()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42]

# réponse 6.8
def listsum(L):
    sum= 0
    for i in L:
        sum += i
        i=i+1
    print(sum)
    
listsum(my_list)


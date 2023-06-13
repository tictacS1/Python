# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat
#
# ATTENTION : ne pas utiliser la fonction sum()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42]

# réponse 6.8
def listsum(L,a,b):
    sum= 0
    for i in range(a,b+1,1):
        sum += L[i]
        sum += L[i+1]
        return sum
    
print(listsum(my_list,0,2))


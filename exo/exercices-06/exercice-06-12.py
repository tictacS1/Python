# exo 6.12
# Comptez les nombres plus petits ou égaux à 10 dans la liste et affichez le résultat
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.12
def listcount(L):
    result= 0
    for i in L:
        if i<=10:
            result += 1
    print(result)

listcount(my_list)

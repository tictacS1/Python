# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
index=0
num=[]

for u in my_list:
    num.append(len(u))

for i in my_list:
    if len(i) < max(num):
        index+=1
    elif len(i) == max(num):
        index+=1
        break
    else:
        None
index=index-1

print(index)
print(max(num))
print(my_list[5])
    

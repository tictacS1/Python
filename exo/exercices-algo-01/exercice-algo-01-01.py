# exo 1.1
# Triez la liste suivante en ordre croissant en utilisant l'algorithme du tri bulle puis affichez la liste.
#
# ATTENTION : ne pas utiliser les fonctions sorted() et list.sort()

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 1.1

for i in range(len(my_list)-1, 0, -1):
    for j in range(0, i):
        if my_list[j+1] < my_list[j]:
            temp = my_list[j+1]
            my_list[j+1] = my_list[j]
            my_list[j] = temp
print(my_list)
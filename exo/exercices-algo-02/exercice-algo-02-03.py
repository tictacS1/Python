# exo 2.3
#
# Écrivez une fonction nommé `fibonacci()` qui :
# - renvoie `0` si on lui passe `0` en paramètre
# - renvoie `1` si on lui passe `1` en paramètre
# - renvoie `None` dans les autres cas
#
# Appelez votre fonction dans une boucle qui va de `0` à `2` en
# utilisant un index et la fonction `range()`.

# réponse 2.3

def fibonacci(a:int):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return None

for i in range(0,2):
    fibonacci(i)
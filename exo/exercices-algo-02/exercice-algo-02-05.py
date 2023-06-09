# exo 2.5
#
# Reprenez votre fonction `fibonacci`.
# Puis modifiez-là de façon à ce que la somme de `fibonacci(0)` et
# `fibonacci(1)` utilise la variable `n` au lieu de valeurs
# constantes.
#
# Appelez votre fonction dans une boucle qui va de `0` à `2` en
# utilisant un index et la fonction `range()`.
#
# Indice : comment obtenir `0` quand `n == 2` ? Comment obtenir `1`
# quand `n == 2` ?

# réponse 2.5

def fibonacci(a:int):
    n=0
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        n=fibonacci(a)+fibonacci(a-1)
        print(n)
        return fibonacci(n)

for i in range(0,2):
    fibonacci(i)

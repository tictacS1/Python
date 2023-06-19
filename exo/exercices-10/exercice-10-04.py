# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur booléenne
# - renvoie True si `a` est plus grand que `b`
# - renvoie False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4
def is_greater(a:float, b:float) ->bool:
    if a>b:
        print(True)
    else:
        print(False)
    
is_greater(2.14,1.78)
is_greater(1.12,1.78)
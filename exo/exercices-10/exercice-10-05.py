# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5
def compare(a:float, b:float) ->int:
    if a>b:
        print(1)
        return 1 
    elif a<b:
        print(-1)
        return -1
    else:
        print(0)
        return 0
        
    
compare(2.12,1.3)
compare(1.3,2.32)
compare(1.1,1.1)
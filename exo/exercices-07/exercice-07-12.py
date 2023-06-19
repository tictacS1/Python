# exo 7.12
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est compris entre 2 et 9 inclus
# affichez la variable `count` après la boucle

import random

# réponse 7.12
c=0
for r in range(0,101):
    r=random.randint(1,10)
    if r in range(2,10):
        c+=1
        
print(c)

# exo 7.10
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# utilisez une variable compteur `count` pour compter le nombre de fois où `r` est plus grand ou égal à 7
# affichez la variable `count` après la boucle

import random

# réponse 7.10
c=0
for r in range(0,101):
    r=random.randint(1,10)
    if r>=7:
        c+=1
        
print(c)

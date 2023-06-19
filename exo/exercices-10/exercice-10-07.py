# exo 10.7
# Créer une fonction nommée `compute_tax()` qui :
# - prend un paramètre nommé `price` de type `float`
# - prend un paramètre nommé `tax_type` de type `int`
# - ajoute une taxe de 2,1 % à `price` si `tax_type` est égal à `1`
# - ajoute une taxe de 5,5 % à `price` si `tax_type` est égal à `2`
# - ajoute une taxe de 10 % à `price` si `tax_type` est égal à `3`
# - ajoute une taxe de 20 % à `price` si `tax_type` est égal à `4`
# - renvoie le prix initial si `tax_type` n'est pas reconnu
# Appelez la fonction et affichez le résultat avec un montant de 100 € pour chaque type de taxe
#
# Référence : [Quels sont les taux de TVA en vigueur en France et dans l'Union européenne ? | economie.gouv.fr](https://www.economie.gouv.fr/cedef/taux-tva-france-et-union-europeenne)

# réponse 10.7
def compute_tax(price:float,tax_type:int):
    a=0
    if tax_type==1:
        a=(price * 2.1) / 100
        price += a
        print(price)
        return price
    elif tax_type==2:
        a=(price * 5.5) / 100
        price += a
        print(price)
        return price
    elif tax_type==3:
        a=(price * 10) / 100
        price += a
        print(price)
        return price
    elif tax_type==4:
        a=(price * 20) / 100
        price += a
        print(price)
        return price
    else:
        print(price)
        return price

compute_tax(100, 1)
compute_tax(100, 2)
compute_tax(100, 3)
compute_tax(100, 4)
compute_tax(100, 18)

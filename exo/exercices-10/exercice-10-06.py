# exo 10.6
# La formule suivante permet de convertir des mètres en miles :
#
#       miles = meters / 1609.344
#
# La formule suivante permet de faire l'inverse :
#
#       meters = miles * 1609.344
#
# Créez une fonction nommée :
#
# - meters_to_miles() permettant de convertir des mètres en miles
# - miles_to_meters() permettant de convertir des miles en mètres
#
# Ensuite convertissez les valeurs :
#
# - 1 Km en miles
# - 10 miles en mètres
#
# Appelez les fonctions et affichez les résultats

# réponse 10.6
c = 1609.344
def meters_to_miles(a,c):
    a = a * c 
    print(a)
    return a

def miles_to_meter(b,c):
    b = b / c
    print(b)
    return b

meters_to_miles(1000,c)

miles_to_meter(10,c)
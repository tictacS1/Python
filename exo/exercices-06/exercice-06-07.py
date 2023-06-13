# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat
#
# ATTENTION : Dans l'énoncé, quand il est écrit Xème position, cela correspond à l'index X-1

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7
ba=my_list.pop(1)
lo=my_list.pop(3)
my_list.insert(1,lo)
my_list.insert(3,ba)
print(my_list)

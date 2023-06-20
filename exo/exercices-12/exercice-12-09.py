# exo 12.9
# Reprenez la classe que vous avez créé pour l'exercice 12.7 et les
# instances que vous avez créé dans l'exercice 12.8.
# Ajoutez chacune des instances de la classe `TaxIncludedProduct` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom, le prix (sans la taxe), la taxe et le prix taxe incluse de chaque produit
# Calculez :
# - la somme du prix des produits sans les taxes
# - la somme du montant des taxes
# - la somme du prix des produits taxes incluses
# Et affichez-en des arrondis à 2 chiffres après la virgule, après la boucle `for`

# réponse 12.9
class TaxIncludedProduct:
  def __init__(self, _name:str, _price:0.0, _tax:0.0):
    self._name = _name
    self._price = _price
    self._tax = _tax

  def get_name(self):
    return self._name
  
  def set_name(self, n):
    self._name=n

  def get_price(self):
    return self._price

  def set_price(self, p):
    self._price=p

  def get_(self):
    return self._tax

  def set_tax(self, t):
    self._price=t

  def get_tax_fee(self):
    print(f"Le montant de la taxe est: {(self._price * self._tax) / 100} €")
    return (self._price * self._tax) / 100

  def get_tax_included_price(self):
    f=0
    f= (self._price * self._tax) / 100
    return self._price + f

product1=TaxIncludedProduct("Dolor",31.41,20.0)
product2=TaxIncludedProduct("Sit",27.18,10.0)
product3=TaxIncludedProduct("Amet",16.18,5.5)

product=(product1,product2,product3)

total_p=0
total_t=0
total_i=0
for i in product:
    print(i._name)
    print(i._price)
    print(i._tax)
    total_p += i._price
    total_t += i._tax
    total_i += i.get_tax_included_price()
  
print(f"Somme du prix des produits: {total_p:.2f}")
print(f"Somme des taxes sur les produits: {total_t:.2f}")
print(f"Somme du prix des taxes incluses sur les produits: {total_i:.2f}")

#ez
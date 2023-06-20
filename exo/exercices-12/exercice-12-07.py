# exo 12.7
# Créez une classe nommée `TaxIncludedProduct` qui possède les attributs suivants :
# - _name: valeur str transmise par le constructeur
# - _price: valeur float par défaut 0.0
# - _tax: valeur float par défaut 0.0
# et les méthodes suivantes :
# - __init__(name, price, tax) : le constructeur
# - get_name() : renvoie le nom du produit
# - set_name() : détermine le nom du produit
# - get_price() : renvoie le prix du produit
# - set_price() : détermine le prix du produit
# - get_tax() : renvoie la taxe en pourcentage
# - set_tax() :  détermine la taxe en pourcentage (pour une taxe de 20 %, le paramètre doit être 20.0)
# - get_tax_fee() : cette méthode calcule le montant de la taxe et le renvoie ; par exmeple pour un produit de 100 € et une taxe de 20 %, le résultat est 20.0
# - get_tax_included_price() : cette méthode calcule le prix taxe incluse et le renvoie ; par exemple pour un produit de 100 € et une taxe de 20 %, le résultat est 120.0

# réponse 12.7
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
    self._price

  def get_tax_fee(self):
    print(f"Le montant de la taxe est: {(self._price * self._tax) / 100} €")

  def get_tax_included_price(self):
    f=0
    f= (self._price * self._tax) / 100
    f= self._price + f
    print(f"Le montant du prix taxe incluse est: {f} €")

u1=TaxIncludedProduct("Malk",100,20)

u1.get_tax_fee()
u1.get_tax_included_price()
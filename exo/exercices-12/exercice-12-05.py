# exo 12.5
# Reprenez la classe que vous avez créé pour l'exercice 12.4.
# Créez 3 instances de la classe `TaxFreeProduct` et affectez les valeurs suivantes à ses attributs en utilisant les setters :
# - product1
#   - name: Foo
#   - price: 31,41
# - product2
#   - name: Bar
#   - price: 27,18
# - product3
#   - name: Baz
#   - price: 16,18

# réponse 12.5
class TaxFreeProduct:
  def __init__(self, _name:str, _price:0.0):
    self._name = _name
    self._price = _price

  def get_name(self):
    return self._name
  
  def set_name(self, n):
    self._name=n

  def get_price(self):
    return self._price

  def set_price(self, p):
    self._price=p

product1=TaxFreeProduct("",0.0)
product2=TaxFreeProduct("",0.0)
product3=TaxFreeProduct("",0.0)
  
product1.set_name("Foo")
product2.set_name("Bar")
product3.set_name("Baz")
product1.set_price(31.41)
product2.set_price(27.18)
product3.set_price(16.18)

print(product1._name)
print(product1._price)
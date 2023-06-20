# exo 12.8
# Reprenez la classe que vous avez créé pour l'exercice 12.7.
# Créez 3 instances de la classe `TaxIncludedProduct` et affectez les valeurs suivantes à ses attributs en utilisant le constructeur :
# - product1
#   - name: Dolor
#   - price: 31,41
#   - tax: 20,0
# - product2
#   - name: Sit
#   - price: 27,18
#   - tax: 10,0
# - product3
#   - name: Amet
#   - price: 16,18
#   - tax: 5,5

# réponse 12.8
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

product1=TaxIncludedProduct("Dolor",31.41,20.0)
product2=TaxIncludedProduct("Sit",27.18,10.0)
product3=TaxIncludedProduct("Amet",16.18,5.5)

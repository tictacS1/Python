# exo 12.1
# Créez une classe nommée `User` qui possède les attributs suivants :
# - firstname: valeur par défaut ''
# - lastname: valeur par défaut ''
# - email: valeur par défaut ''
# - newsletter: valeur par défaut False
# et la méthode suivante :
# - __init__() : le constructeur
# Pas la peine de créer de getters et de setters

# réponse 12.1
class User:
  def __init__(self, name, lastname, email, newsletter:False):
    self.name = name
    self.lastname = lastname
    self.email = email
    self.newsletter = newsletter

u1 = User("Malick","Gondy","blablu@gmail.com",True)
print(u1.name)
print(u1.lastname)
print(u1.email)
print(u1.newsletter)
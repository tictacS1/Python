# exo 12.3
# Reprenez la classe que vous avez créé pour l'exercice 12.1 et les
# instances que vous avez créé dans l'exercice 12.2.
# Ajoutez chacune des instances de la classe `User` à une liste nommée `users`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom complet et l'email de chaque utilisateur s'il est abonné à la newsletter (c-à-d si newsletter == True)

# réponse 12.3
class User:
  def __init__(self, name, lastname, email, newsletter:False):
    self.name = name
    self.lastname = lastname
    self.email = email
    self.newsletter = newsletter

user1=User("Joe","Dalton","joe.dalton@example.com",True)
user2=User("William","Dalton","william.dalton@example.com",False)
user3=User("Jack","Dalton","jack.dalton@example.com",False)
user4=User("Avrel","Dalton","Avrel.dalton@example.com",True)

users=[user1,user2,user3,user4]
for i in users:
    if users[3]==True:
       print(users[0].name)
       print(users[1].name)
       print(users[2].name)
    else:
       None
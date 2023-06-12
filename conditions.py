import random

if True:
    print("cool")

if False:
    print("pas cool")

number1 = random.randint(0,10)
number2 = random.randint(0,10)
print(number2)
print(number1)

if number1 < number2:
    print("win n°2")
else:
    print("win n°1")

#imbriquation du if
if number1 < number2:
    print("win n°2")
else:
    if number1 > number2:
        print("win n°1")
    else:
        print("draw")

#opérateurs booléens
#SE RAPPELER DES TABLES DE VERITE POUR LES OPERATEURS


print(not True)  #grace a not devient False False
print(False)

print(True or True) #OU Logique
print(True or False)
print(False or True)
print(False or False)

#A      B       A or B
#True   True    True
#True   True    True
#False  False   False
#False  False   False

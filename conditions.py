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

print(True or True) #OR Logique
print(True or False)
print(False or True)
print(False or False)

#A      B       A or B   Table de vérité de OR
#True   True    True
#True   True    True
#False  False   False
#False  False   False

#Opérateur NAND (not and)

#OU Exclusif
cash=bool(random.randint(0,1))
cb=bool(random.randint(0,1))

if cb or cash:
    print('Je possède de la maille')
else:
    print('il faut des sous')

if not cb and not cash:
    print("broke")
else:
    print("rich")

#Combinaison de AND et OR
lvle=2
score=143
credit=0

if lvle >= 3 and score>=100 or credit>=10:
    print('le joueur peut acheter')
else:
    print('ur broke !')

#Carte de réduction
age = random.randint(0,90)

# age>=0 IMPORTANT SI INT NEGATIF
if age>=0 and age<=11:
    print('Gratuit')
elif 26<= age <=64:
    print('10%')
else:
    print('50%')

lvl=3
xp=90
social=0




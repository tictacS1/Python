import random

#While est un if répété en boucle
#Ctrl+C pour arrêter le programme

#while True:
    #print("ce message n'est pas la")

dice = random.randint(1,6)

while dice!=6:
    print("je n'ai pas tiré un 6")
    print("Je recommence un tirage")
    dice = random.randint(1,6)
else:
    print("J'ai eu le 6")

#break permet de finir l'itération
#Continue permet de reprendre au début de la boucle suivante
#while True:
    #continue   
    #print("affiché en boucle")
    #break

#boucle for classique (voir js) avec un while
i=0
while i<10:
    print(f'{i=}')
    i+=1
#boucle for classique (voir js) avec un while
i=0
while i<10:
    print(f'{i=}')
    i+=1

#Boucle for classique en python
#0 Inclu mais 10 Exclu
for i in range(0, 10):
    print(f'{i=}')

#Boucle foreach
users=['foo','bar','baz']

for user in users:
    print(user)

#Enumerate permet de recup l'index de chaque element
for i in enumerate(users):
    print(i)
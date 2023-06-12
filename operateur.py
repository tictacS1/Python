import random

#arithmétique
a= 42 + 123
#etc ...

#Division int
b=10 // 2

#Modulo reste de la division
d= 10 % 2

#puissances
c= 2**3

#opérateurs de comparaison
print(123 == 123) # 123 egal a 123 ? on peut stocker dans une var aussi
print(123 > 40) # Strictement plus grand que
print(42>=42) # Plus grand ou egal
print(2<6789) #Plus potit que
print(5 != 34) # different de ue

#Pour js "===" pour la comparaison d'identité

#incrementation
b=1
b=2
b+=1
b+=1
print(b)

#decrementation
c= 3
c = c -1
c-= 1
print(c)

#multiplication
d = 3
d = d * 2
d *= 2
print(d)

#division
e= 10
e= e / 3
e /= 3
print(e)

#division entière
f= 10
f= f//3
f //= 3
print(f)

#opérateur in 'inclusion"
text1 = "Lorem ipsum"
result="e" in text1
print(result)  #ou print("e" in text1)

#opérateur d'inclusion + Liste
list1 = ["Lorem","ipsum"]
print("Lorem" in list1)

#comparaison avec des nombres aléatoires
g= random.randint(0,100)
h= random.randint(0,100)
print(g)
print(h)
result1= e==f
print(result1)

#expression
# 1 + 1 -> 2
# (100 + 2) * 3 -> 102 * 3 -> 306
# 1 + 1 > (100+2)*3
#random.randint(0,100) -> 100

#pas une expression
#print(100)

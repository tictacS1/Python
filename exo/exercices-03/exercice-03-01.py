# exo 3.1
# Alice est née le 10 février 1988.
# Quelle âge a-t-elle cette année ?
# Ne tenez pas compte du mois, on va partir du principe qu'on est après le 10 février pour ne pas se compliquer la vie.
# Stockez l'année en cours dans une variable nommée `year`.
# Calculez l'âge d'Alice en utilisant les variables `birthyear` et `year` puis stockez le résultat dans une variable nommée `age` et affichez ce résultat.


# réponse 3.1

# def age_alice(bir,d):
#    if (d == 2023):
#        print(d-bir)
#    else:
#        age_alice(bir,d + 1)

#print(age_alice(2003,2004))
#print(age_alice(1988,1989))

birthyear=1988
year=2023
age=year-birthyear
print(age)
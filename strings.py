text1="lorem"
text2="ipsum"
#Concaténation
text3=f"{text1} {text2}"
print(text3)
#interpolation avec une f-string
text3=f"citation : {text1} {text2}, César"
print(text3)

#Concaténation fonctionne qu'avec des str SOLUTION Convertir en str
mails=52
text4= "Vous avez" + str(mails) + "non lus"
print(text4)

#Répétiton de texte
text5="foo" * 3
print(text5)

#affichage de valeurs arrondies
number1 = 10/3
text6=f"10/3 est a peu près {number1:.2f}"

#Fonctions string
text7="abc"
print(len(text7))

#Documenter une fonction

def ouinon(v):
    """Cette fonction renvoie:
    -oui si le parametre est True
    -non si le parametre est False
    -none dans les autres cas
    value bool valeur transformée en Oui/non
    return str
    """
    if v==True:
        return "Oui"
    elif v==False:
        return "Non"
    
    return None

#!! 
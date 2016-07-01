import pprint

string = 'Salut les copains !!!!!'
compteur = {}

for lettre in string.upper():
    compteur.setdefault(lettre,0)
    compteur[lettre] += 1

a=pprint.pformat(compteur)
print(a)

    

    










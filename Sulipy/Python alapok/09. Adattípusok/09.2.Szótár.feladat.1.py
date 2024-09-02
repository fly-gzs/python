'''
Írj egy programot, amely a felhasználótól bekéri egy kutya nevét, életkorát, fajtáját,
és azt hogy rendelkezik-e érvényes oltással veszettség ellen!
Az adatokat tárolja a program szótárban, és írja ki a képernyőre az adatszerkezetet!
'''

eb = {}

nev = input('Mi a kutyád neve? ')
kor = input('Életkora? ')
fajta = input('Fajtája? ')
oltas = input('Rendelkezik érvényes veszettség elleni oltással? ')

eb['Név'] = nev
eb['Életkor'] = kor
eb['Fajta'] = fajta
eb['Oltás'] = oltas

print(eb)
print('--------------------')
for kulcs in eb:
    print(kulcs, eb[kulcs])
print('--------------------')
for ertek in eb.values():
    print(ertek)
print('--------------------')
for kulcs, ertek in eb.items():
    print(f"{kulcs}: {ertek}")

'''
Írj egy programot, amely szótárban tárolja egy macska nevét, korát.
A felhasználónak legyen lehetősége megváltoztatni az egyik tárolt adatot.
A program írja ki a felhasználó választása alapján az egyik adatot,
kérdezze meg, mire módosítsa, végül írja ki a képernyőre a frissített adatszerkezetet!
'''

cica = {}

nev = input('Mi a macskád neve? ')
kor = input('Életkora? ')

cica['Név'] = nev
cica['Életkor'] = kor
print('--------------------------')
for kulcs, ertek in cica.items():
    print(f"{kulcs}: {ertek}")
print('--------------------------')

adat = ''
while adat != 'Név' and adat != 'Életkor':
    adat = input('Melyik adatot szeretnéd módosítani? (Név/Életkor) ')
    print('--------------------------')
    if adat == 'Név':
        print(f'A cica neve: {cica[adat]}')
        uj_nev = input('Add meg az új nevet! ')
        cica['Név'] = uj_nev
    elif adat == 'Életkor':
        print(f'A cica életkora: {cica[adat]}')
        uj_kor = input('Add meg az új életkort! ')
        cica['Életkor'] = uj_kor
    else:
        print('Hibás adatbevitel')

print('--------------------------')
print('A cica frissített adatai:')
for kulcs, ertek in cica.items():
        print(f"{kulcs}: {ertek}")
'''
Írj egy programot, amely szótárban tárol adatokat
(legalább egy int, str, és bool típusút).
A program a írja ki a képernyőre az adatszerkezet!
A felhasználónak legyen lehetősége ezt az adatszerkezetet
egy kulcs-érték párral bővítenie.
A program végül írja ki a képernyőre a frissített adatszerkezetet!
'''
diak = {
    'Név': 'Enci',
    'Születési idő': '2017.06.14',
#     'Életkor': 7,
#     'Iskola': 'Szent Mór',
#     'Néptánc': True,
#     'Balett': True,
#     'Foci': False
}
for kulcs in diak:
    print(f'{kulcs}: {diak[kulcs]}')
print('--------------------------')

ertek = 'igen'
adat = 'i'    
while adat == 'i':
    adat = input('Szeretnél új adatot megadni? (i/n) ')
    print('--------------------------')
    if adat == 'i':
        kulcs = input('Add meg az új adatokat! ')
        ertek = input('Add meg a hozzá tartozó értéket! ')
        if ertek.isdigit():
            ertek = int(ertek)
        if '.' in ertek:
            ertek = float(ertek)
        if ertek == 'nem':
            ertek = False
        if ertek == 'igen':
            ertek = True
        else:
            ertek = ertek
        diak[kulcs] = ertek
    elif adat == 'n':
        print('Adatbevitel befejezve')
        print('--------------------------')
    else:
        print('Hibás bevitel! Vége!')
        print('--------------------------')

for kulcs in diak:
    print(f'{kulcs}: {diak[kulcs]}')
print('--------------------------')
print(diak)
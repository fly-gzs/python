'''
A program generáljon 5 egész számot [0;10] intervallumon, tárolja egy halmazban.
A felhasználónak meg kell próbálni kitalálni ezeket, olyan módon, hogy megad 5 számot,
melyeket szintén halmazban tárol a gép. A program tájékoztassa a felhasználót, a következőkről:
hány darab számot talált el, és melyek ezek; hány számot nem talált el, és melyek ezek;
mely számok kerültek rögzítésre a generálás vagy a felhasználó miatt;
mely számok nem szerepeltek egyik halmazban sem!
'''
import random
szamlalo = 1
teljes_halmaz = {0,1,2,3,4,5,6,7,8,9,10}
veletlen_halmaz = set()
veletlen_lista = []
while len(veletlen_halmaz) < 5:
    random_szam = random.randint(0,10)
    veletlen_lista.append(random_szam)
    veletlen_halmaz.add(random_szam)
print(veletlen_lista)
halmaz = set()
print('Adj meg 5 db számot a [0;10] intervallumban!')
while szamlalo <= 5:
    szam = int(input(f'Add meg a(z) {szamlalo}. számot! '))
    halmaz.add(szam)
    szamlalo += 1
print('--------------------------------------')
print(f'A véletlen számok: {veletlen_halmaz}')
print(f'A felhasználó számai: {halmaz}')
print('--------------------------------------')
print(f'{len(veletlen_halmaz & halmaz)} db számot találtál el.')
print(f'Az eltalált számok: {veletlen_halmaz & halmaz}')
print('--------------------------------------')
print(f'{len(veletlen_halmaz - halmaz)} db számot nem találtál el.')
print(f'Az el nem talált számok: {veletlen_halmaz - halmaz}')
print('--------------------------------------')
print(f'{len(teljes_halmaz - veletlen_halmaz - halmaz)} db szám nem szerepel egyikben sem.')
print(f'A hiányzó számok: {teljes_halmaz - veletlen_halmaz - halmaz}')

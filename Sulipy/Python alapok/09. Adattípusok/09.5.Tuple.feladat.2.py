'''
Írj egy programot, amely a felhasználótól bekér egy RGB színkód három összetvőjét!
A program állapítsa meg és írja ki a képernyőre, hogy az adott szín tartalmaz-e zöld komponenst,
illetve melyik komponensből van a legtöbb, és melyikből a legkevesebb!
'''

r = int(input('Add meg a színkód R összetevőjét! '))
g = int(input('Add meg a színkód G összetevőjét! '))
b = int(input('Add meg a színkód B összetevőjét! '))
szinkod = (r, g, b)
print(szinkod)

if szinkod[1] == 0:
    print('A szinkód nem tartalmaz zöld összetevőt!')
else:
    print('A szinkód zöld összetevőjének értéke: ', g)

legnagyobb = szinkod[0]
for szin in szinkod:
    if szin > legnagyobb:
        legnagyobb = szin

if legnagyobb == szinkod[0]:
    print('A legnagyobb komponens a piros.')
elif legnagyobb == szinkod[1]:
    print('A legnagyobb komponens a zöld.')
else:
    print('A legnagyobb komponens a kék.')
    
legkisebb = szinkod[0]
for szin in szinkod:
    if szin < legkisebb:
        legkisebb = szin

if legkisebb == szinkod[0]:
    print('A legkisebb komponens a piros.')
elif legnagyobb == szinkod[1]:
    print('A legkisebb komponens a zöld.')
else:
    print('A legkisebb komponens a kék.')
'''
Készíts egy programot, amely a felhasználótól szavakat kér be, amíg az csupán ENTER-t nem üt!
A szavakat tárolja el a program egy listában!
Az adatbekérés befejezte után írja ki a program a lista elemeit,
a legrövidebb és a leghosszabb szót!
'''
szavak = []
while (szo := input('Adj meg egy szót! ')) != '':
    if szo == '':
        break
    else:
        szavak.append(szo)
print(f'A megadott szavak: {", ".join(szavak)}')
legrovidebb = szavak[0]
leghosszabb = szavak[0]
for szo in szavak:
    if len(szo) < len(legrovidebb):
        legrovidebb = szo
    if len(szo) > len(leghosszabb):
        leghosszabb = szo
print(f'A legrövidebb szó: {legrovidebb}')   
print(f'A leghosszabb szó: {leghosszabb}')    
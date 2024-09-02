'''
A mellékelt fájl Rilke című verset tartalmazza.
Az általad írt program olvassa be a fájl tartalmát a read() metódussal,
és adja meg a válaszokat az alábbi kérdésekre:
- hány betűt tartalmaz a vers,
- hány magánhangzót tartalmaz a vers,
- hány szó fordul elő a versben?
'''

with open('./adatok/Rilke.txt', 'r', encoding='utf-8') as forrasfajl:
    szoveg = forrasfajl.read()
    print(szoveg)
    szamlalo = 0
    szamlalo2 = 0
    for betu in szoveg:
        if betu.lower() in 'aeiouáéíóöőúüű':
#             print(betu)
            szamlalo += 1
        if betu.lower() in 'aeiouáéíóöőúüűbcdfghijklmnpqrstvxyvz':
#             print(betu)
            szamlalo2 += 1
    print('- Rainer Maria Rilke: A párduc -')
    print(f'A versben {szamlalo} db magánhangzó van')
    print(f'A versben {szamlalo2} db betű van.')
    szo = len(szoveg.split())
    print(f'A versben {szo} db szó van.')
    
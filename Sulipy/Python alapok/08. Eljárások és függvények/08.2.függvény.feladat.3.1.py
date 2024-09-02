'''
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt,
amely a paraméterként átvett listában megvizsgálja,
hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza!
A program tartalmazza a függvény hívását is!
'''

def harommal_oszthatok(*args):
    szamlalo = 0
    for szam in args:
        if szam % 3 == 0:
            szamlalo += 1
    return szamlalo
        
print(harommal_oszthatok(3, 9, 9, 1, 4, 7, 12))
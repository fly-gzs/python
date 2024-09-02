'''
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt,
amely True értékkel tér vissza, ha a paraméterként átvett listaelemek
(egész számok) között van páros, ellenkező esetben a visszatérési érték False!
A program tartalmazza a függvény hívását is!
'''

def paros_e(*args):
    ertek = False
    for szam in args:
        if szam % 2 == 0:
            ertek = True
    return ertek
        
print(paros_e(1, 9, 9))
'''
Hozz létre egy Diak nevű osztályt. Attribútumai: név, osztály, születési év.
Az egyik metódusa állíptsa meg az aktuális év és a születési év alapján a diák életkorát,
a másik metódusa pedig adjon vissza egy f-sztringet, amelyben mondatszerűen szerepelnek a diák adatai:
Szia, Kiss Péter vagyok, a 10.A osztályba járok, 16 éves vagyok.
Fejleszd tovább az előző programot úgy, hogy az osztálynak legyen osztályattribútuma, osztály- és statikus metódusa!
Fejleszd tovább az előző programot úgy, hogy az hozzon létre öt Diak-objektumot.
A nevet egy-egy vezeték és keresztneveket tartalmazó listából állítsa össze véletlenszerűen,
az osztályt és a születési évet pedig szintén véletlenszerűen generálja!
A Diak-objektumokat egy listában tárolja! A program a listát bejárva írja ki a diákadatokat a képernyőre!
'''

import datetime
import random

class Diak:
    gyerek = 0
    felnott = 0

    def __init__(self, nev, osztaly, szul_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szul_ev = szul_ev
        if datetime.datetime.now().year - self.szul_ev < 18:
            type(self).gyerek += 1
        else:
            type(self).felnott += 1

    def kor(self):
        return datetime.datetime.now().year - self.szul_ev

    def info(self):
        print(f'Szia! A nevem {self.nev}, a(z) {self.osztaly} osztályba járok és {datetime.datetime.now().year - self.szul_ev} éves vagyok.')

    @classmethod
    def tanulok_db(cls):
        return cls.gyerek + cls.felnott

    @staticmethod
    def suli_info():
       return 'A Szent Mór iskola a legjobb a világon!'


vezeteknev = ['Göndöcs', 'Somogyi', 'Polgár', 'Pintér', 'Kovács']
keresztnev = ['Enna', 'Szofi', 'Szonja', 'Nonó', 'Dani']
osztaly = ['1.A', '2.A', '2.B', 'egyetem']

diakok = []
for _ in range(5):
    teljes_nev = random.choice(vezeteknev) + ' ' + random.choice(keresztnev)
    diak = Diak(teljes_nev, random.choice(osztaly), random.randint(1992,2017))
    diakok.append(diak)

for diak in diakok:
    diak.info()
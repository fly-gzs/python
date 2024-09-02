'''
Hozz létre egy Diak nevű osztályt. Attribútumai: név, osztály, születési év.
Az egyik metódusa állíptsa meg az aktuális év és a születési év alapján a diák életkorát,
a másik metódusa pedig adjon vissza egy f-sztringet, amelyben mondatszerűen szerepelnek a diák adatai:
Szia, Kiss Péter vagyok, a 10.A osztályba járok, 16 éves vagyok.
Fejleszd tovább az előző programot úgy, hogy az osztálynak legyen osztályattribútuma, osztály- és statikus metódusa!
'''

import datetime


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
        print(f'Szia! {self.nev} vagyok, a {self.osztaly} osztályba járok, {datetime.datetime.now().year - self.szul_ev} éves vagyok.')

    @classmethod
    def tanulok_db(cls):
        return cls.gyerek + cls.felnott

    @staticmethod
    def suli_info():
       return 'A Szent Mór iskola a legjobb a világon!'

diak_01 = Diak('Enci', '2A', 2017)
diak_02 = Diak('Szofi', '2A', 2016)
diak_03 = Diak('Szonja', '4C', 2014)
diak_04 = Diak('Nonó', 'Egyetem', 1992)
diak_05 = Diak('Dani', 'Egyetem', 1996)


print(f'Az {diak_01.nev} nevű diák {diak_01.kor()} éves.')
print(f'A {diak_02.nev} nevű diák {diak_02.kor()} éves.')
print(f'A {diak_03.nev} nevű diák {diak_03.kor()} éves.')
print(f'A {diak_04.nev} nevű diák {diak_04.kor()} éves.')
print(f'A {diak_05.nev} nevű diák {diak_05.kor()} éves.')
print('---')
diak_01.info()
diak_02.info()
diak_03.info()
diak_04.info()
diak_05.info()
print('---')
print(f'Az összesen {Diak.tanulok_db()} tanuló van az iskolában. A gyermekek száma: {Diak.gyerek}. A felnőtt tanulók száma: {Diak.felnott}.')
print('---')
print(Diak.suli_info())
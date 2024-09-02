'''
Hozz létre egy Diak nevű osztályt. Attribútumai: név, osztály, születési év.
Az egyik metódusa állíptsa meg az aktuális év és a születési év alapján a diák életkorát,
a másik metódusa pedig adjon vissza egy f-sztringet, amelyben mondatszerűen szerepelnek a diák adatai:
Szia, Kiss Péter vagyok, a 10.A osztályba járok, 16 éves vagyok.
'''

import datetime


class Diak:
    def __init__(self, nev, osztaly, szul_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szul_ev = szul_ev

    def kor(self):
        return datetime.datetime.now().year - self.szul_ev

    def info(self):
        print(f'Szia! {self.nev} vagyok, a {self.osztaly} osztályba járok, {datetime.datetime.now().year - self.szul_ev} éves vagyok.')


diak_01 = Diak('Enci', '2A', 2017)
diak_02 = Diak('Szofi', '2A', 2016)
diak_03 = Diak('Szonja', '4C', 2014)

print(f'Az {diak_01.nev} nevű diák {diak_01.kor()} éves.')
print(f'A {diak_02.nev} nevű diák {diak_02.kor()} éves.')
print(f'A {diak_03.nev} nevű diák {diak_03.kor()} éves.')

diak_01.info()
diak_02.info()
diak_03.info()
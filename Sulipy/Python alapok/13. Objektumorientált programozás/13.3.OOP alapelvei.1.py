'''
Készíts egy programot, amely képes tárolni:
- a diákok nevét és osztályát,
- a tanárok nevét és szakját / szakjait,
és ezeket meg is tudja jeleníteni a képernyőn egy összefüggő mondat formájában.

Például:
Szia, a nevem Kiss Péter, és a(z) 10.A osztályba járok.
Szia, a nevem Horváth Zita, biológia-kémia szakos tanár vagyok.
Szia, a nevem Schmidt Emil, matematika szakos tanár vagyok.

Használj objektumorientált megoldást!
- Először gondold végig, milyen osztályokra lesz szükség?
- Van-e lehetőség öröklődés alkalmazása révén optimálisabb kódot írni?
'''


class Szemely():
    def __init__(self, nev):
        self.nev = nev
    def bemutatkozik(self):
        print(f'Szia! A nevem {self.nev}', end='')

class Diak(Szemely):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly = osztaly
    def bemutatkozik(self):
        super().bemutatkozik()
        print(f' és a(z) {self.osztaly} osztályba járok.')

class Tanar(Szemely):
    def __init__(self, nev, szakok):
        super().__init__(nev)
        self.szakok = szakok
    def bemutatkozik(self):
        super().bemutatkozik()
        print('', '-'.join(self.szakok), ' szakos tanár vagyok.')

diak_01 = Diak('Göndöcs Enna', '2.A')
tanar_01 = Tanar('Horváth Zita', ['biológia', 'kémia'])
tanar_02 = Tanar('Schmidt Emil', ['matematika'])

print(diak_01.nev, diak_01.osztaly)
diak_01.bemutatkozik()
tanar_01.bemutatkozik()
tanar_02.bemutatkozik()
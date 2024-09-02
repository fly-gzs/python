'''
Az 1.1 feladatban meghatározottak szerint készíts egy programot,
amely a felhasználótól egymás után bekér négyzetek oldalhosszát egészen addíg,
amíg a felhasználó 0 értéket nem ad meg!
Ezen adat alapján a program hozzon létre negyzet objektumokat,
melyeket egy listában tárol!
A program írja ki a megadott négyzetek oldalhosszát, kerületét és területét!
'''

class Negyzet:
    def __init__(self, oldal):
        self.oldal = oldal

    def terulet(self):
        return self.oldal **2
    
    def kerulet(self):
        return self.oldal * 4


negyzetek = []
a = 1
while a != 0:
    a = int(input('Add meg a négyzet oldalának hosszát: '))
    negyzet = Negyzet(a)
    if a != 0:
        negyzetek.append(negyzet)

for negyzet in negyzetek:
        print(negyzet.oldal, negyzet.kerulet(), negyzet.terulet())
  
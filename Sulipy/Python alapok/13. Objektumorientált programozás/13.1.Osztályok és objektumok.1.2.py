'''
Készíts egy programot, amelyben van egy Negyzet nevű osztály.
Attribútuma legyen az oldal hossza.
Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!
Módosítsd az előző programot úgy, hogy a metódus ne a kerület- illetve a területértékkel térjen vissza,
hanem maga gondoskodjon ezen értékek kiírásáról egy egész mondatos formában.
'''

import random
class Negyzet:
    def __init__(self, oldal):
        self.oldal = oldal

    def terulet(self):
        return self.oldal **2
    
    def kerulet(self):
        return self.oldal * 4
    
    def info(self):
        print(f'A(z) {self.oldal} egység oldalú négyzet területe {self.terulet():.2f} egység, kerülete {self.kerulet():.2f} egység.')


negyzetek = []
for _ in range(2):
    negyzet = Negyzet(random.randint(0, 10))
    negyzetek.append(negyzet)

for negyzet in negyzetek:
    negyzet.info()
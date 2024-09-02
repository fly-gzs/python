'''
Készíts egy programot, amelyben van egy Negyzet nevű osztály.
Attribútuma legyen az oldal hossza.
Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!
'''

import random
class Negyzet:
    def __init__(self, oldal):
        self.oldal = oldal

    def terulet(self):
        return self.oldal **2
    
    def kerulet(self):
        return self.oldal * 4


negyzetek = []
for _ in range(2):
    negyzet = Negyzet(random.randint(0, 10))
    negyzetek.append(negyzet)

for negyzet in negyzetek:
        print(negyzet.oldal, negyzet.kerulet(), negyzet.terulet())
  
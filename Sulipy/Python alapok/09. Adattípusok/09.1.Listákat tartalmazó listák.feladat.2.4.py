'''
Készíts egy programot, amely egy kétdimenziós listában tárol ötször három darab
véletlenszámot [-5;5] intervallumon. A program írja ki a kétdimenziós lista elemeit,
majd fésülje át a lista tartalmát és törölje belőle a negatív számokat.
Végül ismét kerüljön kiírásra lista tartalma!
'''
import random

lista = []

egy = []
ketto = []
harom = []
negy = []
ot = []

szamlalo = 0
while szamlalo < 3:
    random_szam = random.randint(-5,5)
    egy.append(random_szam)
    random_szam = random.randint(-5,5)
    ketto.append(random_szam)
    random_szam = random.randint(-5,5)
    harom.append(random_szam)
    random_szam = random.randint(-5,5)
    negy.append(random_szam)
    random_szam = random.randint(-5,5)
    ot.append(random_szam)
    szamlalo += 1

lista.append(egy)
lista.append(ketto)
lista.append(harom)
lista.append(negy)  

print(lista)
for block in lista:
    for szam in block[:]:   
        if szam < 0:
            block.remove(szam)
print(lista)

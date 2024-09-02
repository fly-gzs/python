
'''
Írj egy programot, ami 4 darab három elemű [0;25] intervallumban lévő véletlen egész számokat
tartalmazó listát generál, és ezeket a listákat egy 'tarolo' nevű listába helyezi.
A program írja ki a képernyőre a 'tarolo' nevű lista tartalmát!
'''
import random

tarolo = []

egy = []
ketto = []
harom = []
negy = []

szamlalo = 0
while szamlalo < 3:
    random_szam = random.randint(0,25)
    egy.append(random_szam)
    random_szam = random.randint(0,25)
    ketto.append(random_szam)
    random_szam = random.randint(0,25)
    harom.append(random_szam)
    random_szam = random.randint(0,25)
    negy.append(random_szam)
    szamlalo += 1

# print(egy)
# print(ketto)
# print(harom)
# print(negy)

tarolo.append(egy)
tarolo.append(ketto)
tarolo.append(harom)
tarolo.append(negy)  

print(f'A tároló lista tartalma: {tarolo}')
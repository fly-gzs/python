'''
Készíts egy programot, ami a felhasználó által megadott intervallumon
állít elő szintén a felhszanáló által megadott darab véletlen egész számot!
Ezeket a program írja ki a képernyőre emelkedő és csökkenő sorrendben!
  
'''
import random
lista = []
szamlalo = 1
x = int(input('Add meg az intervallum kezdeti elemét: '))
y = int(input('Add meg az intervallum utolsó elemét: '))
z = int(input('Hány darab véletlen számot szeretnél: '))
while szamlalo <= z:
    random_szam = random.randint(x,y)
    lista.append(random_szam)
    szamlalo += 1
novekvo = sorted(lista)
csokkeno = sorted(lista, reverse=True)
print(f'{novekvo=}')
print(f'{csokkeno=}')
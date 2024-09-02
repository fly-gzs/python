'''
Készíts egy programot, amely [1; 40] intervallumon kiírja a 3-mal osztható számokat!
'''
lista3 = []
for szam in range(1,41):
    print(szam, end=',')
    if szam % 3 == 0:
        lista3.append(szam)
print('')
print('A 3-mal osztható számok a következők:')
print(lista3)
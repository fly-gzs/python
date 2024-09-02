'''
Az adott lista elemei közül a program kiírja a "t" és "T" betűkkel kezdődőeket!
Az előző programot alakítsd át úgy, hogy a feltételeknek megfelelő szavak kerüljenek rögzítésre egy másik listában is,
és ez utóbbi listát írja ki a program a képernyőre!
'''
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
t_lista = []
for szo in szavak:
    if szo[0] == 't' or szo[0] == 'T':
        t_lista.append(szo)
print('\n'.join(t_lista))
        
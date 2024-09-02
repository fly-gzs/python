'''
Az adott lista elemei közül a program kiírja a "t" és "T" betűkkel kezdődőeket!

'''
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
t_lista = []
for szo in szavak:
    if szo[0] == 't' or szo[0] == 'T':
        print(szo)
# print('\n'.join(t_lista))
        
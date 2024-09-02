'''
A program számolja össze, hogy hány darab 'A' vagy 'a' betűvel kezdődő szó van
az adott listában (amely a 'Próbáld ki!' gombra kattintva elérhető)!
A képernyőre írja is ki a feltételnek megfelelő szavakat!
'''
szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
a_szavak = []
szamlalo = 0
for szo in szavak:
    if szo[0] == 'A' or szo[0] == 'a':
        a_szavak.append(szo)
        szamlalo += 1
print(f'A listában {szamlalo} db "A" vagy "a" betüvel kezdődő szó van:', a_szavak)
        
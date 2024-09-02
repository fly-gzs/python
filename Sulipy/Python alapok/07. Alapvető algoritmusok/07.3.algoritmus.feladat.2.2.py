'''
A program számolja össze, hogy hány darab 'E' vagy 'e' betűt tartalmazó szó van
az adott listában (amely a 'Próbáld ki!' gombra kattintva elérhető)!
A képernyőre írja is ki a feltételnek megfelelő szavakat!

'''
szavak = ['Elemér', 'Enna', 'ajtó', 'róka', 'egér']
e_szavak = []
szamlalo = 0
for szo in szavak:
    if szo[0] == 'E' or szo[0] == 'e':
        e_szavak.append(szo)
        szamlalo += 1
print(f'A listában {szamlalo} db "E" vagy "e" betüvel kezdődő szó van:', e_szavak)
        
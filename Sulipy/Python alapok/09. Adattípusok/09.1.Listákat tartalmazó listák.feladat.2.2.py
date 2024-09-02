
'''
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát,
amelynek a három listaeleme egy-egy három elemű lista!
Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '.
A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy,
hogy azok egy 3x3-as rácsot adjanak ki.
A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!
Egészítsd ki úgy a programot, hogy a felhasználó megadhasson egy koordinátát
(a bal felső rácspont koordinátája (0;0), a jobb alsó pedig (2;2)),
és ekkor a program rajzolja ki úgy a 3x3-as rácsot,
hogy a megadott koordinátán 'O ' helyett, '+ ' legyen.
'''
tarolo = []

egy = ['O ', 'O ', 'O ']
ketto = ['O ', 'O ', 'O ']
harom = ['O ', 'O ', 'O ']

tarolo.append(egy)
tarolo.append(ketto)
tarolo.append(harom)


x = int(input('Add meg az első koordinátát (0,1,2): '))
y = int(input('Add meg a második koordinátát (0,1,2): '))
tarolo[x][y] = '+ '

for elem in tarolo:
    print(' '.join(elem))


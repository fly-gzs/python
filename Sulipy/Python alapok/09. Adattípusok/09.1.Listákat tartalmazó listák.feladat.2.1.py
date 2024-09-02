
'''
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát,
amelynek a három listaeleme egy-egy három elemű lista!
Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '.
A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy,
hogy azok egy 3x3-as rácsot adjanak ki.
A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!
'''
tarolo = []

egy = ['O ', 'O ', 'O ']
ketto = ['O ', 'O ', 'O ']
harom = ['O ', 'O ', 'O ']


tarolo.append(egy)
tarolo.append(ketto)
tarolo.append(harom)


for elem in tarolo:
    print(' '.join(elem))
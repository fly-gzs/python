'''
Írj egy programot, amely a main() függvényben egy lista formájában eltárolja az
'a', 'b' és 'c' betűket!
Egy másik függvény kérjen be a felhasználótól három betűt, és ezzel írja felül a main()
függvényben létrehozott lista tartalmát.
A bekérés és felülírás mindaddig folytatódjon, amíg a felhasználó három azonos betűt
nem ad meg! (A main() függvénynek kell újra és újra meghívnia a bekérést végző és a
listát felülíró függvényt, és neki kell megvizsgálnia,
hogy a lista immár három egyforma elemet tartalmaz-e!)
'''

def bekeres():
    bekert_lista = []
    elso = input('Add meg az első betüt! ')
    bekert_lista.append(elso)
    masodik = input('Add meg az második betüt! ')
    bekert_lista.append(masodik)
    harmadik = input('Add meg az harmadik betüt! ')
    bekert_lista.append(harmadik)
    return bekert_lista

def main():
    eredeti_lista = ['a', 'b', 'c']
    print(f'Az eredeti lista: {eredeti_lista}')
    eredeti_lista = bekeres()
    if eredeti_lista[0] != eredeti_lista[1]:
        print(f'A felülírt lista: {eredeti_lista}')
        print('')
        print('Mehet újra! A befejezéshez adj meg 3 egyforma betűt!')
        main()
    if eredeti_lista[0] == eredeti_lista[1] and eredeti_lista[0] == eredeti_lista[2]:
        print('Vége!')
   
main()


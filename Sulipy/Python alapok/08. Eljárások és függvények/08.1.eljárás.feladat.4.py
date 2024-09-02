'''
Írj egy programot, amely a felhasználótól bekér 3 szót,
ezeket egy listában tárolja, és egy eljárás segítségével meghatározza,
és a képernyőre kiírja, melyik a legrövidebb szó!
'''

def szo(elso,masodik,harmadik):
    legrovidebb = lista[0]
    for szoveg in lista:
        if len(szoveg) < len(legrovidebb):
            legrovidebb = szoveg
    print(f'A legrövidebb szó: {legrovidebb}')   

lista = []
print('Adj meg három szót!')
elso = input('Add meg az első szót: ')
lista.append(elso)
masodik = input('Add meg a második szót: ')
lista.append(masodik)
harmadik = input('Add meg a harmadik szót: ')
lista.append(harmadik)
szo(elso,masodik,harmadik)




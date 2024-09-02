'''
Készíts egy programot, amely listaelemek leképezésével megvalósítja a következő funkciót:
egy szavakat tartalmazó lista elemeiből generál egy másik listát,
amelyben az eredeti szavak csupa nagybetűs formában szerepelnek!
A program írja ki az eredeti és a generált listát is a képernyőre!!
'''
kis_lista = []
nagy_lista = []
szamlalo = 1
while szamlalo <= 3:
    szo = input('Adj meg 3 kisbetüs szót: ')
    kis_lista.append(szo)
    szo = szo.upper()
    nagy_lista.append(szo)
    szamlalo += 1
print('Az eredeti lista: ', kis_lista)
print('A generált lista: ', nagy_lista)
    
    
    
# print('A megadott szó csupa nagybetűvel: ', szo.upper())
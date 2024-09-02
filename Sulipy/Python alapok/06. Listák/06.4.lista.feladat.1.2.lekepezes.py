'''
Készíts egy programot, amely listaelemek leképezésével megvalósítja a következő funkciót:
egy szavakat tartalmazó lista elemeiből generál egy másik listát,
amelyben az eredeti szavak csupa nagybetűs formában szerepelnek!
A program írja ki az eredeti és a generált listát is a képernyőre!!
'''
kis_lista = ['enci','cica','csücsi','a','aa','aaa','aaaa']
nagy_lista = [szo.upper() for szo in kis_lista]
print('Az eredeti lista: ', kis_lista)
print('A generált lista: ', nagy_lista)



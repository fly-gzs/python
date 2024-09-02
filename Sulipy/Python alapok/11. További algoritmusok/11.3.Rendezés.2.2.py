'''
Az alábbi adatokat olvassa be a program,
és tárolja el egy olyan listában, amelynek az elemei szótárak.
Ár szerint rendezve jelenítse meg az egyes árucikkek jellemzőit!
A rendezéshez lambda függvényt haszáljon!

típus;bútor;osztály;ár;raktáron
Samu;íróasztal;iroda;120;igen
Álom-5;ágy;hálószoba;210;nem
Stílus;étkező asztal;konyha;140;igen
Óriás;kanapé;szoba;320;igen
Xora;kisasztal;szoba;89;nem
Boxxx;iratszekrény;iroda;150;nem
Lux;sarokpolc;szoba;180;igen
  
'''
from pprint import pprint

lista = []
with open('./adatok/butor1.txt', 'r', encoding='ANSI') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        butor = {
            'tipus': adatok[0],
            'butor': adatok[1],
            'osztaly': adatok[2],
            'ar': int(adatok[3]),
        }
        if adatok[4] == 'igen':
            butor['raktar'] = True
        else:
            butor['raktar'] = False
        lista.append(butor)
pprint(lista, sort_dicts=False)
print('---')
lista.sort(key=lambda x: x['ar'])
pprint(lista, sort_dicts=False)
        
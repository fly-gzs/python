'''
Az alábbi sorokat másold be egy .txt kiterjesztésű fájlba!
Készíts egy programot, amely ezen forrásfájlban szereplő
adatokat beolvassa és eltárolja!
A program válogassa ki egy külön listába,
a raktáron lévő bútorokat, majd jelenítse meg a lista tartalmát!

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
with open('./adatok/butor.txt', 'r', encoding='ANSI') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        if adatok[4] == 'igen':
            lista.append(adatok)
pprint(lista)
        
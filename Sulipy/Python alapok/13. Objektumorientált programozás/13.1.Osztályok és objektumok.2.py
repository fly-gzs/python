'''
Készíts egy programot, amely objektumorientált módon tartja nyilván kutyák adatait
(név, életkor, nem)! A nevét a felhasználó adja meg, az életkorát és
a nemét véletlenszerűen határozza meg a program!
Befejezésként a program a képernyőre írja ki a megadott kutyák adatait!
'''

import random
class Kutya:
    def __init__(self, nev, kor, nem):
        self.nev = nev
        self.kor = kor
        self.nem = nem

kutyak = []
nemek = ['kan', 'nőstény']
a = 'x'
while a != '':
    a = input('Add meg a kutya nevét: ')
    b = random.randint(1,20)
    c = random.choice(nemek)
    if a != '':
        kutya = Kutya(a, b, c)
        kutyak.append(kutya)

for kutya in kutyak:
    print(kutya.nev, kutya.kor, kutya.nem)
  
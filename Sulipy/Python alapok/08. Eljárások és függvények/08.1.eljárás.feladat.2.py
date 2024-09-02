'''
Írj eljárást, amely paraméterül kapott számról eldönti,
és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
'''

def szam(x):
    if x > 0:
        print('Ez a szám pozitív')
    elif x < 0:
        print('Ez a szám negatív')
    else:
        print('Ez a szám nulla')
    

szam(0)




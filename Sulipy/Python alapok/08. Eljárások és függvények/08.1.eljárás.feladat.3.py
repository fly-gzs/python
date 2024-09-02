'''
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít,
és a képernyőre kiírja, melyik a nagyobb szám!
Kezeld azt az esetet is, ha a két szám egyenlő!
'''

def szam(x,y):
    if x > y:
        print(f'Az {x} nagyobb mint {y}')
    elif x < y:
        print(f'Az {x} kisebb mint {y}')
    else:
        print(f'Az {x} egyenlő {y}-vel')
    

szam(9,1)




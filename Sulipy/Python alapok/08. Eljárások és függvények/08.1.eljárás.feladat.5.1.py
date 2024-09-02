'''
A "Próbáld ki!" gombra kattintva elérhető egy program, 
ami egy eljárás segítségével kirajzol a képernyőre egy 6x3-as mezőt. 
Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak 
megfelelően a program az adott pozícióba 'O' helyett '+' jelet írjon ki. 
A lenti példában az eljárás hivása: mezot_rajzol(0,4)
'''


def mezot_rajzol(a,b):
    for sor in range(3):
        for oszlop in range(6):
            if sor == a and oszlop == b:
                print('+ ', end='')
            else:
                print('O ', end='')
        print()
        
mezot_rajzol(0,4)


'''
Készíts egy programot, amely egymásba ágyazott ciklusok segítségével rajzolja ki
egy 5 x 5-ös mezőben az alábbi alakzatot!
'''

sor = 1
while sor <=5:
    oszlop = 1
    while oszlop <= 5:
#         print(f'({sor + oszlop:2}) ', end='')
        print(f'({sor};{oszlop}) ', end='')
        if sor - oszlop == 0:
            print('O ', end='')
        elif sor + oszlop == 6:
            print('O ', end='')
        else:
            print('. ', end='')
        oszlop += 1
    print('')
    sor += 1

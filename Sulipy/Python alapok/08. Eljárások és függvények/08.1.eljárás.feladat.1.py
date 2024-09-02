'''
Írj eljárást, amely egy tetszőleges szöveget, ill. alakzatot ír ki a képernyőre!
'''

def koszont(nev):
    print('Szia '+ nev +', puszi!')

koszont('Encike')

def mezot_rajzol(a,b):
    for sor in range(3):
        for oszlop in range(6):
            if sor == a and oszlop == b:
                print('+ ', end='')
            else:
                print('O ', end='')
        print()
        
mezot_rajzol(0,4)


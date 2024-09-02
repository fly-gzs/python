'''
A program tároljon egy listában színeket.
Kérjen be a felhasználótól egy színt, és állapítsa meg,
hogy a megadott szín már szerepel-e az adott listában.
A vizsgálat eredményéről tájékoztassa a program a felhasználót,
és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást,
hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában!
Ha a megadott szín nincs még tárolva, továbbra is a
"A megadott szín nem szerepel a listában." szöveg jelenjen meg!
'''

szinlista = ['zöld','piros','fekete','sárga','kék','zöld']
print(szinlista)
szin = input('Adj meg egy színt:\t')
if szin in szinlista:
    print('Eltaláltad! A ' + szin + ' szín szerepel a listában.')
else:
    print('Nem találtad el! A ' + szin + ' szín nem szerepel a listában.')
print('Az általad megadott ' + szin + ' szín ' + str(szinlista.count(szin)) + ' alkalommal szerepel a listában.')
print('A lista színei: ',', '.join(szinlista))
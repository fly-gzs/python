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
Egészítsük ki az előbbi programot úgy, hogy a kiértékelést követően a felhasználó által megadott szín
kerüljön felvételre a listába, és csak ezután történjen meg a lista tartalmának kiírása!
'''

szinlista = ['zöld','piros','fekete','sárga','kék','zöld']
szinlista_uj = szinlista.copy()
# print(szinlista)
szin = input('Adj meg egy színt:\t')
if szin in szinlista:
    print('Eltaláltad! Az általad megadott ' + szin + ' szín ' + str(szinlista.count(szin)) + ' alkalommal szerepel a listában.')
else:
    print('Nem találtad el! A ' + szin + ' szín nem szerepel az eredeti listában.')
szinlista_uj.append(szin)  
print('Az eredeti lista színei: ',', '.join(szinlista))
print('Az új lista színei: ',', '.join(szinlista_uj))

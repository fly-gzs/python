'''
Írj egy programot, amely a fenti listából kiszűri az 'l' betűt tartalmazó szavakat 
kétféleképpen: filter() + lambda függvény és list comprehension segítségével is!
'''


szavak = ['alma', 'ló', 'padló', 'citrom', 'kávé', 'nyugalom']   
  
print(list(filter(lambda szo: szo.count('l'), szavak)))
print([szo for szo in szavak for betu in szo if betu == 'l'])  

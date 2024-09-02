'''
Írj egy programot, amely a fenti listában tárolt azonosítókat írja ki a képernyőre a
számok sorrendjének megfelelően!
'''


azonositok = ['id10', 'id100', 'id23', 'id2', 'id13', 'id1', 'id19']    
  
print(sorted(azonositok, key=lambda szo: int(szo[2:5])))

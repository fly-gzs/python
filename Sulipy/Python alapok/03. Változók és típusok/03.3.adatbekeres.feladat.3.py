'''
Írj egy programot, ami bekér egy számot a felhasználótól,
és valamilyen matemataikai műveletek sorozataként generál
és kiír a felhasználónak egy szerencseszámot!
'''
szam=int(input("Adj meg egy számot: "))
szerencse=(szam+2)*3/5
# szerencse=round(szerencse,0)
szerencse=int(szerencse)
print("A te szerencseszámod:", szerencse)
'''
Készíts egy programot, amely sztringeket tartalmazó listaelemek leképezését valósítja meg.
A leképezéshez a sztringek metódusait ezen az oldalon bemutató listából válassz egyet!
A program írja ki az eredeti és a generált listát is a képernyőre!
'''

lista = ['enci','cica','csücsi']
lista_cap = []
print(lista)
for szo in lista:
    szo = szo.capitalize()
    lista_cap.append(szo)
print(lista_cap)

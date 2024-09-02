'''
Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban.
A bekérés akkor fejeződjön be, amikor a felhasználó intervallumon kívüli értéket ad meg!
A program írja ki a megadott intervallumba eső számokat és az összegüket!
'''

lista = []
osszeg = 0
szam = 0
# szam = int(input('Adj meg egész számokat [-5;5] intervallumban: '))
while -5 <= szam <= 5:
    szam = int(input('Adj meg egész számokat [-5;5] intervallumban: '))
    if szam <= 5:
        lista.append(szam)
print(lista)
for szam in lista:
    osszeg = osszeg + szam
print('A megadott számok összege:', osszeg)
    
    
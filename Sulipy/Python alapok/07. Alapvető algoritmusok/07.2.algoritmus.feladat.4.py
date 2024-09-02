'''
A program kérjen be egy szöveget!
Határozza meg és írja ki a képernyőre, hogy
- az adott szövegben volt-e,
- ha igen akkor hány darab,
- és hányadik helyen / helyeken (a legelső hely az egyes számú)
”a”, ”e”, ”i” , ”o” vagy ”u” magánhangzó!
Mindegyik magánhangzóra külön-külön adja meg az információkat!
'''

maganhangzok = ["a","e","i","o","u"]
szoveg = input('Adj meg egy teszőleges szöveget! ')
for mgh in maganhangzok:
    szamlalo = 0
    sorszam = []
    for index, karakter in enumerate(szoveg):
        if mgh == karakter.lower():
            sorszam.append(str(index+1))
            szamlalo += 1
    if szamlalo == 0:
        print(f'A szóban nincs "{mgh}" magánhangzó!')
    else:
        print(f'A szövegben az "{mgh}" magánhangzó {szamlalo} alkalommal szerepet a(z) {"., ".join(sorszam)}. helyen/helyeken.')

            
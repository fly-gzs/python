'''
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e!
A válasz kétféle lehet: igen vagy nem.
A választól függően írjon ki üzenetet a gép!

Fejleszd tovább az első feladat programját úgy,
hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) közül ad meg egyet,
a gép kiírja: "Sajnos nem értem a válaszodat!"
'''
nap=input("Jó napod van ma? (igen/nem): ")
if (nap=="igen"):
    print("Jaj, de jó!!!")
elif (nap=="nem"):    
    print("Sebaj, holnap jobb lesz!")
else:
    print("Sajnos nem értem a válaszodat")
    print("A válasz csak kétféle lehet: igen vagy nem.")
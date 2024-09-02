'''
Írj egy programot, ami a felhasználótól bekéri először a keresztnevét,
majd a vezetéknevét. A program ezután összefűzi ezeket egy teljes_nev nevű változóba.
Végül a program a teljes nevén üdvözli a felhasználót!
'''
keresztnev=input("Add meg keresztneved: ")
vezeteknev=input("Add meg vezetékneved: ")
nev=vezeteknev + " " + keresztnev
udv="Üdvözöllek kedves " + nev + " nevű barátom!"
print(udv)
'''
A pop2023 nevű táblázat tartalmazza a világ legnépesebb városainak adatait! (forrás)

Írj egy programot, ami az alábbi szempontok alapján beolvassa, eltárolja, és megjeleníti az adatokat.
Az összes adat kerüljön eltárolásra! Az adatok objektumorientált módon legyenek tárolva. Ezt két osztály valósítsa meg! Mérlegeld alaposan, hogy a két osztáy objektumai között milyen kapcsolati viszonyt hozol létre! Ez egy kulcskérdés ebben a feladatban!
A két osztály egy külön modulban legyen, és a program tartalmazzon main() és további függvényeket!
Legyen lehetőség az összes adat képernyőre való kiíratására (soronként egy-egy város adatai)!
A felhasználó lekérhesse egy bizonyos város adatait, ha a megadott város nem szerepel az adatok között, akkor kapjon erről tájékoztatást!
A program egyértelmű utasításokat és tájékoztatást adjon a felhasználónak! A kiirás legyen áttekinthető! A lakosságszám pontos érték formájában legyen tárolva, de a megjelenítése legyen ezen példa szerinti: 13,67 millió!
Csak a fent megnevezett szempontok kötelező érvényűek, az összes többi kérdésben szabadon dönthetsz!
'''

import csv
from city import City
from city_database import CityDatabase


def load_data_from_csv(file_path):
    city_db = CityDatabase()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city = City(
                pop2023=row['Pop2023'],
                pop2022=row['Pop2022'],
                name=row['City'],
                country=row['Country'],
                continent=row['Continent'],
                growth_rate=row['growthRate'],
                rank=row['rank']
            )
            city_db.add_city(city)
    return city_db


def main():
    file_path = './adatok/pop2023.csv'
    city_db = load_data_from_csv(file_path)

    while True:
        print("\n--- Város adatbázis ---")
        print("1. Összes város adatainak megjelenítése")
        print("2. Város adatainak lekérdezése név alapján")
        print("3. Kilépés")
        choice = input("Válassz egy opciót (1/2/3): ")

        if choice == '1':
            city_db.list_all_cities()
        elif choice == '2':
            city_name = input("Add meg a város nevét: ")
            city = city_db.get_city_by_name(city_name)
            if city:
                print(city)
            else:
                print("A megadott város nem szerepel az adatbázisban.")
        elif choice == '3':
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás, próbáld újra.")


if __name__ == "__main__":
    main()

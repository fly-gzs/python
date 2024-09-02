import requests
import json

# API végpont és fejlécek beállítása a bejelentkezéshez
login_url = "http://192.168.2.150/api/v2.0.0/login"
login_headers = {
    "Content-Type": "application/json; charset=utf-8"
}

# Autentikációs adatok
login_payload = {
    "username": "api",
    "password": "1ed5697871c128ad8050309c1923fecf",
    "port": "8260",
    "version": "2.0.0"
}

# Bejelentkezés az API-ba
login_response = requests.post(login_url, headers=login_headers, data=json.dumps(login_payload))

if login_response.status_code == 200:
    token = login_response.json().get("token")
    print("Sikeres bejelentkezés! Token:", token)
else:
    print(f"Hiba történt bejelentkezéskor: {login_response.status_code} - {login_response.text}")
    token = None

# Ha sikerült a bejelentkezés, folytatjuk a mellék módosítását
if token:
    # API végpont a melléklista lekéréséhez
    update_url = f"http://192.168.2.150/api/v2.0.0/cdr/get_random?token={token}"
    update_headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    update_payload = {
        "number": "12",                         # összes mellék: "number": "all"
        "starttime": "2024-08-09 00:00:00",
        "endtime": "2024-08-09 13:59:59"
    }

    # POST kérés küldése a mellék módosításához
    update_response = requests.post(update_url, headers=update_headers, data=json.dumps(update_payload))

    # Az API válaszának kiértékelése
    if update_response.status_code == 200:
        print("A random kód sikeresen lekérve!")
        update_response = update_response.json()
        print(f"Állapot: {update_response['status']}")
        print(f"Mellékszám: {update_response['number']}")
        print(f"Lekérés kezdete: {update_response['starttime']}")
        print(f"Lekérés vége: {update_response['endtime']}")
        print(f"Random kód a webes letöltéshez: {update_response['random']}")
    else:
        print(f"Hiba történt a mellék módosításakor: {update_response.status_code} - {update_response.text}")


# A random kód lekérése után a következő url-t kell megnyitni egy bőngészőben, amely letölti a .csv fájl-t.
# A token és random kódot aktualizálni kell!
# https://192.168.2.150:8088/api/v2.0.0/cdr/download?number=12&starttime=2024-08-09%2000:00:00&endtime=2024-08-09%2023:59:59&token=556abc0f23ecb67a1bbc3b2364ea27bf&random=556abc0f23ecb67a1bbc3b2364ea27bf
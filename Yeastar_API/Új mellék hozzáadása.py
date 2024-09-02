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
    "password": "453e4dac79acb3fe87590b24e1a26dd7",
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
    # API végpont a mellék módosításához
    update_url = f"http://192.168.2.150/api/v2.0.0/extension/add?token={token}"
    update_headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    # Adatok az új mellék hozzáadásához
    update_payload = {
        "number": "99",
        "username": "99",
        "registername": "99",
        "registerpassword": "v0S*ZrB6Y3g~1-oe"
    }

    # POST kérés küldése a mellék módosításához
    update_response = requests.post(update_url, headers=update_headers, data=json.dumps(update_payload))


    # Az API válaszának kiértékelése
    if update_response.json()['status'] == 'Success':
        print(f"Az {update_payload['number']} számú mellék sikeresen hozzáadva!")
    else:
        print(f"Hiba történt a mellék hozzáadásakor!")

'''
A videóban bemutatott időjárás app-ot szabd személyre! Valósíts meg különböző funkciókat!
Például: Írja ki a program a képernyőre, hogy a következő napokban a levegő hőmérséklete pl.: 4 Celsius fok alá süllyed-e!
'''

import requests
from pprint import pprint
from datetime import datetime

API_KEY = 'ba90bdde34b41af55d498d88ad37935c'
ONE_CALL_API = 'https://api.openweathermap.org/data/2.5/onecall'
GEOCODING_API = 'http://api.openweathermap.org/geo/1.0/direct'


def get_coordinates(city):
    geo_payload = {'q': city, 'appid': API_KEY}
    geo_resp = requests.get(GEOCODING_API, params=geo_payload)
    geo_resp = geo_resp.json()[0]
    return geo_resp['lat'], geo_resp['lon']


def get_weather(lat, lon):
    weather_payload = {'lat': lat, 'lon': lon,
                       'appid': API_KEY, 'units': 'metric', 'lang': 'hu'}
    weather_resp = requests.get(ONE_CALL_API, params=weather_payload)
    print(weather_resp.url)
    weather_resp = weather_resp.json()

    return weather_resp


def main():
    varos = input('Add meg a város nevét! ')
    coordinates = get_coordinates(varos)
    weather = get_weather(coordinates[0], coordinates[1])
    current_datetime = weather['current']['dt']
    with open(f'./adatok/{varos}.txt', 'w', encoding='utf-8') as celfajl:
        print(f"Város: {varos} \n", file=celfajl)
        print(f"A lekérdezés ideje: {datetime.fromtimestamp(current_datetime)}", file=celfajl)
        print(f"Hőmérséklet: {weather['current']['temp']:.0f} °C", file=celfajl)
        print(f"Felhőzet: {weather['current']['clouds']} %, {weather['current']['weather'][0]['description']}", file=celfajl)
        print(f"UV index: {weather['current']['uvi']:.1f}", file=celfajl)
        print(f"Harmatpont: {weather['current']['dew_point']:.0f} °C", file=celfajl)
        print(f"Hőérzet: {weather['current']['feels_like']:.0f} °C", file=celfajl)
        print(f"Páratartalom: {weather['current']['humidity']} %", file=celfajl)
        print(f"Légnyomás: {weather['current']['pressure']} mBar", file=celfajl)
        print(f"Napkelte: {datetime.fromtimestamp(weather['current']['sunrise']).strftime('%H:%M')}", file=celfajl)
        print(f"Napnyugta: {datetime.fromtimestamp(weather['current']['sunset']).strftime('%H:%M')}", file=celfajl)
        print(f"Látótávolság: {weather['current']['visibility'] / 1000} km", file=celfajl)
        print(f"Szélirány: {weather['current']['wind_deg']}°", file=celfajl)
        print(f"Szélsebesség: {weather['current']['wind_speed']} km/h", file=celfajl)
    print(f"Város: {varos} \n")
    print(f"A lekérdezés ideje: {datetime.fromtimestamp(current_datetime)}")
    print(f"Hőmérséklet: {weather['current']['temp']:.0f} °C")
    print(f"Felhőzet: {weather['current']['clouds']} %, {weather['current']['weather'][0]['description']}")
    print(f"UV index: {weather['current']['uvi']:.1f}")
    print(f"Harmatpont: {weather['current']['dew_point']:.0f} °C")
    print(f"Hőérzet: {weather['current']['feels_like']:.0f} °C")
    print(f"Páratartalom: {weather['current']['humidity']} %")
    print(f"Légnyomás: {weather['current']['pressure']} mBar")
    print(f"Napkelte: {datetime.fromtimestamp(weather['current']['sunrise']).strftime('%H:%M')}")
    print(f"Napnyugta: {datetime.fromtimestamp(weather['current']['sunset']).strftime('%H:%M')}")
    print(f"Látótávolság: {weather['current']['visibility'] / 1000} km")
    print(f"Szélirány: {weather['current']['wind_deg']}°")
    print(f"Szélsebesség: {weather['current']['wind_speed']} km/h")
    min_lista = []
    for min_temp in weather['daily']:
        napi_min_temp = min_temp['temp']['min']
        min_lista.append(napi_min_temp)
    print('---')
    x = int(input('Add meg a minimális hőmérsékletet! '))
    x_alatt = []
    x_felett = []
    for index, elem in enumerate(min_lista):
        if float(elem) < x:
            x_alatt.append(str(index+1))
        else:
            x_felett.append(index + 1)
    try:
        if x_alatt[0]:
            print(f"A(z) {'., '.join(x_alatt)} napokon a minimális hőmérséklet {x} °C alá csökken")
    except:
        print(f'A következő 8 napban mindig {x} °C felett lesz a minimális hőmérsékklet!')


main()

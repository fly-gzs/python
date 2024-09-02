import datetime


class Taxi:
    uj_taxi = 0
    regi_taxi = 0

    def __init__(self, rendszam, ossz_km, kov_szerviz, szakasz_km, fogyasztas=6.0, tank_l=35,):
        self.rendszam = rendszam
        self.ossz_km = ossz_km
        self.kov_szerviz = kov_szerviz
        self.szakasz_km = szakasz_km
        self.fogyasztas = fogyasztas
        self.tank_l = tank_l
        if ossz_km < 100000:
            type(self).uj_taxi += 1
        else:
            type(self).regi_taxi += 1

    def vissza_km(self):
        return round(self.tank_l / self.fogyasztas * 100 - self.szakasz_km)

    def szerviz(self):
        return self.kov_szerviz - datetime.datetime.now().year

    @classmethod
    def flotta_db(cls):
        return cls.uj_taxi + cls.regi_taxi

    @staticmethod
    def flotta_info():
        return 'Alfa Taxi mindíg az élen!\nTelefonszám: ...'

taxi_01 = Taxi('ABC123', 160000, 2023, 300, 5.8, 37)
taxi_02 = Taxi('AAA333', 150000, 2026, 120)
print(taxi_01.szakasz_km)
print(f'A következő szervízig {taxi_01.szerviz()} év van vissza.')
print(f'A tankban lévő üzemanyag még {taxi_02.vissza_km()} kilométerre elegendő.')
print('Az új taxik száma: ', Taxi.uj_taxi)
print('A régi taxik száma: ', Taxi.regi_taxi)
print(f'{datetime.datetime.now()}')
print(Taxi.flotta_db())
print(Taxi.flotta_info())

print(type(taxi_01))
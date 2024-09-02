class CityDatabase:
    def __init__(self):
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

    def get_city_by_name(self, name):
        for city in self.cities:
            if city.name.lower() == name.lower():
                return city
        return None

    def list_all_cities(self):
        for city in self.cities:
            print(city)

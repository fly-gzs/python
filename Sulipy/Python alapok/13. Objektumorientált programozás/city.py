class City:
    def __init__(self, pop2023, pop2022, name, country, continent, growth_rate, rank):
        self.pop2023 = int(pop2023)
        self.pop2022 = int(pop2022)
        self.name = name
        self.country = country
        self.continent = continent
        self.growth_rate = float(growth_rate)
        self.rank = int(rank)

    def __str__(self):
        pop2023_million = self.pop2023 / 1_000_000
        return f"{self.name}, {self.country}, {self.continent}, {self.rank}. {pop2023_million:.2f} millió lakos, növekedési ütem: {self.growth_rate*100:.2f}%"


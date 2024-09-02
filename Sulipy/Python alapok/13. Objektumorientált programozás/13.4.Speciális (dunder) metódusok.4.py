'''
Objektumok rendezése
'''


class School:
    def __init__(self, name):
        self.name = name
        self.level = self.get_level()

    def get_level(self):
        if 'általános iskola' in self.name.lower():
            return 1
        elif 'gimnázium' in self.name.lower():
            return 2
        elif 'egyetem' in self.name.lower():
            return 3
        else:
            return 0

    def __lt__(self, other):
        return self.level < other.level

    def __le__(self, other):
        return self.level <= other.level

    def __gt__(self, other):
        return self.level > other.level

    def __ge__(self, other):
        return self.level >= other.level

    def __repr__(self):
        return self.name


names = ['Berzsenyi Gimnázium', 'Kossuth Általános Iskola', 'Szegedi Tudományegyetem']
schools = []
for name in names:
    schools.append(School(name))

print(f'{schools}')
# [Berzsenyi Gimnázium, Kossuth Általános Iskola, Szegedi Tudomány Egyetem]

schools.sort()
print(f'{schools}')
# [Kossuth Általános Iskola, Berzsenyi Gimnázium, Szegedi Tudomány Egyetem]

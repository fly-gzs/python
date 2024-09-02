'''
Objektumok egyenlősége: __eq__
'''


class Book:
    def __init__(self, title, author, edition):
        self.title = title
        self.author = author
        self.edition = edition

    # egyenlő, ha a cím és szerző egyezik
    # a kiadásnak nem kell egyeznie
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

book_01 = Book('Garabonci Gréti nagy titka', 'Wanda Coven', '1')
book_02 = Book('Garabonci Gréti varázsol', 'Wanda Coven', '1')
book_03 = Book('Garabonci Gréti nagy titka', 'Wanda Coven', '2')

print(book_01 == book_02)
print(book_01 == book_03)
print(book_01 is book_02)
print(book_01 is book_03)
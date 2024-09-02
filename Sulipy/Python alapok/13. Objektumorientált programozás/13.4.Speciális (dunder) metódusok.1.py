'''
__repr__ és __str__
'''


class Book:
    def __init__(self, title, author, edition):
        self.title = title
        self.author = author
        self.edition = edition

    def __repr__(self):
        return f"Book(author='{self.author}', title='{self.title}', edition={self.edition})"

    def __str__(self):
        return f'{self.author}: {self.title}'

book_01 = Book('Garabonci Gréti nagy titka', 'Wanda Coven', '1')

print(book_01)
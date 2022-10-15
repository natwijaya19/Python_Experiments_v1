class Books:
    def __init__(self):
        self.books = {}
        self.number = 0

    def add_book(self, book_name):
        self.number += 1
        self.books[self.number] = book_name

    def __str__(self):
        return str(self.books)


class StoreBooks:
    @staticmethod
    def save_books(file_name, books: Books):
        with open(file_name, 'w') as f:
            f.write(str(books))


if __name__ == "__main__":
    my_books = Books()
    my_books.add_book('The Lord of the Rings')
    my_books.add_book('The Hobbit')
    my_books.add_book('The Silmarillion')
    print(my_books)
    store_books = StoreBooks()
    store_books.save_books(file_name='books.txt', books=my_books)

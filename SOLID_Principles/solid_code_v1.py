class Books():
    def __init__(self):
        self.books = {}
        self.number = 0

    def add_book(self, book_name):
        self.number += 1
        self.books[self.number] = book_name

    def __str__(self):
        return str(self.books)

    def save_books(self, file_name):
        with open(file_name, 'w') as f:
            f.write(str(self))


if __name__ == "__main__":
    books = Books()
    books.add_book('The Lord of the Rings')
    books.add_book('The Hobbit')
    books.add_book('The Silmarillion')
    print(books)
    books.save_books('books.txt')


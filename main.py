class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = 'Issued' if self.is_issued else 'Available'
        return f'{self.title} by {self.author} - {status}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book added to library: {book.title} ')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_issued:
                    self.books.remove(book)
                    print(f'Book removed: {title}')
                else:
                    print(f'Cannot remove: {title} is currently issued.')
                return
        print(f'Book not found: {title}')

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_issued:
                    book.is_issued = True
                    print(f'Book issued: {title}')
                else:
                    print(f'Book already issued: {title}')
                return
        print(f'Book not found: {title}')

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_issued:
                    book.is_issued = False
                    print(f'Book returned: {title}')
                else:
                    print(f'Book was not issued: {title}')

    def display_books(self):
        if not self.books:
            print('No books in the library')
        else:
            for book in self.books:
                print(book)


def main():
    library = Library()
    book1 = Book('Carrie', 'Stephen King')
    book2 = Book('Dallas 63', 'Stephen King')
    book3 = Book('Green Mile', 'Stephen King')
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.display_books()
    library.issue_book('Carrie')
    library.display_books()
    library.issue_book('Green Mile')
    library.display_books()
    library.return_book('Carrie')
    library.display_books()
    library.remove_book('Dallas 63')
    library.display_books()


if __name__ == '__main__':
    main()

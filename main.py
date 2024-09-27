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

    def add_book(self):
        pass

    def remove_book(self):
        pass

    def issue_book(self):
        pass

    def return_book(self):
        pass

    def display_books(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()

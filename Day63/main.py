#excercise 6

# Library management sytem in python

class Library:
    def __init__(self):
        self.noBooks = 0
        self.Books = []
    
    def addBooks(self, Books):
        self.Books.append(Books)
        self.noBooks = len(self.Books)

    def details(self):
            print(f"Total number of books are {self.noBooks} & the books are")
            for book in self.Books:
                print(book)
l = Library()
b1 = l.addBooks("Book1")
b2 = l.addBooks("Book2")
b3 = l.addBooks("Book3")
l.details()
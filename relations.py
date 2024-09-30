# from faker import Faker

# faker = Faker()
from datetime import datetime


class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book: 'Book'):
        self.books.append(book)

    def get_books(self):
        return f"Libros del autor={[book.title for book in self.books]}"


class Book:
    def __init__(self, title: str, pages: int, author: Author):
        self.title = title
        self.pages = pages
        self.author = author
    
    def __str__(self) -> str:
        return f"Book(title={self.title}, pages={self.pages}, author={self.author.name})"

class Library:
    
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_books(self):
        today = datetime.now().date()
        print(f"Contenido de la bibliote al dia {today}:\n")
        for index, book in enumerate(self.books):
            print(f"Libro {index + 1}: {book}") 
    
    


author_1 = Author('Gabriel Garcia Márquez')
author_2 = Author('Pablo Neruda')

book_1 = Book('Cien años de soledad', 473, author_1)
book_2 = Book('El coronel no tiene quien le escriba', 566, author_1)

book_3 = Book('Canto General', 283, author_2)

author_1.add_book(book_1)
author_1.add_book(book_2)
author_2.add_book(book_3)

print(author_2.get_books())


print('------------------------\n')

library = Library()

library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)

library.get_books()






    







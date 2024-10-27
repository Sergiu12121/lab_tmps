# models/book.py
from abc import ABC, abstractmethod


# Abstract Product
class Book(ABC):
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    @abstractmethod
    def get_format(self):
        pass


# Concrete Product 1 - Physical Book
class PhysicalBook(Book):
    def get_format(self):
        return "Physical Copy"


# Concrete Product 2 - EBook
class EBook(Book):
    def get_format(self):
        return "E-Book"

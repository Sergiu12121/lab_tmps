# domain/book.py
from abc import ABC, abstractmethod


# Abstract Book class
class Book(ABC):
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    @abstractmethod
    def get_format(self):
        pass


# Physical Book
class PhysicalBook(Book):
    def get_format(self):
        return "Physical Copy"


# EBook
class EBook(Book):
    def get_format(self):
        return "E-Book"

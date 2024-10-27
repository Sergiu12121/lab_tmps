# services/book_prototype.py
import copy
from models.book import Book


class BookPrototype:
    def __init__(self, book: Book):
        self.book = book

    def clone(self):
        return copy.deepcopy(self.book)

from abc import ABC, abstractmethod
from domain.book import Book

# Abstract Handler
class DiscountHandler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, book: Book):
        pass

# Physical Book Discount Handler
class PhysicalBookDiscountHandler(DiscountHandler):
    def handle_request(self, book: Book):
        if book.get_format() == "Physical Copy":
            book.price *= 0.9  # 10% discount
            print(f"Discount applied to physical book '{book.title}'. New price: ${book.price:.2f}")
        if self.successor:
            self.successor.handle_request(book)

# E-Book Discount Handler
class EBookDiscountHandler(DiscountHandler):
    def handle_request(self, book: Book):
        if book.get_format() == "E-Book":
            book.price *= 0.8  # 20% discount
            print(f"Discount applied to e-book '{book.title}'. New price: ${book.price:.2f}")
        if self.successor:
            self.successor.handle_request(book)

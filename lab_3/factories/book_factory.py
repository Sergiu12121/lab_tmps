# factories/book_factory.py
from domain.book import PhysicalBook, EBook

class BookFactory:
    @staticmethod
    def create_book(book_type: str, title: str, author: str, price: float):
        if book_type == "physical":
            return PhysicalBook(title, author, price)
        elif book_type == "ebook":
            return EBook(title, author, price)
        else:
            raise ValueError("Unknown book type")

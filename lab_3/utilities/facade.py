# utilities/facade.py
from domain.inventory import Inventory
from factories.book_factory import BookFactory
from utilities.adapter import PDFBook, EPUBBook, PDFBookAdapter, EPUBBookAdapter
from utilities.discount_handler import PhysicalBookDiscountHandler, EBookDiscountHandler


class BookstoreFacade:
    def __init__(self):
        self.inventory = Inventory()

    def add_book(self, book_type, title, author, price):
        book = BookFactory.create_book(book_type, title, author, price)
        self.inventory.add_book(book)

    def generate_report(self, format_type, title, author):
        if format_type == "pdf":
            pdf_book = PDFBook(title, author)
            adapter = PDFBookAdapter(pdf_book)
            print(adapter.generate_report(pdf_book))
        elif format_type == "epub":
            epub_book = EPUBBook(title, author)
            adapter = EPUBBookAdapter(epub_book)
            print(adapter.generate_report(epub_book))

    def list_books(self):
        self.inventory.list_books()

    def apply_discounts(self):
        # Build the chain of handlers
        ebook_handler = EBookDiscountHandler()
        physical_handler = PhysicalBookDiscountHandler(successor=ebook_handler)

        # Apply discounts to inventory
        self.inventory.apply_discounts(physical_handler)

# client/interaction_handler.py
from utilities.facade import BookstoreFacade


class InteractionHandler:
    def __init__(self):
        self.facade = BookstoreFacade()

    def add_books(self):
        # Add books using the Facade
        self.facade.add_book("physical", "1984", "George Orwell", 12.99)
        self.facade.add_book("ebook", "Brave New World", "Aldous Huxley", 7.99)

    def list_books(self):
        # List books through the Facade
        self.facade.list_books()

    def generate_reports(self):
        # Generate reports using the Adapter through the Facade
        self.facade.generate_report("pdf", "1984", "George Orwell")
        self.facade.generate_report("epub", "Brave New World", "Aldous Huxley")

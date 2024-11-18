from utilities.facade import BookstoreFacade


class InteractionHandler:
    def __init__(self):
        self.facade = BookstoreFacade()

    def add_books(self):
        self.facade.add_book("physical", "1984", "George Orwell", 12.99)
        self.facade.add_book("ebook", "Brave New World", "Aldous Huxley", 7.99)

    def list_books(self):
        self.facade.list_books()

    def apply_discounts(self):
        self.facade.apply_discounts()

    def apply_discounts(self):
        # Apply discounts using the Facade
        self.facade.apply_discounts()

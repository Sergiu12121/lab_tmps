# domain/inventory.py
class Inventory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Inventory, cls).__new__(cls)
            cls._instance.books = []
        return cls._instance

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("Inventory is empty.")
        for book in self.books:
            print(
                f"{book.title} by {book.author}, Format: {book.get_format()}, Price: ${book.price}"
            )

    def apply_discounts(self, handler):
        for book in self.books:
            handler.handle_request(book)

# main.py
from services.book_factory import BookFactory
from services.inventory import Inventory
from services.book_prototype import BookPrototype

if __name__ == "__main__":
    # Create books using Factory Method
    book1 = BookFactory.create_book("physical", "1984", "George Orwell", 12.99)
    book2 = BookFactory.create_book("ebook", "Brave New World", "Aldous Huxley", 7.99)

    # Access the Singleton Inventory
    inventory = Inventory()
    inventory.add_book(book1)
    inventory.add_book(book2)

    # List the books in inventory
    print("\n--- Initial Inventory ---")
    inventory.list_books()

    # Clone an existing book using Prototype pattern
    book_prototype = BookPrototype(book1)
    book_clone = book_prototype.clone()
    inventory.add_book(book_clone)

    # List books again to include the clone
    print("\n--- Inventory After Cloning ---")
    inventory.list_books()

# main.py
from client.interaction_handler import InteractionHandler

if __name__ == "__main__":
    handler = InteractionHandler()
    handler.add_books()  # Add books to inventory
    handler.list_books()  # List books before applying discounts
    handler.apply_discounts()  # Apply discounts
    handler.list_books()  # List books after applying discounts

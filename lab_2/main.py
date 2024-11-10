# main.py
from client.interaction_handler import InteractionHandler

if __name__ == "__main__":
    handler = InteractionHandler()

    # Add books to inventory
    handler.add_books()

    # List books in the inventory
    print("\n--- Inventory ---")
    handler.list_books()

    # Generate reports for the books
    print("\n--- Generating Reports ---")
    handler.generate_reports()

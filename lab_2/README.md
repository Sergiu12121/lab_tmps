# Creational Design Patterns

## Author: Dimbitchi Sergiu

---

## Objectives:

- Understand Creational Design Patterns (CDPs);
- Choose a domain for applying CDPs (Bookstore management system);
- Implement at least three different CDPs in the chosen domain.

## Used Design Patterns:

- Singleton
- Factory Method
- Adapter
- Facade

## Implementation

- **Singleton Pattern**:

  - I used the Singleton pattern in the `Inventory` class to make sure there’s only one instance of the inventory in my bookstore system. This way, the system always has just one centralized place for storing books, which keeps things organized and avoids duplicate inventories.

  ```python
  # domain/inventory.py
  class Inventory:
      _instance = None

      def __new__(cls):
          if cls._instance is None:
              cls._instance = super(Inventory, cls).__new__(cls)
              cls._instance.books = []
          return cls._instance
  ```

- **Factory Method Pattern**:

  - The Factory Method pattern is used in the `BookFactory` class to create either a `PhysicalBook` or an `EBook`. This makes the process of adding new types of books easy, and the main code doesn’t have to know the specifics, it just asks the factory for the book type.

  ```python
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
  ```

- **Adapter Pattern**:

  - The Adapter pattern is used to convert books to different report formats, like PDF and EPUB. I created a `ReportGenerator` interface, and then `PDFBook` and `EPUBBook` classes handle the specific formats. This way, I can add more formats later without changing the main code.

  ```python
  # utilities/adapter.py
  class ReportGenerator:
      def generate_report(self, book):
          raise NotImplementedError("Subclasses should implement this method")

  class PDFBook:
      def __init__(self, title: str, author: str):
          self.title = title
          self.author = author

      def get_pdf_format(self):
          return f"PDF Format for {self.title}"
  ```

- **Facade Pattern**:

  - I used a Facade pattern to make the bookstore interface simple and clean. The `BookstoreFacade` class combines different actions, like adding books or generating reports, so that the client code just calls the facade without knowing all the details behind the scenes.

  ```python
  # utilities/facade.py
  from factories.book_factory import BookFactory
  from domain.inventory import Inventory

  class BookstoreFacade:
      def __init__(self):
          self.inventory = Inventory()
          self.factory = BookFactory()

      def add_book(self, book_type, title, author, price):
          book = self.factory.create_book(book_type, title, author, price)
          self.inventory.add_book(book)
  ```

## Conclusions / Screenshots / Results

In this project, I was able to use multiple design patterns to simplify the bookstore system and make it more modular. Each pattern solved a specific problem, like controlling the inventory instance, simplifying book creation, adapting to different report formats, and providing a straightforward interface for users.

This approach showed me how design patterns can make code more organized and easier to manage or extend, which was especially clear in the way the Facade pattern helped centralize user interactions.

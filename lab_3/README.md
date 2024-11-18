# Topic: _Behavioral Design Patterns_

## Author: _Dimbitchi Sergiu_

---

## Introduction

In software engineering, behavioral design patterns are used to identify and establish efficient communication patterns between software entities. These patterns not only streamline interactions but also improve flexibility and scalability within a system. They are essential for addressing complex business requirements that involve interaction and state management.

This laboratory work focuses on integrating one behavioral design pattern, the **Chain of Responsibility**, into a previously developed system. This pattern is particularly suited for scenarios where requests must be processed by a chain of handlers, enabling a flexible approach to task delegation.

---

## Objectives

1. Study and understand Behavioral Design Patterns.
2. Analyze communication scenarios within the existing system and identify where behavioral design patterns can be beneficial.
3. Extend the system by implementing a behavioral design pattern to enhance its functionality.

---

## Theoretical Background

### Behavioral Design Patterns

Behavioral design patterns focus on the interaction between objects, facilitating clear and maintainable communication channels.

Examples of behavioral design patterns include:

- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Observer
- Strategy

### Chain of Responsibility Pattern

The **Chain of Responsibility** is a design pattern that allows a request to pass through a chain of handlers until one of them processes it. This pattern is particularly effective for systems requiring dynamic and decoupled handling of requests.

Key benefits include:

- Decoupling sender and receiver.
- Simplifying complex if-else or switch-case logic.
- Adding or modifying handlers without altering the chain structure.

---

## Implementation & Explanation

### Motivation

In the bookstore management system, different book formats (e.g., physical and e-books) have varying discount policies. Instead of hardcoding these conditions, the Chain of Responsibility pattern was chosen to apply discounts dynamically, ensuring extensibility and maintainability.

### Project Structure

The project follows the prescribed structure:

```
client/
    interaction_handler.py
domain/
    book.py
    inventory.py
utilities/
    facade.py
    discount_handler.py
factories/
    book_factory.py
```

### Code Snippets

#### **`utilities/discount_handler.py`**

Defines the handlers for processing discounts:

```python
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
```

#### **`domain/inventory.py`**

Integrates the chain of handlers for applying discounts:

```python
class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}, Format: {book.get_format()}, Price: ${book.price:.2f}")

    def apply_discounts(self, handler):
        for book in self.books:
            handler.handle_request(book)
```

#### **`utilities/facade.py`**

Simplifies the application of discounts via the facade:

```python
from utilities.discount_handler import PhysicalBookDiscountHandler, EBookDiscountHandler

class BookstoreFacade:
    def __init__(self, inventory):
        self.inventory = inventory

    def apply_discounts(self):
        ebook_handler = EBookDiscountHandler()
        physical_handler = PhysicalBookDiscountHandler(successor=ebook_handler)
        self.inventory.apply_discounts(physical_handler)
```

#### **`client/interaction_handler.py`**

Provides a single entry point for applying discounts:

```python
from utilities.facade import BookstoreFacade
from domain.inventory import Inventory
from factories.book_factory import BookFactory

class InteractionHandler:
    def __init__(self):
        self.inventory = Inventory()
        self.facade = BookstoreFacade(self.inventory)

    def add_books(self):
        factory = BookFactory()
        self.inventory.add_book(factory.create_book("physical", "1984", "George Orwell", 12.99))
        self.inventory.add_book(factory.create_book("ebook", "Brave New World", "Aldous Huxley", 7.99))

    def list_books(self):
        self.inventory.list_books()

    def apply_discounts(self):
        self.facade.apply_discounts()
```

---

## Results

### Before Discounts

```
1984 by George Orwell, Format: Physical Copy, Price: $12.99
Brave New World by Aldous Huxley, Format: E-Book, Price: $7.99
```

### During Discount Application

```
Discount applied to physical book '1984'. New price: $11.69
Discount applied to e-book 'Brave New World'. New price: $6.39
```

### After Discounts

```
1984 by George Orwell, Format: Physical Copy, Price: $11.69
Brave New World by Aldous Huxley, Format: E-Book, Price: $6.39
```

---

## Conclusion

The implementation of the Chain of Responsibility pattern successfully decouples the logic for applying discounts from the main system workflow. It demonstrates the utility of behavioral design patterns in enhancing flexibility, maintainability, and scalability in software systems. By implementing this pattern, the system's codebase becomes more modular and easier to extend.

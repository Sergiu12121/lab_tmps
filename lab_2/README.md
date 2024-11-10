# Bookstore Inventory System - Structural Design Patterns

**Author**: [Your Name]

## Introduction
This project implements an extended version of the bookstore inventory system, incorporating three structural design patterns: **Adapter**, **Composite**, and **Facade**. These patterns streamline object interactions, making the system more flexible and scalable.

## Implementation & Explanation
1. **Adapter Pattern**: The Adapter pattern is used to adapt different book formats (e.g., PDF, EPUB) so they can be handled uniformly when generating reports.
    - Code Location: `utilities/adapter.py`

2. **Composite Pattern**: The Composite pattern allows for grouping multiple books into categories or bundles, treating them as a single object in the inventory.
    - Code Location: `domain/inventory.py`

3. **Facade Pattern**: The Facade pattern provides a simplified interface to the entire bookstore system, allowing the client to manage the inventory, book creation, and order processing without dealing with internal complexities.
    - Code Location: `utilities/facade.py`

## Results & Conclusions
- The client can now easily add books, generate reports in different formats, and interact with the system via a simplified interface.
- Screenshots or output logs can be found in the `results/` directory.

### How to Run:
```bash
python client/main.py

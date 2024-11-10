# utilities/adapter.py

# Target Interface
class ReportGenerator:
    def generate_report(self, book):
        raise NotImplementedError("Subclasses should implement this method")

# Adaptee 1 - PDF Format
class PDFBook:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_pdf_format(self):
        return f"PDF Format for {self.title}"

# Adaptee 2 - EPUB Format
class EPUBBook:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_epub_format(self):
        return f"EPUB Format for {self.title}"

# Adapter for PDFBook
class PDFBookAdapter(ReportGenerator):
    def __init__(self, pdf_book: PDFBook):
        self.pdf_book = pdf_book

    def generate_report(self, book):
        return self.pdf_book.get_pdf_format()

# Adapter for EPUBBook
class EPUBBookAdapter(ReportGenerator):
    def __init__(self, epub_book: EPUBBook):
        self.epub_book = epub_book

    def generate_report(self, book):
        return self.epub_book.get_epub_format()

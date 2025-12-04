class Book:
    def _init_(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"

    def to_dict(self):
        """Converts book object to dictionary for JSON saving."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def _str_(self):
        return f"[{self.isbn}] {self.title} by {self.author} ({self.status})"

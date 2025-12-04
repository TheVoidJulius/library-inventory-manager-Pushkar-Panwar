import json
import logging
from pathlib import Path
from .book import Book

# Configure Logging (Task 5)
logging.basicConfig(
    filename='library.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LibraryInventory:
    def _init_(self, file_path="data/library.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    def add_book(self, title, author, isbn):
        """Adds a new book and saves to file."""
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        logging.info(f"Added book: {title} ({isbn})")
        print("Book added successfully.")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return [b for b in self.books if b.isbn == isbn]

    def display_all(self):
        if not self.books:
            print("No books in inventory.")
        for book in self.books:
            print(book)

    def save_books(self):
        """Task 3: Save to JSON."""
        try:
            # Ensure directory exists
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            
            data = [book.to_dict() for book in self.books]
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            logging.error(f"Failed to save data: {e}")
            print("Error saving data.")

    def load_books(self):
        """Task 3: Load from JSON with Error Handling."""
        if not self.file_path.exists():
            logging.info("No data file found. Starting with empty inventory.")
            return

        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                # Convert dicts back to Book objects
                self.books = [Book(**item) for item in data]
            logging.info("Database loaded successfully.")
        except (json.JSONDecodeError, IOError) as e:
            logging.error(f"Error loading data: {e}")
            print("Error loading inventory file. Starting fresh.")
            self.books = []

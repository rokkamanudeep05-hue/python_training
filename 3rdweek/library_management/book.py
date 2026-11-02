from storage import load_data, save_data
from validator import validate_text, validate_id, validate_year
from exceptions import (
    BookNotFoundError,
    BookUnavailableError,
    DuplicateRecordError,   
    
)


class BookManager:
    def __init__(self):
        self.books = load_data("books.json")

    def _find_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book

        raise BookNotFoundError(
            f"Book with ID {book_id} was not found."
        )

    def add_book(self, title, author, year):
        title = validate_text(title, "Title")
        author = validate_text(author, "Author")
        year = validate_year(year)

        book_id = str(
            max(
                (int(book["id"]) for book in self.books),
                default=0,
            ) + 1
        )

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "year": year,
            "available": True,
        }

        self.books.append(book)
        self._save()

        return book

    def search_books(self, keyword):
        keyword = validate_text(keyword, "Search keyword").lower()

        return [
            book for book in self.books
            if keyword in book["title"].lower()
            or keyword in book["author"].lower()
            or keyword == book["id"]
        ]

    def update_book(self, book_id, title=None, author=None, year=None):
        book_id = validate_id(book_id, "Book ID")
        book = self._find_book(book_id)

        if title is not None:
            book["title"] = validate_text(title, "Title")

        if author is not None:
            book["author"] = validate_text(author, "Author")

        if year is not None:
            book["year"] = validate_year(year)

        self._save()
        return book

    def delete_book(self, book_id):
        book_id = validate_id(book_id, "Book ID")
        book = self._find_book(book_id)

        if not book["available"]:
            raise BookUnavailableError(
                "Cannot delete a borrowed book."
            )

        self.books.remove(book)
        self._save()

    def list_books(self):
        return self.books.copy()

    def get_book(self, book_id):
        return self._find_book(validate_id(book_id, "Book ID"))

    def _save(self):
        save_data("books.json", self.books)
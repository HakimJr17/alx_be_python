class Book:
    """
    Represents a book in the library system.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    Private Attributes:
        _is_checked_out (bool): True if the book is currently checked out, False otherwise.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False # Books are available by default

    def check_out(self):
        """
        Marks the book as checked out.
        Returns:
            bool: True if the book was successfully checked out, False otherwise (e.g., already checked out).
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        print(f"'{self.title}' is already checked out.")
        return False

    def return_book(self):
        """
        Marks the book as available (returned).
        Returns:
            bool: True if the book was successfully returned, False otherwise (e.g., not checked out).
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        print(f"'{self.title}' was not checked out.")
        return False

    def is_available(self):
        """
        Checks if the book is currently available.
        Returns:
            bool: True if available, False if checked out.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book instances.
    Private Attributes:
        _books (list): A list to store Book objects.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.
        Args:
            book (Book): The Book object to add.
        """
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.
        Args:
            title (str): The title of the book to check out.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.check_out():
                    print(f"Checked out '{title}'.")
                break
        if not found:
            print(f"Book with title '{title}' not found in the library.")

    def return_book(self, title):
        """
        Attempts to return a book by its title.
        Args:
            title (str): The title of the book to return.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.return_book():
                    print(f"Returned '{title}'.")
                break
        if not found:
            print(f"Book with title '{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books that are currently available in the library.
        If no books are available, it prints a message.
        """
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
            return

        for book in available_books:
            print(book)

# Library Management System using Object-Oriented Programming

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_book(self):
        status = "Available" if self.is_available else "Issued"
        print(f"ID: {self.book_id} | Title: {self.title} | "
              f"Author: {self.author} | Status: {status}")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display_patron(self):
        print(f"ID: {self.patron_id} | Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:", ", ".join(self.borrowed_books))
        else:
            print("Borrowed Books: None")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book added successfully!")

    # Register a new patron
    def register_patron(self):
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        self.patrons.append(patron)

        print("Patron registered successfully!")

    # Issue a book
    def issue_book(self):
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        book = None
        patron = None

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if book is None:
            print("Book not found!")
            return

        if patron is None:
            print("Patron not found!")
            return

        if not book.is_available:
            print("Book is already issued!")
            return

        book.is_available = False
        patron.borrowed_books.append(book.title)

        print("Book issued successfully!")

    # Return a book
    def return_book(self):
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        book = None
        patron = None

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if book is None:
            print("Book not found!")
            return

        if patron is None:
            print("Patron not found!")
            return

        if book.is_available:
            print("This book is already available in the library!")
            return

        book.is_available = True

        if book.title in patron.borrowed_books:
            patron.borrowed_books.remove(book.title)

        print("Book returned successfully!")

    # Display all books
    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n--- BOOK LIST ---")
        for book in self.books:
            book.display_book()

    # Display all patrons
    def display_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
            return

        print("\n--- PATRON LIST ---")
        for patron in self.patrons:
            patron.display_patron()


# Main program
library = Library()

while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add New Book")
    print("2. Register Patron")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Display All Patrons")
    print("7. Exit")
    print("===============================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.register_patron()

    elif choice == "3":
        library.issue_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_patrons()

    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
# import os
# import csv
# def file_creat():
#     file_name="libary.csv"
#     if not os.path.exists(file_name):
#         with open ("libary.csv","a",newline="") as f:
#             writer=csv.writer(f)
#             writer.writerow(["Book Title",
#                              "Author",
#                              "Book Id",
#                              "Availability Status"])


# Library Management System

class Book:

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True

    def display_book(self):
        status = "Available" if self.available else "Issued"

        print("----------------------------")
        print("Book ID   :", self.book_id)
        print("Title     :", self.title)
        print("Author    :", self.author)
        print("Status    :", status)


class Library:

    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        book_id = input("Enter Book ID: ")

        book = Book(title, author, book_id)
        self.books.append(book)

        print("Book added successfully!")

    # View All Books
    def view_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return

        for book in self.books:
            book.display_book()

    # Search Book
    def search_book(self):
        search = input("Enter Book Title or ID: ")

        found = False

        for book in self.books:

            if book.title.lower() == search.lower() or book.book_id == search:
                book.display_book()
                found = True

        if not found:
            print("Book not found.")

    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:

            if book.book_id == book_id:

                if book.available:
                    book.available = False
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")

                return

        print("Book not found.")

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:

            if book.book_id == book_id:

                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("Book is already available.")

                return

        print("Book not found.")

    # Delete Book
    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")

        for book in self.books:

            if book.book_id == book_id:

                self.books.remove(book)
                print("Book deleted successfully!")
                return

        print("Book not found.")


# Create Library Object
library = Library()


# Main Menu
while True:

    print("~~ LIBRARY MANAGEMENT SYSTEM ~~")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        print("Thank you for using Library Management System")
        break

    else:
        print("Invalid choice<Please try again>")
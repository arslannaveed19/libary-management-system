# Library Management System

A simple **Library Management System** built with **Python and Object-Oriented Programming (OOP)**.

This is a console-based application that allows users to manage books in a library. Users can add, view, search, issue, return, and delete books.

## Features

The program provides the following features:

1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Classes and Objects
* Lists
* Functions
* Loops
* Conditional Statements

## Project Structure

The project uses two main classes:

### Book Class

The `Book` class represents a single book.

Each book contains:

* Book Title
* Author
* Book ID
* Availability Status

Example:

```python
class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True
```

### Library Class

The `Library` class manages all books in the library.

It contains a list called `books` where book objects are stored.

The class provides methods for:

* Adding books
* Viewing books
* Searching books
* Issuing books
* Returning books
* Deleting books

## Book Availability

When a new book is added, its availability is automatically set to:

```text
Available
```

When a book is issued:

```text
Issued
```

When the book is returned:

```text
Available
```

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Save the Python File

Save the program as:

```text
library_management.py
```

### 3. Run the Program

Open the terminal in VS Code and run:

```bash
python library_management.py
```

## Main Menu

The program displays the following menu:

```text
~~ LIBRARY MANAGEMENT SYSTEM ~~

1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit

Enter your choice:
```

## Example

### Adding a Book

```text
Enter Book Title: Python Programming
Enter Author Name: John Smith
Enter Book ID: B101

Book added successfully!
```

### Viewing Books

```text
----------------------------
Book ID   : B101
Title     : Python Programming
Author    : John Smith
Status    : Available
```

### Issuing a Book

```text
Enter Book ID to issue: B101

Book issued successfully!
```

The status will then become:

```text
Status    : Issued
```

### Returning a Book

```text
Enter Book ID to return: B101

Book returned successfully!
```

The status changes back to:

```text
Status    : Available
```

## OOP Concepts Used

This project is designed to practice important Python OOP concepts.

### Class

Two classes are used:

```text
Book
Library
```

### Object

Objects are created from the `Book` class:

```python
book = Book(title, author, book_id)
```

An object is also created from the `Library` class:

```python
library = Library()
```

### Constructor

The `__init__()` method initializes the object:

```python
def __init__(self, title, author, book_id):
```

### Self

`self` refers to the current object and is used to access its attributes and methods.

### Methods

The project uses methods such as:

```text
add_book()
view_books()
search_book()
issue_book()
return_book()
delete_book()
```

## Learning Objectives

This project helps practice:

* Python Classes
* Objects
* Constructors
* `self`
* Methods
* Lists
* `for` loops
* `if-else` statements
* User input
* Searching data
* Adding and removing objects
* Basic library management logic

## Future Improvements

The project can be improved by adding:

* CSV file storage
* Database integration
* Student/member management
* Due dates
* Fine calculation
* Login system
* GUI interface
* FastAPI web API



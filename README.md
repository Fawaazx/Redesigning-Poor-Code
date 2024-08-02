# Library Management System

## Overview

The Library Management System (LMS) is a command-line application designed to manage a library's books, users, and checkouts. It provides functionalities for adding, updating, deleting, and searching for books and users, as well as managing book checkouts. The system is implemented using Python and follows object-oriented design principles.

## Features

1. **Book Management:**
   - Add new books
   - Update existing books
   - Delete books
   - Search for books by title, author, or ISBN
   - List all books

2. **User Management:**
   - Add new users
   - Update existing users
   - Delete users
   - Search for users by name or user ID
   - List all users

3. **Checkout Management:**
   - Checkout books to users
   - List all checkouts


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system

## Usage
1. **Run the application:**
   ```bash
   python main.py
2. Follow the prompts to manage books, users, and checkouts.


## Modules
## models.py
Defines the data models for books, users, and checkouts.

## book.py
Handles book management, including adding, updating, deleting, searching, and listing books.

## user.py
Handles user management, including adding, updating, deleting, searching, and listing users.

## check.py
Handles book checkouts, including recording and listing checkouts.

## storage.py
Handles data storage and retrieval using file-based storage (JSON format).

## main.py
Brings everything together and handles user interactions through a command-line interface.


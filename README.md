# 📚 Library Automation & Membership System

A Python-based **Library Automation & Membership System** developed using **Object-Oriented Programming (OOP)**, JSON data storage, file handling, date and time operations, exception handling, modules, and a **Streamlit graphical user interface**.

The system automates common library operations such as book registration, member registration, book searching, book issuing, book returning, due-date calculation, fine calculation, availability tracking, and borrowing history management.

---

## 📌 Project Overview

The Library Automation & Membership System is designed to manage books, library members, and borrowing transactions in an organized way.

The project is divided into separate Python modules to keep the code structured, reusable, and easy to maintain.

The system consists of:

* **Core Python modules** for business logic
* **Streamlit GUI** for user interaction
* **JSON file** for persistent data storage

The application provides functionality for managing books and members and maintaining the complete book borrowing and returning process.

---

# ✨ Features

## 📚 Book Registration

* Add new books
* Store Book ID
* Store book title
* Store author
* Store book category
* Track book availability
* Prevent duplicate Book IDs

## 🏷️ Book Categories

Books are organized using categories.

The category is stored as part of the book information and can be used during book searching.

## 👤 Member Registration

* Register new members
* Store Member ID
* Store member name
* Store phone number
* Maintain borrowed-books information
* Prevent duplicate Member IDs

## 🔍 Book Search

Books can be searched using:

* Book title
* Author
* Category
* Keyword

The search operation checks the stored book information and returns matching books.

## 📖 Book Issue

The Book Issue module allows registered members to borrow available books.

Before issuing a book, the system validates:

* Book ID
* Member ID
* Book availability
* Borrowing eligibility

After a successful issue:

* Book availability is updated
* Book ID is added to the member's borrowed-books list
* Issue date is recorded
* Due date is calculated
* Transaction information is maintained

## ↩️ Book Return

The Book Return module manages returned books.

When a book is returned:

* Return date is recorded
* Late days are calculated
* Fine is calculated when applicable
* Book availability is updated
* Book ID is removed from the member's borrowed-books list
* Borrowing history is updated

## 📅 Due Date Calculation

The system automatically calculates the due date when a book is issued.

The borrowing period is **14 days**.

The calculation uses Python's `datetime` and `timedelta` functionality.

## 💰 Fine Calculation

The system calculates a fine when a book is returned after the due date.

The fine rate is **₹5 per late day**.

The system calculates the number of late days by comparing the return date with the due date.

## 📊 Availability Tracking

Book availability is tracked using a Boolean value.

* `True` → Book is available
* `False` → Book is currently issued

The availability status is updated automatically during book issue and return operations.

## 📜 Borrowing History

The system maintains borrowing and returning history.

Each transaction stores:

* Member ID
* Book ID
* Issue Date
* Due Date
* Return Date
* Fine

---

# 🧠 Technical Concepts Used

The project demonstrates the following Python concepts:

## Lists

Lists are used to store collections of values.

They are mainly used for:

* Borrowed books
* Borrowing history
* Search results

## Dictionaries

Dictionaries are used to store data using key-value pairs.

They are used for:

* Books
* Members
* Transaction information
* JSON data

Book IDs and Member IDs are used as unique keys for efficient data access.

## Functions

Functions divide the application into smaller reusable operations.

Core functions include:

* `add_book()`
* `add_member()`
* `search_books()`
* `issue_book()`
* `return_book()`
* `load_data()`
* `save_data()`

## Classes

The project uses Object-Oriented Programming through classes.

The main classes are:

* `Book`
* `Member`
* `Library`

The `Book` class manages book-related information.

The `Member` class manages member-related information.

The `Library` class contains the main business logic.

## File Handling

File handling is used to permanently store library information.

The project uses JSON files to:

* Read existing data
* Write updated data
* Maintain persistent information

Python's `open()` function is used for reading and writing the JSON file.

## Date and Time

Python's `datetime` module is used for:

* Issue date
* Due date
* Return date
* Late-day calculation
* Fine calculation

`timedelta` is used to calculate the 14-day borrowing period.

## Exception Handling

Exception handling is used to manage unexpected errors and prevent the application from terminating unexpectedly.

It is useful while handling:

* File operations
* JSON data
* User input
* Data conversion
* Date operations

The project uses `try` and `except` blocks where required.

## Modules

The project is divided into separate Python modules.

The modules allow different responsibilities to be maintained separately and can be imported wherever required.

---

# 📂 Project Structure

```text
Library-Automation-Membership-System/
│
├── app.py
├── library.py
├── book.py
├── member.py
├── file_handler.py
│
├── library_data.json
├── requirements.txt
├── README.md
│
└── .gitignore
```

---

# 📄 Core Modules

## `book.py`

Contains the `Book` class.

Responsibilities:

* Store Book ID
* Store title
* Store author
* Store category
* Track availability
* Convert book information into dictionary format for storage

---

## `member.py`

Contains the `Member` class.

Responsibilities:

* Store Member ID
* Store member name
* Store phone number
* Maintain borrowed-books list
* Convert member information into dictionary format for storage

---

## `library.py`

Contains the `Library` class and the **core business logic** of the application.

Responsibilities:

* Book registration
* Member registration
* Book search
* Book issue
* Book return
* Due-date calculation
* Fine calculation
* Availability tracking
* Borrowing history

This is the main business-logic module of the project.

---

## `file_handler.py`

Handles JSON data storage and retrieval.

Responsibilities:

* Load library data
* Save library data
* Read JSON information
* Write updated JSON information

---

## `app.py`

Contains the **Streamlit graphical user interface**.

The GUI provides an interface for interacting with the core library functionality.

The Streamlit interface connects user actions with the business logic implemented in `library.py`.

---

# 🖥️ Streamlit GUI

The graphical interface is developed using **Streamlit**.

The GUI provides modules for:

* Dashboard
* Book Registration
* Book Categories
* Member Registration
* Book Search
* Book Issue
* Book Return
* Due Date
* Fine Calculation
* Availability Tracking
* Borrowing History

The GUI provides a user-friendly interface while the core operations are handled by the Python business-logic modules.

---

# 💾 Data Storage

The application uses **JSON** for persistent data storage.

The main data file is:

```text
library_data.json
```

The file contains three major sections:

* `books`
* `members`
* `history`

### Books

Stores information about registered books and their availability.

### Members

Stores registered member information and borrowed books.

### History

Stores book issue and return transactions.

---

# 🔄 Application Workflow

The overall application workflow is:

```text
User
  ↓
Streamlit GUI
  ↓
Library Class
  ↓
Book / Member Classes
  ↓
File Handler
  ↓
library_data.json
```

## Book Issue Workflow

```text
Book Selection
      ↓
Book Validation
      ↓
Member Validation
      ↓
Availability Check
      ↓
Due Date Calculation
      ↓
Update Book Status
      ↓
Update Member Records
      ↓
Save Data
```

## Book Return Workflow

```text
Book Selection
      ↓
Borrowing Validation
      ↓
Return Date
      ↓
Due Date Comparison
      ↓
Late Day Calculation
      ↓
Fine Calculation
      ↓
Update Book Status
      ↓
Update Member Records
      ↓
Update History
      ↓
Save Data
```

---

# 🛠️ Technologies Used

* **Python 3**
* **Object-Oriented Programming**
* **Streamlit**
* **JSON**
* **File Handling**
* **datetime**
* **Exception Handling**
* **Python Modules**
* **Git**
* **GitHub**

---

# 📦 Installation

### Install the required packages

```bash
pip install -r requirements.txt
```

The project requires Streamlit for the graphical interface.

---

# ▶️ Running the Application

The main application file is:

```text
app.py
```

Run the application using:

```bash
streamlit run app.py
```

If Streamlit is not recognized, use:

```bash
python -m streamlit run app.py
```

---

# ☁️ Streamlit Community Cloud Deployment

The project can be deployed using **Streamlit Community Cloud**.

### Deployment Requirements

* GitHub repository
* `app.py`
* `requirements.txt`
* Required Python modules
* `library_data.json`

### Deployment Process

1. Push the complete project to GitHub.
2. Make sure `requirements.txt` contains the required dependencies.
3. Connect the GitHub repository to Streamlit Community Cloud.
4. Select the required repository and branch.
5. Set `app.py` as the main application file.
6. Deploy the application.

After deployment, Streamlit provides a public URL for accessing the application.

---

# 🎯 Project Objective

The main objective of this project is to apply Python programming concepts to a practical real-world Library Management System.

The project combines:

* Python programming
* Lists
* Dictionaries
* Functions
* Classes and Objects
* Modules
* File Handling
* JSON data storage
* Date and Time
* Exception Handling
* Book Management
* Member Management
* Book Issue and Return
* Due Date Calculation
* Fine Calculation
* Availability Tracking
* Borrowing History
* Streamlit GUI

The project demonstrates how Python core business logic can be combined with persistent JSON storage and a Streamlit graphical interface to build a complete library automation system.

---

# 🚀 Future Enhancements

Possible future improvements include:

* User authentication
* Admin and librarian roles
* Database integration
* Email notifications
* Automatic due-date reminders
* Advanced reports
* Library analytics
* Book cover images
* Multiple user roles
* Improved search and filtering

---

# 👨‍💻 Author

**Surya Teja**



**github**--https://github.com/surya123971
**repository**--https://github.com/surya123971/library_mangment



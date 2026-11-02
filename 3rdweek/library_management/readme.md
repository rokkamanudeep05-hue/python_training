# Library Management System

## 1. Project Overview

The Library Management System is a Python-based application developed using Object-Oriented Programming (OOP) concepts.

It helps manage library operations such as adding books, registering members, issuing and returning books, tracking availability, calculating late fees, and generating reports.

The application uses JSON files for data storage, allowing records to persist even after the application is closed.

## 2. Project Objectives

- Develop a modular application using Python.
- Apply OOP concepts in a real-world project.
- Manage book and member records.
- Implement book issuing and returning functionality.
- Calculate fines for late returns.
- Generate library reports.
- Handle invalid inputs and application errors.
- Store and retrieve data using JSON files.

## 3. Features

### Book Management
- Add new books.
- Update existing book details.
- Delete available books.
- Search books by title, author, or ID.
- Display all books.
- Track book availability.

### Member Management
- Register new members.
- Update member details.
- Delete members.
- Validate membership.
- Prevent duplicate email registration.

### Book Issue and Return
- Issue books to registered members.
- Check book availability before issuing.
- Validate membership before borrowing.
- Set a borrowing period of 14 days.
- Record issue and return dates.
- Calculate late return fines.

### Fine Management
- Calculate fines based on overdue days.
- Fine rate: ₹5 per day.
- Display late-return information.
- Identify overdue books.
- Generate fine reports.

### Reports
- Available books report.
- Borrowed books report.
- Top borrowers report.
- Fine report.

## 4. Technologies Used

| Technology | Purpose |
| Python 3 | Application development |
| OOP | Code organization and design |
| JSON | Data persistence |
| pathlib | File path management |
| datetime | Date and fine calculations |
| VS Code | Development environment |
| pytest | Automated testing |

## 5. Project Structure

  
library_management/
│
├── app.py
├── book.py
├── member.py
├── issue.py
├── reports.py
├── storage.py
├── exceptions.py
├── validator.py
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── issues.json
│
└── README.md
```

## 6. Module Description

| File | Responsibility |
|---|---|
| app.py | Main application and menu |
| book.py | Book management operations |
| member.py | Member registration and management |
| issue.py | Book issue, return, and fine calculations |
| reports.py | Library reports |
| storage.py | JSON data storage and retrieval |
| exceptions.py | Custom exception handling |
| validator.py | Input validation |
| data/ | Stores application records |

## 7. OOP Concepts Implemented

- **Classes and Objects:** BookManager, MemberManager, IssueManager, and ReportManager.
- **Encapsulation:** Groups data and related operations inside classes.
- **Inheritance:** Custom exceptions inherit from a common LibraryError class.
- **Abstraction:** Exposes simple methods for complex library operations.
- **Composition:** IssueManager works with BookManager and MemberManager objects.
- **Exception Handling:** Handles invalid operations and unexpected inputs.

## 8. Installation and Setup

### Prerequisites

- Python 3.10 or newer.
- Visual Studio Code.
- Basic knowledge of Python.

### Step 1: Clone or download the project

Open the project folder in VS Code.

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### Step 4: Prepare JSON files

Create the following files inside the data folder:

- books.json
- members.json
- issues.json

Initialize each file with an empty JSON list:

```json
[]
```

### Step 5: Run the application

```bash
python app.py
```

No external Python packages are required for the core application.

## 9. Application Menu

The application provides the following operations:

```text
===== LIBRARY MANAGEMENT SYSTEM =====

1. Add book
2. List books
3. Search books
4. Update book
5. Delete book
6. Register member
7. List members
8. Update member
9. Delete member
10. Issue book
11. Return book
12. Available books report
13. Borrowed books report
14. Top borrowers report
15. Fine report
0. Exit
```

## 10. Fine Calculation

The borrowing period is 14 days.

The fine rate is ₹5 per overdue day.

Formula:

Fine = Number of Late Days × Fine Per Day

Example:

- Due date: 25 October 2026
- Return date: 28 October 2026
- Late days: 3
- Fine per day: ₹5

Total fine = 3 × 5 = ₹15.

No fine is charged for books returned on or before the due date.

## 11. Testing

The application should be tested using functional, validation, and negative test cases.

### Functional Testing

- Add and list books.
- Update and delete books.
- Register and update members.
- Issue and return books.
- Generate library reports.

### Negative Testing

- Add a book with an empty title.
- Register a member with an existing email.
- Issue an unavailable book.
- Issue a book to an invalid member.
- Return a book that was never issued.
- Delete a book that is currently borrowed.

### Persistence Testing

- Add records and close the application.
- Restart the application.
- Verify that the previously saved records are available.

### Run Automated Tests

If pytest tests have been implemented:

```bash
pip install pytest
pytest -v
```

## 12. Error Handling

The application uses custom exceptions to handle errors such as:

- BookNotFoundError
- MemberNotFoundError
- BookUnavailableError
- InvalidMembershipError
- DuplicateRecordError

These exceptions help provide meaningful error messages and prevent invalid operations.

## 13. Future Enhancements

- Integrate SQLite or MySQL database.
- Add login and authentication.
- Implement member borrowing limits.
- Add book reservation functionality.
- Generate PDF reports.
- Develop a graphical user interface.
- Add automated email notifications for overdue books.

## 14. Conclusion

The Library Management System demonstrates how Python and Object-Oriented Programming can be used to develop a modular, maintainable, and practical application.

It integrates book management, member management, borrowing operations, fine calculations, data persistence, validation, exception handling, and reporting into a single application.

The project provides practical experience in Python programming, modular architecture, OOP principles, file handling, and software testing.
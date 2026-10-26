Python Training Project
Description
This is my beginner Python project. I am learning Python setup, virtual environments, pip, and project structure.
Requirements
Python 3

Visual Studio Code

pip
Project Structure
main.py: Main Python program

.venv/: Virtual environment

requirements.txt: Python package dependencies

.gitignore: Files ignored by Git

README.md: Project documentation
Setup Instructions
Create a virtual environment:

python -m venv .venv

Activate it in Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Install project dependencies:

python -m pip install -r requirements.txt
Run the Project

 ## week 2 

 ## day1 -- monday 19/10/2026
# Python Task Tracker

A command-line task tracker using
Python collections and JSON file persistence.

## Requirements
- Python 3.15
- Visual Studio Code

## Setup

Create a virtual environment:

    python -m venv .venv

Activate on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

No external packages are required.

## Run the application

    python tracker.py

## Run unit tests

    python test_tracker -v

## Features
- Add, view, complete, and delete tasks
- Validate task titles and IDs
- Save tasks in tasks.json
- Handle missing task IDs and invalid JSON

## Acceptance checks
1. Add a task and verify it appears in the list.
2. Restart the app and verify the task is still present.
3. Complete a task and verify its status changes.
4. Enter an empty title and verify it is rejected.
5. Enter an unknown task ID and verify an error is reported.
6. Run all unit tests and verify they pass.

## day 2 -- tuesday 20/10/2026
# Python Task Tracker

## Overview
A command-line application built with Python to add, view, complete, and delete tasks. Tasks are saved in a JSON file.

## Project Structure
- `main.py` – Handles the menu and user input.
- `task_manager.py` – Manages task operations and JSON storage.
- `tasks.json` – Stores task records.
- `test_tracker.py` – Contains unit tests.

## Features
- Add, view, complete, and delete tasks.
- Save and load tasks using JSON.
- Validate task titles and IDs.
- Handle invalid JSON.
- Use type hints and modular code.

## Requirements
- Python 3.15 or later.
- No external packages required.

## Run the Application

python main.py
```

## Run Tests

python  test_tracker.py
```

Tests cover task operations, file persistence, and invalid inputs.

## Concepts Used
- Functions and modules
- Dictionaries and type hints
- JSON persistence
- Exception handling
- Unit testing


## day 3 -- 21/10/2026


# Python Task Tracker

## Overview
A command-line application to add, view, complete, and delete tasks.
Tasks are stored in a JSON file.

## Files
- `tracker.py` - TaskManager class and task operations
- `main_json.py` - Command-line menu
- `test_tracker.py` - Unit tests
- `tasks.json` - Persistent task data

## Requirements
- Python 3.15


## Run the Application
```bash
python main_json.py
```

## Run Tests
```bash
python -m test_tracker.py

```

## Validation and Error Handling
- Rejects empty task titles.
- Validates task IDs and stored task records.
- Handles malformed JSON with a clear error.
- Handles missing files by starting with an empty task list.
- Reports file access errors instead of silently ignoring them.

## Persistence Design
Data is written to a temporary file before replacing the existing
JSON file. In-memory changes are applied only after saving succeeds.

## Known Limitations
- Tasks are stored locally in a JSON file.
- There is no multi-user access or concurrent-write protection.
- Malformed JSON is reported, but automatic data recovery is not supported.
- Temporary-file replacement reduces the risk of partial writes but
  cannot protect against every hardware or filesystem failure.

  ## day 4 -- 22/10/2026

  
# Python Task Tracker – Unit Testing

## 1. Overview
This project implements a Python Task Tracker with JSON-based data persistence. Unit testing is used to verify application functionality, input validation, and error handling.

## 2. Technologies Used
- Python 3
- Pytest
- Unittest
- JSON
- Git and GitHub
- Visual Studio Code

## 3. Project Structure

```text
task-tracker/
├── tracker.py
├── test_tracker.py
├── tasks.json
└── README.md
```

## 4. Installation and Setup

### Step 1: Verify Python
```bash
python --version
```

### Step 2: Install Pytest
```bash
python -m pip install pytest
```

### Step 3: Verify Pytest
```bash
python -m pytest --version
```

## 5. Unit Testing

The test suite checks the following functionality:

- Task creation and persistence
- Empty and invalid task titles
- Title whitespace handling
- Task completion and deletion
- Invalid and unknown task IDs
- Corrupt JSON data
- Invalid JSON structure
- Duplicate task IDs
- Invalid task records

## 6. Run the Tests

Run all tests with detailed output:

```bash
python -m pytest test_tracker.py -v
```

Run an individual test:

```bash
python -m pytest test_tracker.py::TestTaskManager::test_add_task -v
```

## 7. Expected Results

- `PASSED`: The test behaved as expected.
- `FAILED`: The test did not behave as expected and requires investigation.

The test suite is designed to contain 14 test cases. Confirm the actual results by running pytest.

## 8. Git Workflow

Check modified files:

```bash
git status
```

Stage the changes:

```bash
git add tracker.py test_tracker.py README.md
```

Commit the changes:

```bash
git commit -m "test: add task tracker unit tests"
```

Push the changes to GitHub:

```bash
git push
```

## 9. Outcome

This task demonstrates how to set up pytest, execute unit tests, validate expected behavior, identify errors, and manage source code changes using Git and GitHub.


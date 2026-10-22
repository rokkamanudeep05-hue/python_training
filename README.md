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

 ## day1
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

## day 2 
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



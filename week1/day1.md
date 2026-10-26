# Day 1 — Python Environment and Workflow

**Training Date:** Monday, 12 October 2026  
**Topic:** Python Environment Setup, Development Workflow, and Git Basics

## 1. Objective

The objective of Day 1 is to set up a Python development environment, understand the basic terminal commands, create a virtual environment, manage Python dependencies using pip, and maintain project files using Git and GitHub.

## 2. Tools and Technologies

- **Python 3:** Programming language used to develop applications.
- **Visual Studio Code (VS Code):** Code editor used to write and run Python programs.
- **Virtual Environment (`.venv`):** Isolates project-specific Python packages.
- **pip:** Installs and manages Python packages.
- **Git:** Tracks changes in project files and code.
- **GitHub:** Hosts the Git repository online.
- **README.md:** Documents the project purpose, setup, and execution instructions.

## 3. Project Structure

The project follows this folder structure:

```text
python-training/
├── .venv/
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

**File and folder descriptions:**

- `.venv/` — Contains the virtual environment for the project.
- `.gitignore` — Specifies files and folders Git should ignore.
- `requirements.txt` — Lists external Python package dependencies.
- `README.md` — Explains the project and how to use it.
- `main.py` — Contains the initial Python program.

## 4. Python Installation Verification

Verify that Python is installed by running the following command in the VS Code terminal:

```bash
python --version
```

Verify pip:

```bash
python -m pip --version
```

These commands display the installed Python and pip versions.

## 5. Virtual Environment Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

If using Command Prompt instead of PowerShell:

```bat
.venv\Scripts\activate.bat
```

After activation, the terminal should normally display `(.venv)`.

To deactivate the environment:

```bash
deactivate
```

## 6. pip and Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install a package when the project requires one:

```bash
python -m pip install package_name
```

Save installed packages to `requirements.txt`:

```bash
python -m pip freeze > requirements.txt
```

Install the listed dependencies in another environment:

```bash
python -m pip install -r requirements.txt
```

For a project that uses only Python's built-in modules, an empty `requirements.txt` is acceptable.

## 7. Basic Terminal Commands

| Command | Purpose |
|---|---|
| `pwd` | Displays the current directory in supported shells. |
| `cd folder_name` | Moves into a directory. |
| `cd ..` | Moves to the parent directory. |
| `dir` | Lists files and folders in Windows Command Prompt. |
| `mkdir folder_name` | Creates a directory. |
| `python --version` | Checks the Python version. |
| `cls` | Clears the Windows terminal. |

## 8. Create and Run a Python Program

Create a file named `main.py` and add the following code:

```python
def main():
    print("Hello, Python!")
    print("Day 1: Environment and Workflow")
    print("Python environment setup completed.")


if __name__ == "__main__":
    main()
```

Run the program:

```bash
python main.py
```

Expected output:

```text
Hello, Python!
Day 1: Environment and Workflow
Python environment setup completed.
```

## 9. Git and GitHub Workflow

Initialize Git in the project directory:

```bash
git init
```

Create a `.gitignore` file containing:

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.vscode/
```

Check the current changes:

```bash
git status
```

Stage the project files:

```bash
git add README.md main.py .gitignore requirements.txt
```

Create a commit:

```bash
git commit -m "Complete Day 1 Python environment setup"
```

To publish the project, create an empty repository on GitHub, then connect it using the repository URL provided by GitHub:

```bash
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL. If a remote is already configured, check it with `git remote -v` instead of adding it again.

## 10. Outcomes

After completing Day 1, I should be able to:

- Verify Python and pip installations.
- Create and activate a virtual environment.
- Understand the purpose of project dependencies.
- Navigate directories and manage files using terminal commands.
- Create and execute a basic Python program.
- Document a project using Markdown.
- Track changes with Git and publish a repository on GitHub.


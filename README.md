# TASKY

A command-line interface (CLI) application for managing tasks using object-oriented programming principles. The application allows you to add, delete, mark tasks as completed, and list tasks. Tasks are persisted in a JSON file, so they remain saved even after closing the application.

## Project Structure

```plaintext
project-name/
└   .venv
│   README.md
└───src/
│   │   __init__.py
│   │   main.py
│   │   task_manager.py
│   │   task.py
│   │   utils.py
└───tests/
    │   __init__.py
    │   test_task.py
    │   test_task_manager.py
    │   test_utils.py
```
## Requirements

- Python 3.10+
- `unittest` (part of Python’s standard library)
- `mypy`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/okusjid/Tasky.git
    ```

2. Navigate to the project directory:

    ```bash
    cd TASKY
    ```

3. Install any required packages:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

Run the application from the command line:

```bash
python src/main.py
```
## Features

- **Add a New Task:** Add a new task with a description.
- **Delete a Task:** Delete a task by specifying its ID.
- **Mark a Task as Completed:** Mark a task as completed by specifying its ID.
- **List All Tasks:** List all tasks with completed tasks clearly indicated.

## 1. Activate Your Virtual Environment

Ensure your virtual environment is activated:

**Windows:**
```bash
.venv\Scripts\activate
```
## 2. Running Individual Test Files

You can run a specific test file using:

```bash
python -m unittest tests/test_task.py
```

## 3. Running All Tests

To run all the tests in the tests/ directory, use:

```bash
python -m unittest discover -s tests
```

## Understanding the Tests

The tests are written using Python’s built-in `unittest` framework. Here’s a brief overview of what is tested:

### Task Class (`test_task.py`)

- Task creation and initialization.
- String representation of tasks.
- Converting tasks to/from dictionaries.

### Task Manager (`test_task_manager.py`)

- Adding, deleting, and marking tasks as completed.
- Listing tasks.
- Saving and loading tasks to/from JSON format.

### Utilities (`test_utils.py`)

- Reading from and writing to the JSON file for persistence.


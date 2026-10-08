# Student Management System

A beginner-friendly Student Management System built using Python.

This project started as a console-based application and was later upgraded with JSON file handling and a Tkinter graphical user interface.

The application allows users to add, view, update, and delete student records through a simple GUI.

## Features

* **Add Student:** Add a student's name, roll number, and branch.
* **Display Students:** Display all student records in a table.
* **Select Student:** Select a student from the table to automatically load their details into the form.
* **Update Student:** Modify a selected student's name, roll number, and branch.
* **Delete Student:** Delete a selected student from the system.
* **JSON Persistence:** Student records are saved to a JSON file and loaded when the application starts.
* **Graphical User Interface:** Manage student records through a Tkinter-based GUI.
* **CRUD Operations:** Supports Create, Read, Update, and Delete operations.

## Technologies Used

* **Language:** Python
* **GUI:** Tkinter
* **Data Storage:** JSON
* **Libraries:** `json`, `tkinter`, `tkinter.ttk`
* **Concepts:** Functions, Lists, Dictionaries, Loops, Conditional Statements, File Handling, GUI Programming, and CRUD Operations

## Project Structure

```text
Python-Student-Management-System/
│
├── main.py
├── students.json
├── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Solitudeseeker/Python-Student-Management-System.git
```

### 2. Open the project folder

```bash
cd Python-Student-Management-System
```

### 3. Run the application

```bash
python main.py
```

## How to Use

After running the program, the Student Management System GUI will open.

### Add Student

1. Enter the student's name.
2. Enter the roll number.
3. Enter the branch.
4. Click **Add Student**.

The student will be added to the table and saved to `students.json`.

### Display Students

Click **Display Students** to refresh and display the student records stored in the system.

### Select Student

Click a student from the table.

Their:

- Name
- Roll Number
- Branch

will automatically appear in the input fields.

### Update Student

1. Select a student from the table.
2. Modify the information in the input fields.
3. Click **Update Student**.

The updated information will be saved to the JSON file.

### Delete Student

1. Select a student from the table.
2. Click **Delete Student**.

The selected student will be removed from the system and the JSON file will be updated.

## Learning Objectives

This project was created as a hands-on Python learning project to practice:

- Defining and calling functions
- Working with lists and dictionaries
- Using loops and conditional statements
- Working with user input
- Implementing CRUD operations
- Reading and writing JSON files
- Connecting a GUI with Python logic
- Using Tkinter widgets
- Working with `ttk.Treeview`
- Handling GUI events
- Connecting GUI operations with persistent data

## Project Versions

### Version 1.0 — Console Application

The first version was a basic console-based Student Management System.

Features included:

- Add student
- View students
- Search student
- Update student
- Delete student
- Menu-driven interface

### Version 2.0 — GUI Application

The second version upgraded the project with:

- JSON file handling
- Persistent student records
- Tkinter graphical user interface
- Student table using `ttk.Treeview`
- GUI-based Add Student operation
- GUI-based Display Students operation
- GUI-based Update Student operation
- GUI-based Delete Student operation
- Selecting students directly from the table
- Automatic loading of saved student records

## Future Improvements

- Prevent duplicate roll numbers
- Improve input validation
- Add a search feature to the GUI
- Add confirmation dialogs before deleting students
- Improve the overall UI design
- Add sorting and filtering
- Separate GUI and application logic into multiple modules

## Project Status

**Version 2.0 — GUI-based Student Management System completed**

The application currently supports persistent student records using JSON and provides a graphical interface for managing student data.

## Author

**Firozji Machhar**

Computer Science Engineering Student

GitHub: [Solitudeseeker (Firozji Machhar)](https://github.com/Solitudeseeker)

---

*Built as a hands-on Python learning project.*
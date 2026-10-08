import json
import tkinter as tk
from tkinter import ttk

students = []
window = tk.Tk()
window.title("Student Management System")
window.geometry("600x500")

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def load_students():
    with open("students.json", "r") as file:
        return json.load(file)

def add_student(name, roll, branch):
    new_student = {
        "name": name,
        "Roll No." : roll,
        "Branch" : branch
    }
    students.append(new_student)
    save_students()
    print("\nStudent added Successfully")

def add_student_gui():
    name = name_entry.get()
    roll = roll_entry.get()
    branch = branch_entry.get()

    add_student(name, roll, branch)

    result_label.config(text="Student added successfully!")

    refresh_students()
    
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)


def refresh_students():
    for item in student_table.get_children():
        student_table.delete(item)

    for student in students:
        student_table.insert("", "end", values=(student["name"], student["Roll No."], student["Branch"]))

def select_student(event):
    selected = student_table.selection()

    if selected:
        item = student_table.item(selected[0])
        values = item["values"]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, values[0])

        roll_entry.delete(0, tk.END)
        roll_entry.insert(0, values[1])

        branch_entry.delete(0, tk.END)
        branch_entry.insert(0, values[2])

def update_student_gui():
    selected = student_table.selection()

    if not selected:
        result_label.config(text="Please select a student!")
        return

    item = student_table.item(selected[0])
    old_roll = str(item["values"][1])

    for student in students:
        if str(student["Roll No."]) == old_roll:

            student["name"] = name_entry.get()
            student["Roll No."] = roll_entry.get()
            student["Branch"] = branch_entry.get()

            save_students()
            refresh_students()

            result_label.config(text="Student updated successfully!")
            return

    result_label.config(text="Student not found!")

def delete_student_gui():
    selected = student_table.selection()

    if not selected:
        result_label.config(text="Please select a student!")
        return

    item = student_table.item(selected[0])
    roll = str(item["values"][1])

    for student in students:
        if str(student["Roll No."]) == roll:

            students.remove(student)

            save_students()
            refresh_students()

            name_entry.delete(0, tk.END)
            roll_entry.delete(0, tk.END)
            branch_entry.delete(0, tk.END)

            result_label.config(text="Student deleted successfully!")
            return

    result_label.config(text="Student not found!")

students = load_students()

title_label = tk.Label(window, text="Student Management System")
title_label.pack()

form_frame = tk.Frame(window)
form_frame.pack(pady=20)

table_frame = tk.Frame(window)
table_frame.pack(pady=20)

name_label = tk.Label(form_frame, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

roll_label = tk.Label(form_frame, text="Roll No:")
roll_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

roll_entry = tk.Entry(form_frame)
roll_entry.grid(row=1, column=1, padx=10, pady=5)

branch_label = tk.Label(form_frame, text="Branch:")
branch_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

branch_entry = tk.Entry(form_frame)
branch_entry.grid(row=2, column=1, padx=10, pady=5)

result_label = tk.Label(window, text="")
result_label.pack()

button_frame = tk.Frame(window)
add_button = tk.Button(
    button_frame,
    text="Add Student",
    command=add_student_gui
)
add_button.pack(side="left", padx=5)

update_button = tk.Button(
    button_frame,
    text="Update Student",
    command=update_student_gui
)
update_button.pack(side="left", padx=5)

display_button = tk.Button(
    button_frame,
    text="Display Students",
    command=refresh_students
)
display_button.pack(side="left", padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Student",
    command=delete_student_gui
)
delete_button.pack(side="left", padx=5)

button_frame.pack(pady=10)

student_table = ttk.Treeview( table_frame, columns=("name", "roll", "branch"), show="headings")
student_table.heading("name", text="Name")
student_table.heading("roll", text="Roll No.")
student_table.heading("branch", text="Branch")
student_table.pack()

student_table.bind("<ButtonRelease-1>", select_student)

refresh_students()

window.mainloop()
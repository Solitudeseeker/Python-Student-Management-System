students = []

def add_student(name, roll, branch):
    new_student = {
        "name": name,
        "Roll No." : roll,
        "Branch" : branch
    }
    students.append(new_student)
    print("\nStudent added Successfully")

def view_student():
    if not students:
        print("No students found!")
        return

    for student in students:
        print("\n----------------")
        for key, value in student.items():
            print(key, ":", value)
        print("----------------")

def search_student():
    search_roll = input("Enter student roll number: ")
    for student in students:
        if student["Roll No."] == search_roll:
            print("\n----------------")
            print("Student Found!")
            for key, value in student.items():
                print(key, ":", value)
            print("----------------\n")
            return
    print("Student Not Found!")

def update_student():
    search_roll = input("Enter roll number to update: ")

    for student in students:
        if student["Roll No."] == search_roll:
            print("\n----------------")
            print("Student Found!")
            new_name = input("Enter new name: ")
            new_branch = input("Enter new branch: ")
            student["name"] = new_name
            student["Branch"] = new_branch
            print("Student updated successfully!")
            print("----------------\n")
            return
    print("Student Not Found!")

def delete_student():
    search_roll = input("Enter roll number to delete: ")
    for student in students:
        if student["Roll No."] == search_roll:
            print("Student Found: ", student["name"])
            confirm = input("Are you sure?(yes/no): ")
            if confirm.lower() == "yes":
                students.remove(student)
                print("Student deleted Successfully!")
            else:
                print("Deletion cancelled!")
            return
    print("Student Not Found!")

while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Add Student Selected")
        name = input("\nEnter student name: ")
        roll = input("Enter student roll number: ")
        branch = input("Enter student branch: ")

        add_student(name, roll, branch)
        
    elif choice == "2":
        print("View Students Selected")
        view_student()

    elif choice == "3":
        print("Search Student Selected")
        search_student()

    elif choice == "4":
        print("Update Student Details Selected")
        update_student()

    elif choice == "5":
        print("Delete Student Selected")
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")
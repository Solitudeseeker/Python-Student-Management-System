students = []

def add_student(name, roll, branch):
    new_student = {
        "name": name,
        "Roll No." : roll,
        "Branch" : branch
    }
    students.append(new_student)
    print("\nStudent added Successfully")

while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Exit")
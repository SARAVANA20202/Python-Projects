import json
import os

DATA_FILE = "students.json"

# Load data from JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Save data to JSON file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add new student
def add_student(data):
    student_id = input("Enter Student ID: ")
    if student_id in data:
        print("❌ Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    dept = input("Enter Department: ")
    marks = float(input("Enter Marks: "))

    data[student_id] = {
        "name": name,
        "age": age,
        "department": dept,
        "marks": marks
    }
    save_data(data)
    print("✅ Student added successfully!\n")

# View all students
def view_students(data):
    if not data:
        print("No student records found.\n")
        return

    print("\n--- All Student Records ---")
    for sid, info in data.items():
        print(f"ID: {sid}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Department: {info['department']}")
        print(f"Marks: {info['marks']}")
        print("-----------------------------")
    print()

# Search student by ID
def search_student(data):
    student_id = input("Enter Student ID to search: ")
    if student_id in data:
        info = data[student_id]
        print("\n--- Student Found ---")
        print(f"ID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Department: {info['department']}")
        print(f"Marks: {info['marks']}\n")
    else:
        print("❌ Student not found!\n")

# Update student details
def update_student(data):
    student_id = input("Enter Student ID to update: ")
    if student_id not in data:
        print("❌ Student not found!\n")
        return

    print("What do you want to update?")
    print("1. Department")
    print("2. Marks")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        new_dept = input("Enter new Department: ")
        data[student_id]["department"] = new_dept
    elif choice == "2":
        new_marks = float(input("Enter new Marks: "))
        data[student_id]["marks"] = new_marks
    else:
        print("Invalid choice!")
        return

    save_data(data)
    print("✅ Student details updated successfully!\n")

# Delete a student
def delete_student(data):
    student_id = input("Enter Student ID to delete: ")
    if student_id in data:
        del data[student_id]
        save_data(data)
        print("🗑️ Student record deleted successfully!\n")
    else:
        print("❌ Student not found!\n")

# Main program
def main():
    data = load_data()

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            update_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            print("Exiting program... 👋")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Correct entry point
if __name__ == "__main__":
    main()

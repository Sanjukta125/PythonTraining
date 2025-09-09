import os
import shutil

def write_file():
    with open("FileHandling/student.txt", "w") as f:
        n = int(input("Enter number of students: "))
        for i in range(n):
            name = input(f"Enter name of student {i+1}: ")
            roll = input(f"Enter roll number of student {i+1}: ")
            marks = input(f"Enter marks of student {i+1}: ")
            f.write(f"Name: {name}, Roll: {roll}, Marks: {marks}\n")
    print(" Data written to students.txt")

def read_file():
    if os.path.exists("FileHandling/student.txt"):
        with open("FileHandling/student.txt", "r") as f:
            print("\n File Content:")
            print(f.read())
    else:
        print(" students.txt not found!")

def rename_file():
    if os.path.exists("FileHandling/student.txt"):
        os.rename("FileHandling/student.txt", "FileHandling/student_records.txt")
        print(" File renamed to student_records.txt")
    else:
        print(" students.txt not found!")

def create_and_move():
    dirname = "FileHandling/SchoolData"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print(" Directory SchoolData created")
    source="FileHandling/student_records.txt"
    if os.path.exists(source):
        shutil.move(source,dirname)
        print(" student_records.txt moved to SchoolData")

        print("\n Files inside SchoolData:")
        print(os.listdir(dirname))
    else:
        print(" student_records.txt not found!")

def delete_all():
    filepath = "FileHandling/student_records.txt"
    dirname = "FileHandling/SchoolData"
    

    if os.path.exists(filepath):
        os.remove(filepath)
        print("student_records.txt deleted")

    if os.path.exists(dirname):
        os.rmdir(dirname)  # works only if folder is empty
        print("SchoolData directory deleted")

def menu():
    while True:
      
        print("1. Write to students.txt")
        print("2. Read students.txt")
        print("3. Rename students.txt → student_records.txt")
        print("4. Create SchoolData & Move student_records.txt")
        print("5. Delete file and directory")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            write_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            rename_file()
        elif choice == "4":
            create_and_move()
        elif choice == "5":
            delete_all()
        elif choice == "6":
            print(" Exiting program.")
            break
        else:
            print(" Invalid choice")

# Run the menu
menu()

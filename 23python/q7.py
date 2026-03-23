#7. Build a Student Record System using nested dictionaries/lists to add students, update marks, compute averages, and find toppers.
students = {}

def add_student():
    name = input("Enter name: ")
    marks = list(map(int, input("Enter marks separated by space: ").split()))
    students[name] = {"marks": marks}

def update_marks():
    name = input("Enter name to update: ")
    if name in students:
        marks = list(map(int, input("Enter new marks: ").split()))
        students[name]["marks"] = marks
    else:
        print("Student not found")

def compute_average():
    for name, data in students.items():
        avg = sum(data["marks"]) / len(data["marks"])
        print(name, "Average:", avg)

def find_topper():
    topper = None
    highest = 0
    for name, data in students.items():
        avg = sum(data["marks"]) / len(data["marks"])
        if avg > highest:
            highest = avg
            topper = name
    print("Topper:", topper, "with average", highest)

while True:
    print("\n1.Add 2.Update 3.Average 4.Topper 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        compute_average()
    elif choice == "4":
        find_topper()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
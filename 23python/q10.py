#10. Student Record Manager Create a system where a user can enter multiple student records (name, roll number, marks). Use loops to add records and conditions to filter students based on pass/fail criteria. Store data using dictionaries and lists.
students = []

while True:
    print("\n1.Add Record 2.Display Pass/Fail 3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "roll": roll, "marks": marks})

    elif choice == "2":
        for s in students:
            status = "Pass" if s["marks"] >= 40 else "Fail"
            print(s["name"], "-", s["roll"], "-", s["marks"], "-", status)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
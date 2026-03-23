#9. Employee Attendance System Build a loop-based menu system to add, remove, and display employee names stored in a dictionary. Use conditions and loops to control program flow.
employees = {}

while True:
    print("\n1.Add 2.Remove 3.Display 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        employees[emp_id] = name

    elif choice == "2":
        emp_id = input("Enter employee ID to remove: ")
        if emp_id in employees:
            del employees[emp_id]
        else:
            print("Employee not found")

    elif choice == "3":
        for emp_id, name in employees.items():
            print(emp_id, ":", name)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
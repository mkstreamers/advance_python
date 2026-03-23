def manage_integer_list():
    """
    Manages a list of integers with add, remove, sort, and display operations.
    """
    integer_list = []
    
    while True:
        print("\n--- List Operations Menu ---")
        print("1. Add an integer")
        print("2. Remove an integer")
        print("3. Sort the list")
        print("4. Display the list")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            # Add operation
            try:
                num = int(input("Enter an integer to add: "))
                integer_list.append(num)
                print(f"{num} added to the list.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                
        elif choice == '2':
            # Remove operation
            if not integer_list:
                print("The list is empty. Cannot remove elements.")
                continue
                
            try:
                num = int(input("Enter an integer to remove: "))
                if num in integer_list:
                    integer_list.remove(num)
                    print(f"{num} removed from the list.")
                else:
                    print(f"{num} is not in the list.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                
        elif choice == '3':
            # Sort operation
            if not integer_list:
                print("The list is empty. Nothing to sort.")
                continue
                
            integer_list.sort()
            print("List sorted in ascending order.")
            
        elif choice == '4':
            # Display operation
            if not integer_list:
                print("The list is currently empty.")
            else:
                print(f"Current list: {integer_list}")
                
        elif choice == '5':
            # Exit
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    # This ensures the function runs when the script is executed
    manage_integer_list()

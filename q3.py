#Write a Python program to create a list of integers and perform add, remove, sort, and display operations.
# Function to display the current list
def display_list(int_list):
    """Displays the current list of integers."""
    if not int_list:
        print("The list is currently empty.")
    else:
        print(f"Current list: {int_list}")
    print("-" * 20)

# Function to add an item to the list
def add_item(int_list):
    """Prompts the user for an integer and adds it to the list."""
    try:
        item = int(input("Enter an integer to add: "))
        int_list.append(item)
        print(f"Added {item}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    
# Function to remove an item from the list
def remove_item(int_list):
    """Prompts the user for an integer and removes the first occurrence from the list."""
    if not int_list:
        print("The list is empty. Cannot remove items.")
        return
    try:
        item = int(input("Enter an integer to remove: "))
        if item in int_list:
            int_list.remove(item)
            print(f"Removed the first occurrence of {item}.")
        else:
            print(f"{item} not found in the list.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Function to sort the list
def sort_list(int_list):
    """Sorts the list in ascending order."""
    if not int_list:
        print("The list is empty. Cannot sort.")
        return
    int_list.sort()
    print("List sorted in ascending order.")

# Main program loop
def main():
    """Manages the main program flow for list operations."""
    # Initialize an empty list of integers
    my_list = []

    while True:
        print("\nMenu:")
        print("1. Display list")
        print("2. Add an item")
        print("3. Remove an item")
        print("4. Sort list")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_list(my_list)
        elif choice == '2':
            add_item(my_list)
        elif choice == '3':
            remove_item(my_list)
        elif choice == '4':
            sort_list(my_list)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the script
if __name__ == "__main__":
    main()





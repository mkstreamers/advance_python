# Function to convert and display data types
def convert_and_display(value):
    try:
        # Convert to integer
        int_value = int(value)
        # Convert to float
        float_value = float(value)
        # Convert to string (the input is already a string but we explicitly convert the float for clarity)
        string_value = str(float_value)

        # Display results
        print(f"Original input: {value}")
        print(f"Integer value: {int_value}, Data type: {type(int_value)}")
        print(f"Float value: {float_value}, Data type: {type(float_value)}")
        print(f"String value: {string_value}, Data type: {type(string_value)}")

    except ValueError:
        print(f"Error: '{value}' cannot be converted to a number. Please enter a valid numerical input.")

# Main part of the program
if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter a number: ")

    # Call the function to process the input
    convert_and_display(user_input)

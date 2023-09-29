# Define a function to check if a name is valid
def checking_name(name):
    # Check if any character is a digit or not an alphabet letter
    if any(char.isdigit() or not char.isalpha() for char in name):
        # Raise a ValueError if the name is invalid
        raise ValueError("Invalid name. Please enter only alphabets.")
    else:
        # Print a message if the name is valid
        print("Valid name entered.")

# Initialize a flag to control the program loop
repeat_program = True

# Continue running the program until the user decides to exit
while repeat_program:
    try:
        # Prompt the user for their name
        name = input("Enter your name: ")
        # Check if the name is valid using the checking_name function
        checking_name(name)
    except ValueError as ve:
        # Catch and print any ValueErrors that occur
        print(ve)

    # Ask the user if they want to run the program again
    repeat_input = input("Do you want to run the program again? (y/n): ")
    
    # Check if the input is 'y' to continue, otherwise exit the loop
    if repeat_input.lower() == "y":
        repeat_program = True
    else:
        repeat_program = False

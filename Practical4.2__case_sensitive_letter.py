# Initialize a boolean variable 'l' to control the program's loop
l = True

# Start a loop that continues as long as 'l' is True
while l == True:
    # Input a character from the user as a string
    char = str(input("Enter a character: "))
    
    # Check if the input length is not equal to 1 or if it's a digit
    if len(char) != 1 or char.isdigit():
        print("Please enter a single letter!")  # Print an error message
    else:
        # Check if the character is uppercase
        if char.isupper():
            print(char, "is uppercase.")
        else:
            print(char, "is lowercase.")
    
    # Ask the user if they want to run the program again
    l = input("Do you want to run the program again? (y/n): ")
    
    # Convert the user's input to a boolean value ('True' or 'False')
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

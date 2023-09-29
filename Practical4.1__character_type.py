# Initialize a boolean variable 'l' to control the program's loop
l = True

# Start a loop that continues as long as 'l' is True
while l == True:
    # Input a character from the user as a string
    char = str(input("Enter a character: "))
    
    # Check if the input length is not equal to 1 (not a single character)
    if len(char) != 1:
        print("Enter a single letter!")  # Print an error message
    else:
        # Check if the character is a letter (uppercase or lowercase)
        if ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
            print(char, "is a letter.")
        # Check if the character is a digit (0-9)
        elif (char >= '0' and char <= '9'):
            print(char, "is a Numeric Digit.")
        else:
            # If it's not a letter or a number, consider it a symbol
            print(char, "is a Special Character.")
    
    # Ask the user if they want to run the program again
    l = input("Do you want to run the program again? (y/n): ")
    
    # Convert the user's input to a boolean value ('True' or 'False')
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

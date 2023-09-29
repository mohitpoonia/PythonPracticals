# Define a function 'num_2_word' to convert a digit character to its word representation
def num_2_word(char):
    if char == '0':
        print("Zero")
    elif char == '1':
        print("One")
    elif char == '2':
        print("Two")
    elif char == '3':
        print("Three")
    elif char == '4':
        print("Four")
    elif char == '5':
        print("Five")
    elif char == '6':
        print("Six")
    elif char == '7':
        print("Seven")
    elif char == '8':
        print("Eight")
    else:
        print("Nine")

# Initialize a boolean variable 'l' to control the program's loop
l = True

# Start a loop that continues as long as 'l' is True
while l == True: 
    # Input a character from the user as a string
    char = input("Enter a character: ")
    
    # Check if the input length is not equal to 1 or if it's an alphabet character
    if len(char) != 1 or char.isalpha():
        print("Please enter a single number!")  # Print an error message
    else:
        # Call the 'num_2_word' function to convert the digit character to its word representation
        num_2_word(char)
    
    # Ask the user if they want to run the program again
    l = input("Do you want to run the program again? (y/n): ")
    
    # Convert the user's input to a boolean value ('True' or 'False')
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

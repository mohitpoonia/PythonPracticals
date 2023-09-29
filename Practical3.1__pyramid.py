# Function to print a pyramid with 'n' rows
def print_pyramid(n):
    # Loop to iterate through each row of the pyramid
    for i in range(1, n + 1):
        # Print leading spaces (before the asterisks)
        for j in range(n - i):
            print(" ", end="")  # Print a space without moving to the next line
        
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end="")  # Print an asterisk without moving to the next line
        
        # Move to the next line to start a new row
        print()  # Print an empty line to move to the next row

# Main program
while True:
    # Ask the user for the number of rows in the pyramid
    n = int(input("Enter the number of rows for the pyramid: "))
    print_pyramid(n)  # Call the function to print the pyramid

    # Ask if the user wants to print another pyramid
    repeat = input("Do you want to print another pyramid? (yes/no): ")
    if repeat.lower() != "yes":
        break  # Exit the loop if the user's input is not "yes"

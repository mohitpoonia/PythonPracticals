# Function to print a reverse pyramid with 'n' rows
def print_reverse_pyramid(n):
    # Loop to iterate through each row of the reverse pyramid
    for i in range(n, 0, -1):
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
    # Ask the user for the number of rows in the reverse pyramid
    n = int(input("Enter the number of rows for the reverse pyramid: "))
    print_reverse_pyramid(n)  # Call the function to print the reverse pyramid

    # Ask if the user wants to print another reverse pyramid
    repeat = input("Do you want to print another reverse pyramid? (yes/no): ")
    if repeat.lower() != "yes":
        break  # Exit the loop if the user's input is not "yes"

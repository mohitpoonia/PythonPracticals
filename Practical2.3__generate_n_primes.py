# Initialize a boolean variable 'l' to control the program's loop
l = True

# Start a loop that continues as long as 'l' is True
while l == True:
    # Input the number of prime numbers to generate 'n' from the user
    n = int(input("Enter the number of prime numbers you want: "))
    
    # Initialize a variable 'i' to start checking numbers from 2 onwards
    i = 2
    
    # Continue generating prime numbers until 'n' prime numbers are found
    while n != 0:
        # Check if 'i' is prime by testing for divisibility with numbers from 2 to 'i-1'
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            # If 'i' is not divisible by any 'j', it's a prime number, so print it
            print(i)
            n -= 1  # Decrease the count of prime numbers remaining to be found
        i += 1  # Move on to the next number
    
    # Ask the user if they want to run the program again
    l = input("Do you want to run the program again? (y/n): ")
    
    # Convert the user's input to a boolean value ('True' or 'False')
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

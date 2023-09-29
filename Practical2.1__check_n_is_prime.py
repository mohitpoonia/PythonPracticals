# Initialize a boolean variable 'l' to control the program's loop
l = True

# Start a loop that continues as long as 'l' is True
while l == True:
    # Initialize a boolean variable 'is_prime' as True by default
    is_prime = bool(1)
    
    # Input a number 'n' from the user
    n = int(input("Enter a number: "))
    
    # Check if 'n' is 0 or 1 (neither prime nor composite)
    if n == 1 or n == 0:
        print(n, "is neither prime nor composite.")
    elif n > 1:
        i = int(2)
        
        # Start a loop to check for factors from 2 to n/2
        while i < n/2:
            # If 'n' is divisible by 'i', set 'is_prime' to False and break the loop
            if n % i == 0:
                is_prime = bool(0)
                break
            else:
                i += 1
        
        # Check if 'is_prime' is still True (no factors found)
        if is_prime:
            print(n, "is a prime number.")
        else:
            print(n, "is not a prime number.")
        
        # Ask the user if they want to run the program again
        l = input("Do you want to run the program again? (y/n): ")
        
        # Convert the user's input to a boolean value ('True' or 'False')
        if l == "y":
            l = bool(1)
        else:
            l = bool(0)

# Initialize a boolean variable 'l' to control the program's loop
l = True

# Start a loop that continues as long as 'l' is True
while l == True:
    # Input a number 'n' from the user to generate prime numbers up to 'n'
    n = int(input("Generate prime numbers up to: "))
    
    # Iterate through numbers from 2 to 'n'
    for i in range(2, n + 1):
        # Iterate through numbers from 2 to 'i' (exclusive)
        for j in range(2, i):
            # Check if 'i' is divisible by 'j', if yes, 'i' is not prime, break the loop
            if i % j == 0:
                break
        else:
            # If 'i' is not divisible by any 'j', it's a prime number, so print it
            print(i)
    
    # Ask the user if they want to run the program again
    l = input("Do you want to run the program again? (y/n): ")
    
    # Convert the user's input to a boolean value ('True' or 'False')
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

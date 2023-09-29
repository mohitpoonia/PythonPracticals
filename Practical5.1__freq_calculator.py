# Initialize a boolean variable 'l' to control the program's loop
l = True

# Start a loop that continues as long as 'l' is True
while l == True: 
    # Input a string from the user
    my_string = str(input("Enter a string: "))
  
    # Initialize an empty dictionary 'freq' to store character frequencies
    freq = {}
  
    # Iterate through each character in the input string
    for i in my_string:
        # Check if the character 'i' is already in the 'freq' dictionary
        if i in freq:
            # If it is, increment its count by 1
            freq[i] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            freq[i] = 1
  
    # Print the character frequencies in the input string
    print("Count of all characters in", my_string, "is :")
    print(freq)
    
    # Ask the user if they want to run the program again
    l = input("Do you want to run the program again? (y/n): ")
    
    # Convert the user's input to a boolean value ('True' or 'False')
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

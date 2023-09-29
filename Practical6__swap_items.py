# Initialize a boolean variable 'l' to control the program's loop
l = True

# Start a loop that continues as long as 'l' is True
while l == True: 
    # Input the first string from the user
    str1 = input("Please Enter First String: ")
    
    # Input the second string from the user
    str2 = input("Please Enter Second String: ")
    
    # Input the number of characters to swap from the user
    n = int(input("Enter the number of characters to swap: "))
    
    # Extract the first 'n' characters from the first string 'str1'
    x = str1[0:n]

    # Replace the first 'n' characters in 'str1' with the first 'n' characters from 'str2'
    str1 = str1.replace(str1[0:n], str2[0:n])

    # Replace the first 'n' characters in 'str2' with the extracted characters 'x'
    str2 = str2.replace(str2[0:n], x)

    # Print the modified first and second strings
    print("Your first string has become:", str1)
    print("Your second string has become:", str2)
    
    # Ask the user if they want to run the program again
    l = input("Do you want to run the program again? (y/n): ")
    
    # Convert the user's input to a boolean value ('True' or 'False')
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

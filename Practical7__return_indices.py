# Initialize a flag to control the program loop
repeat_program = True

# Continue running the program until the user decides to exit
while repeat_program:
    # Prompt the user for two strings
    str1 = str(input("Enter a string: "))
    str2 = str(input("Enter another string: "))
    
    # Initialize a list to store indices where str2 is found in str1
    indices = []
    index = -1
    
    # Search for str2 in str1 and record indices of each occurrence
    while True:
        index = str1.find(str2, index + 1)
        if index == -1:
            break
        indices.append(index)
    
    # Check if any indices were found and print the results
    if indices:
        print(indices)
    else:
        print(-1)
    
    # Ask the user if they want to run the program again
    repeat_input = input("Do you want to run the program again? (y/n): ")
    
    # Check if the input is 'y' to continue, otherwise exit the loop
    if repeat_input.lower() == "y":
        repeat_program = True
    else:
        repeat_program = False

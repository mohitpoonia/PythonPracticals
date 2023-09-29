# Input a sentence from the user
str1 = str(input("Enter a sentence: "))

# Initialize an empty string 'result' to store the modified sentence
result = ""

# Input a character to remove from the user
ch_to_remove = str(input("Input a character: "))

# Iterate over each character in the input sentence 'str1'
for ch in str1:
    # Initialize a boolean flag 'occurred_flag' to track if the character occurred
    occurred_flag = False
    
    # Check if the character 'ch' is equal to the character to be removed 'ch_to_remove'
    # and if 'occurred_flag' is False (indicating the first occurrence)
    if ch == ch_to_remove and occurred_flag == False:
        # Set 'occurred_flag' to True to indicate the character has occurred
        occurred_flag = True
        continue  # Skip adding this character to 'result'
    else:
        # If it's not the character to remove or if it's not the first occurrence,
        # add the character to the 'result' string
        result += ch

# Display the resulting modified string without the first occurrence of 'ch_to_remove'
print(result)

# Ask the user if they want to run the program again and store their input in the variable 'l'
l = input("Do you want to run the program again? (y/n): ")

# Check if the user's input is equal to "y" (yes)
if l == "y":
    # If the user input is "y", set the variable 'l' to True
    l = bool(1)  # This converts the string "1" to the boolean value True
else:
    # If the user input is not "y" (no), set the variable 'l' to False
    l = bool(0)  # This converts the string "0" to the boolean value False

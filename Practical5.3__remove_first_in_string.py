# Input a sentence from the user
str1 = str(input("Enter a word: "))

# Initialize an empty string 'result' to store the modified sentence
result = ""

# Input a character to remove from the user
ch_to_remove = str(input("Input a character: "))

# Initialize a flag 'occurred_flag' to track if the character occurred
occurred_flag = False

# Iterate over each character in the input sentence 'str1'
for ch in str1:
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
# Ask the user if they want to run the program again
l = input("Do you want to run the program again? (y/n): ")
    
    # Convert the user's input to a boolean value ('True' or 'False')
if l == "y":
        l = bool(1)
else:
        l = bool(0)

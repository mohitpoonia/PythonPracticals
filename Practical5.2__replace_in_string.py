# Input a string from the user
string = str(input("Enter a string: "))

# Input the character to replace and the character to replace with from the user
char_to_replace = input("Enter the character to replace: ")
replacement_char = input("Enter the character to replace with: ")

# Use the 'replace' method to create a new string with character replacements
new_string = string.replace(char_to_replace, replacement_char)

# Print the original and new strings
print("Original String: ", string)
print("New String: ", new_string)
 # Ask the user if they want to run the program again
l = input("Do you want to run the program again? (y/n): ")
    
# Convert the user's input to a boolean value ('True' or 'False')
if l == "y":
        l = bool(1)
else:
        l = bool(0)

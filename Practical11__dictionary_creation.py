# Ask the user for the number of terms
num_terms = int(input("Enter the number of terms: "))

# Initialize an empty dictionary to store the results
cubed_dict = {}

# Calculate the cubes of numbers from 1 to num_terms and store them in the dictionary
for i in range(1, num_terms + 1):
    # Calculate the cube of the current number and create a dictionary entry
    cubed_value = i ** 3
    term_dict = {i: cubed_value}
    
    # Update the main dictionary with the new entry
    cubed_dict.update(term_dict)

# Print the resulting dictionary
print(cubed_dict)

# Ask the user if they want to repeat the code
repeat = input("Do you want to run the code again? (yes/no): ")

# Check if the user wants to repeat or not
if repeat.lower() == "yes":
    # If "yes," repeat the code
    pass  # Pass statement allows continuing to the next iteration of the loop
else:
    # If "no" or anything else, exit the program
    print("Goodbye!")

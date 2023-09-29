# Given tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a. Print half the values of the tuple in one line and the other half in the next line.
half_length = len(t1) // 2  # Calculate the midpoint of the tuple
first_half = t1[:half_length]  # Slice the first half of the tuple
second_half = t1[half_length:]  # Slice the second half of the tuple
print("First Half:", first_half)  # Print the first half
print("Second Half:", second_half)  # Print the second half

# b. Print another tuple whose values are even numbers in the given tuple.
even_numbers = tuple(x for x in t1 if x % 2 == 0)  # Create a new tuple with even numbers from t1
print("Tuple of Even Numbers:", even_numbers)  # Print the tuple of even numbers

# c. Concatenate a tuple t2=(11, 13, 15) with t1.
t2 = (11, 13, 15)
concatenated_tuple = t1 + t2  # Concatenate t1 and t2 to create a new tuple
print("Concatenated Tuple:", concatenated_tuple)  # Print the concatenated tuple

# d. Return maximum and minimum value from this tuple
max_value = max(concatenated_tuple)  # Find the maximum value in the concatenated tuple
min_value = min(concatenated_tuple)  # Find the minimum value in the concatenated tuple
print("Maximum Value:", max_value)  # Print the maximum value
print("Minimum Value:", min_value)  # Print the minimum value

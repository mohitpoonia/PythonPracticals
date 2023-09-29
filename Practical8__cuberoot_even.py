while True:
    # Initialize an empty list to store the cubes of even integers
    cubes_of_even = []

    # Get user input as a comma-separated list of elements
    input_str = input("Enter a list of elements separated by commas: ")

    # Split the input string into a list of elements
    input_list = input_str.split(",")

    # Iterate through the elements of the input list
    for element in input_list:
        # Convert the element to an integer (if possible)
        try:
            element = int(element)
        except ValueError:
            # If conversion to int fails, skip this element
            continue

        # Check if the element is an integer and even
        if isinstance(element, int) and element % 2 == 0:
            # Cube the even integer and add to the list
            cubes_of_even.append(element ** 3)

    # Print the list containing cubes of even integers
    print(cubes_of_even)

    # Ask if the user wants to repeat the process
    repeat = input("Do you want to repeat? (yes/no): ")
    if repeat.lower() != "yes":
        break  # Exit the loop if the user's input is not "yes"

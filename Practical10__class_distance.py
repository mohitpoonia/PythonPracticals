import math

# Initialize a flag to control the program loop
repeat_program = True

# Continue running the program until the user decides to exit
while repeat_program:
    # Define a class called "Point" to represent points in 2D space
    class Point:
        # Constructor to initialize the Point object with x and y coordinates
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # Method to print the coordinates of the point
        def print_point(self):
            print("Point coordinates: ({}, {})".format(self.x, self.y))

        # Method to calculate the Euclidean distance between two points
        def distance(self, other_point):
            dx = self.x - other_point.x
            dy = self.y - other_point.y
            return math.sqrt(dx ** 2 + dy ** 2)

    # Prompt the user to enter coordinates for the first point
    print("For the first set of coordinates:")
    x1 = int(input("Enter value at x-axis: "))
    y1 = int(input("Enter value at y-axis: "))
    p1 = Point(x1, y1)

    # Prompt the user to enter coordinates for the second point
    print("For the second set of coordinates:")
    x2 = int(input("Enter value at x-axis: "))
    y2 = int(input("Enter value at y-axis: "))
    p2 = Point(x2, y2)

    # Print the coordinates of both points
    p1.print_point()
    p2.print_point()

    # Calculate and print the distance between the two points
    distance = p1.distance(p2)
    print("Distance between p1 and p2: {}".format(distance))

    # Ask the user if they want to run the program again
    repeat_input = input("Do you want to run the program again? (y/n): ")
    
    # Check if the input is 'y' to continue, otherwise exit the loop
    if repeat_input.lower() == "y":
        repeat_program = True
    else:
        repeat_program = False

# Define a function 'eqn' to solve a quadratic equation
def eqn(a, b, c):
    
    # Declare 'det' as a global variable to store the determinant
    
    global det
    det = b**2 - 4*a*c
    # Calculate the determinant
    if det == 0 or det > 0:
        # If the determinant is zero or positive, calculate real solutions
        x1 = float((-b + (det)**0.5) / (2 * a))
        x2 = float((-b - (det)**0.5) / (2 * a))
        return x1, x2
    elif det < 0:
        # If the determinant is negative, there are no real solutions
        return "No real solutions"

# Initialize a boolean variable 'l' to control the program's loop
l = True

# Start a loop that continues as long as 'l' is True
while l == True:
    # Input coefficients of the quadratic equation
    a = int(input("Enter the coefficient of x²: "))
    b = int(input("Enter the coefficient of x: "))
    c = int(input("Enter the constant term: "))
    
    # Call the 'eqn' function to solve the equation and print the result
    print(eqn(a, b, c))
    
    # Ask the user if they want to run the program again
    l = input("Do you want to run the program again? (y/n): ")
    
    # Convert the user's input to a boolean value ('True' or 'False')
    if l == "y":
        l = bool(1)
    else:
        l = bool(0)

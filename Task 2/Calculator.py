# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator function
def calculator():
    print("Simple Calculator")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input for operation choice
    choice = input("Enter operation choice (1/2/3/4): ")

    # Check if the input is valid
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        return

    # Get user input for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")

# Run the calculator
calculator()

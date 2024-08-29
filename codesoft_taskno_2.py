def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not possible."
    return x / y
def main():
    while True:
        print("Welcome to the Simple Calculator")
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid values.")
            continue
        
        print("Choose the operation form the following:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        operation = input("Enter the operation number (1/2/3/4): ")
        if operation == '1':
            result = add(number1, number2)
        elif operation == '2':
            result = subtract(number1, number2)
        elif operation == '3':
            result = multiply(number1, number2)
        elif operation == '4':
            result = divide(number1, number2)
        else:
            result = "Invalid operation choice."
        
        print("Result:", result)
        continue_choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Thank you for using Simple Calculator. Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()

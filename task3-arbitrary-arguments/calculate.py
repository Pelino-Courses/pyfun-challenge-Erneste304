def process_numbers(*args, **kwargs):
    """
    Helper function to process numbers
    args:
        *args: list of numbers
        **kwargs: dictionary of operations
    returns:
        result: result of the operation  
    """
    if not args:
        raise ValueError("At least one number is required.")
    for num in args:
        if not isinstance(num, (int, float)):
            raise TypeError(f"Invalid number: {num}. Must be int or float.")
    
    result = args[0]
    for num in args[1:]:
        if 'add' in kwargs and kwargs['add']:
            result += num
        elif 'subtract' in kwargs and kwargs['subtract']:
            result -= num
        elif 'multiply' in kwargs and kwargs['multiply']:
            result *= num
        elif 'divide' in kwargs and kwargs['divide']:
            if num == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result /= num
    return result

def calculator():
    """
    Calculator function to perform basic arithmetic operations
    """
    print("Calculator")
    print("Enter your numbers:")
    numbers = input("Numbers (comma-separated): ")
    numbers = [float(num) for num in numbers.split(",")]
    
    print("Choose your operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Operation (1/2/3/4): ")
    
    if operation == '1':
        result = process_numbers(*numbers, add=True)
        print(f"Result: {result}")
    elif operation == '2':
        result = process_numbers(*numbers, subtract=True)
        print(f"Result: {result}")
    elif operation == '3':
        result = process_numbers(*numbers, multiply=True)
        print(f"Result: {result}")
    elif operation == '4':
        result = process_numbers(*numbers, divide=True)
        print(f"Result: {result}")
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    try:
        print(process_numbers(10, 20, add=True))       # ➜ 30
        print(process_numbers(10, 250, multiply=True))  # ➜ 2500
        print(process_numbers(1000, 500, divide=True))    # ➜ 2.0
    except Exception as e:
        print("Error:", e)

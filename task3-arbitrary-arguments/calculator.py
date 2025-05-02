def process_numbers(*args, **kwargs):
    """
    Helper function to process inputs and validate them.

    Returns:
    a tuple of numbers and a dictionary of operations.
    
    Raises:
    TypeError or ValueError for invalid inputs.
    """
    try:
        numbers = []  # list to store numbers
        for arg in args:

            if isinstance(arg, (int, float)):
                numbers.append(arg)

            else:
                raise TypeError(f"Invalid argument: {arg}. All arguments must be numbers.")
        
        operations = {}  # dictionary to store operations

        for key, value in kwargs.items():  # iterate through keyword arguments
            if key not in ['add', 'subtract', 'multiply', 'divide'] or not isinstance(value, bool):
                raise ValueError(f"Invalid operation: {key}. Must be one of ['add', 'subtract', 'multiply', 'divide'].")
            operations[key] = value
        
        return numbers, operations

    except TypeError as e:
        return f"Error: {e}"
    
    except ValueError as e:
        return f"Error: {e}"
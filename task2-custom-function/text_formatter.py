def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """
    Format the input text with optional prefix, suffix, capitalization, and maximum length.

    Args:
        text (str): The input text to format.
        prefix (str): Optional prefix to add to the text.
        suffix (str): Optional suffix to add to the text.
        capitalize (bool): Whether to capitalize the first letter of the text.
        max_length (int): Optional maximum length of the formatted text.

    Returns:
        str: The formatted text.
    """
    if not isinstance(text, str):
        raise TypeError("The 'text' argument must be a string.")
    
    if not isinstance(prefix, str):
        raise TypeError("The 'prefix' argument must be a string.")
    
    if not isinstance(suffix, str):
        raise TypeError("The 'suffix' argument must be a string.")
    
    if not isinstance(capitalize, bool):
        raise TypeError("The 'capitalize' argument must be a boolean.")
    
    if max_length is not None and not isinstance(max_length, int):
        raise TypeError("The 'max_length' argument must be an integer.")

    formatted_text = f"{prefix}{text}{suffix}"

    if capitalize:
        formatted_text = formatted_text.capitalize()

    if max_length is not None and len(formatted_text) > max_length:
        formatted_text = formatted_text[:max_length]

    return formatted_text
def main():
    print("text_formatter editor")

    print("enter your formatting options:")
    text = input("text: ")
    prefix = input("prefix: ")
    suffix = input("suffix: ")
    cap_input = input("capitalize (y/n): ")
    if cap_input.lower() == 'y':
        capitalize = True
    elif cap_input.lower() == 'n':
        capitalize = False
    else:
        print("Invalid input for capitalization. Defaulting to False.")
        capitalize = False
    max_length_input = input("max length (or press enter for no limit): ")
    if max_length_input:
        try:
            max_length = int(max_length_input)
        except ValueError:
            print("Invalid input for max length. Defaulting to no limit.")
            max_length = None
    else:
        max_length = None
    formatted_text = format_text(text, prefix, suffix, capitalize, max_length)
    print("Formatted text:", formatted_text)
if __name__ == "__main__":
    main()

#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    :param text: The input text.
    :raises TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a flag to check if a new line has been added recently
    new_line_added = False

    for char in text:
        if char in ['.', '?', ':']:
            print(char, end='')
            print("\n\n", end='')
            new_line_added = True
        elif char == ' ' and new_line_added:
            pass  # Skip spaces after adding new lines
        else:
            print(char, end='')
            new_line_added = False

    # Ensure there are no trailing spaces or new lines
    print('', end='')


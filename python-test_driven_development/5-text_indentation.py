#!/usr/bin/python3
def text_indentation(text):
    """ This function takes a string and prints it with
    two new lines after each delimiters.
    Each new line should be indented with no spaces
    at the beginning or end of each line.
    Raises: TypeError: If the provided argument is not a string. """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"

    lines = []
    current_line = ""
    for char in text:
        current_line += char
        if char in delimiters:
            current_line = current_line.strip()
            lines.append(current_line)
            lines.append("")
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line)

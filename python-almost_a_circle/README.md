# Python - Almost a Circle

## Description
This project involves the implementation of classes to represent rectangles and squares, with validation of attributes and methods for manipulation. It covers concepts such as inheritance, class methods, static methods, getters and setters, serialization, deserialization, and unit testing.

## Tasks Examples
### 0. If it's not tested it doesn't work
All files, classes, and methods must be unit tested and PEP 8 validated.

### 3. Validate attributes
Update the `Rectangle` class by adding validation for all setter methods and instantiation (excluding id):
- If the input is not an integer, raise a TypeError exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`.
- If width or height is less than or equal to 0, raise a ValueError exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`.
- If x or y is less than 0, raise a ValueError exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`.

## PEP 8 Validation
- All code must adhere to PEP 8 style guidelines.
- It uses the `pycodestyle` tool to validate the code.



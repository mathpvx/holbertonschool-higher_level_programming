#!/usr/bin/python3
def read_file(filename=""):
    """ Reads the contents of a text file and prints it to the console."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data, end='')

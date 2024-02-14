#!/usr/bin/python3
def read_file(filename="my_file_0.txt"):
    """ Reads the contents of a text file and prints it to the console."""
    with open('my_file_0.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        print(data, end='')

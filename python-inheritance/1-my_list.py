#!/usr/bin/python3
class MyList(list):
    """Subclass that inherits from list built in python class """

    def print_sorted(self):
        """ Sorts the list in ascending order and prints it """
        sorted_list = sorted(self)
        print(sorted_list)

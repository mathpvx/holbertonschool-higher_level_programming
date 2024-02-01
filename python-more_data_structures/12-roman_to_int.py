#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    sum = 0
    nb_i = 0
    unit_sum = 0
    for char in roman_string:
        if char == 'M':
            sum += 1000
        if char == 'D':
            sum += 500
        if char == 'C':
            sum += 100
        if char == 'L':
            sum += 50
        if char == 'X':
            if nb_i == 0:
                sum += 10
            else:
                sum += 10 - nb_i
                nb_i = 0
        if char == 'V':
            if nb_i == 0:
                sum += 5
            else:
                sum += 5 - nb_i
                nb_i = 0
        if char == 'I':
            nb_i += 1
    if nb_i == 0:
        return sum
    else:
        return sum + nb_i

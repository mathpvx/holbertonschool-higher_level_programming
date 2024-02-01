#!/usr/bin/python3
def best_score(a_dictionary):
    dat_score = 0
    if a_dictionary is None:
        return None
    else:
        for key in a_dictionary:
            if a_dictionary[key] > dat_score:
                dat_score = a_dictionary[key]
                best_student = key
    return best_student

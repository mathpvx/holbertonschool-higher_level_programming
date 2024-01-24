#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = number % 10
neg_last_d = number % -10
if number > 0 and last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
elif number > 0 and last_d < 6 and last_d > 0:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
elif number < 0 and last_d < 6 and last_d > 0:
    print(f"Last digit of {number} is {neg_last_d*-1} and is less than 6 and not 0")
elif number >= 0 and last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")

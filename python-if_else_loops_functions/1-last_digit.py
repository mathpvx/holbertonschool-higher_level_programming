#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_d = -number % 10
else:
    last_d = number % 10

if last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
elif 0 < last_d < 6:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")

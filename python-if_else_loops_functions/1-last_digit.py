#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_d = abs(number) % 10
print(f"Last digit of {number} is {last_d} and is", end=' ')

if last_d > 5:
    print("greater than 5")
elif last_d == 0:
    print("0")
else:
    print("less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lt = abs(number) % 10
if number < 0:
    lt = -lt
print("Last digit of {} is {} and is ".format(number, lt), end="")
if lt > 5:
    print("greater than 5")
elif lt == 0:
    print("0")
elif lt < 6 and lt != 0:
    print("less than 6 and not 0")

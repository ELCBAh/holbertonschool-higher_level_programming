#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = abs(number) % 10 * -1
else:
    last = number % 10
if last == 0:
    print("Last digit of {0} is {1} and is 0".format(number, last))
elif last > 5:
    prGr5 = "Last digit of {0} is {1} and is greater than 5"
    print(prGr5.format(number, last))
else:
    prLs6n0 = "Last digit of {0} is {1} and is less than 6 and not 0"
    print(prLs6n0.format(number, last))

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit = -lastDigit

output = "Last digit of %d is %d and is" %(number, lastDigit)

if lastDigit > 5:
    print(output, "greater than 5")
elif lastDigit == 0:
    print(output, "0")
elif lastDigit < 6 and lastDigit != 0:
    print(output, "less than 6 and not 0")

#!/usr/bin/python3
import sys

argCount = len(sys.argv)
total = 0

for i in range(1, argCount):
    total += int(sys.argv[i])

print(total)

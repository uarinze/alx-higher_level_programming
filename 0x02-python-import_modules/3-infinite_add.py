#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argCount = len(sys.argv)
    total = 0

    for i in range(1, argCount):
        total += int(sys.argv[i])

    print(total)

#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argCount = len(sys.argv) - 1
    if (argCount) == 0:
        print("{:d} {:s}.".format(argCount, "arguments"))
    elif (argCount) == 1:
        print("{:d} {:s}:".format(argCount, "argument"))
    else:
        print("{:d} {:s}:".format(argCount, "arguments"))
    for i in range(argCount):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))

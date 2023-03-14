#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1
    import sys

    add = calculator_1.add
    sub = calculator_1.sub
    mul = calculator_1.mul
    div = calculator_1.div

    argCount = len(sys.argv) - 1

    if argCount != 3:
        print("{}".format("Usage: ./100-calculator.py <a> <operator> <b>"))
        sys.exit(1)

    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))
    elif operator == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a,b)))
    elif operator == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a,b)))
    elif operator == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a,b)))
    else:
        print("{:s}".format("Unknown operator. Available operators: +, -, * and /"))
        sys.exit(1)

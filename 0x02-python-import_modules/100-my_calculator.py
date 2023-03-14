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

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        print("{} {} {} = {}".format(a, sys.argv[2], b, operators[sys.argv[2]](a, b)))

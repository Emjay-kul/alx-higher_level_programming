#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = ['+', '-', '*', '/', '%']
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if (len(sys.argv) - 1) == 3:
        if sys.argv[2] not in op:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        elif sys.argv[2] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            print("0")
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            print("0")
        elif sys.argv[2] == '%':
            print("{} % {} = {}".format(a, b, mul(a, b)))
            print("0")
        elif sys.argv[2] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
            print("0")
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            print("0")

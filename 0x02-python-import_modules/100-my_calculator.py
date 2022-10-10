#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import a, b, add, sub, mul, div

    op = ['+', '-', '*', '/']

    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("1")
    else:
        if sys.argv[2] not in op:
            print("Unknown operator. Available operators: +, -, * and /")
            print("1")
        elif sys.argv[2] == '+':
            print("{} + {} = {}".format(int(a), int(b), add(a, b)))
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(int(a), int(b), sub(a, b)))
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(int(a), int(b), mul(a, b)))
        elif sys.argv[2] == '/':
            print("{} / {} = {}".format(int(a), int(b), div(a, b)))

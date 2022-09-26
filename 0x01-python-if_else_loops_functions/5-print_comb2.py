#!/usr/bin/python3
for numbers in range(100):
    print("{:02d}".format(numbers), end= '\n' if num == 99 else '')
    if numbers < 99:
        print(", ", end='')

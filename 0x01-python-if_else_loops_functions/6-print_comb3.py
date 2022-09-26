#!/usr/bin/python3
for num in range(9):
    for var in range(num + 1, 10):
        print("{:d}{:d}".format(num, var), end='\n' if numbers == 8 else ', ')

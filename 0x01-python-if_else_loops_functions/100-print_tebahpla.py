#!/usr/bin/python3
for var in range(ord('z'), ord('a') - 1, -1):
    if var % 2 == 0:
        diff = 0
    else:
        diff = 32
    print("{}".format(chr(var - diff)), end='')

#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 == 0:
        c = i + 32
    else:
        c = i
    print("{:c}".format(c), end="")

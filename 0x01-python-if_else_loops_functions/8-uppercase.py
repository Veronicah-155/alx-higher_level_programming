#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ascii_code = ord(str[i])
        if ascii_code >= 97 and ascii_code <= 122:
            ascii_code = ascii_code - 32
        print("{}".format(chr(ascii_code)), end='')
    print()

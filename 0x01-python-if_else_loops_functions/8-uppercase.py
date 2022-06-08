#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if(ord(c) >= 97 and ord(c) <= 122):
            value = 32
        else:
            value = 0
        print("{:c}".format(ord(c) - value), end="")
    print()

#!/usr/bin/python3
for i in range(97, 123):
    if (i % 2 != 0):
        i -= 32
    c = chr(i)
    print(c, end="")

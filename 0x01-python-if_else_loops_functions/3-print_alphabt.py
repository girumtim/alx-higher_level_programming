#!/usr/bin/python3
for i in range(97, 123):
    c = chr(i)
    if ((c != 'e') and (c != 'q')):
        print("{}".format(c), end="")

#!/usr/bin/python3
def print_last_digit(number):
    i = number % 10
    if (i < 0):
        i = i * -1
    return (i)

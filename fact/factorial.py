#!/usr/bin/env python3
"""
For loops and range()

Author: mjslawson
"""
def main():
    """ Main program """
    x_each = int(input("Enter a number: "))
    f_var = 1
    for i in range(1, x_each+1):
        f_var = f_var * i
    print(str(x_each) + '! = ' + str(f_var))

main()

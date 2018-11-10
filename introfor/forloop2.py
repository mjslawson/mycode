#!/usr/bin/env python3

"""
For looping pt. 2

Author: mjslawson
"""

def main():
    """ Main Program """
    vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'alta3', 'zach', 'stuart']
    approved_vendors = ['cisco', 'juniper', 'big_ip']
    for x_each in vendors:
        print("\nThe vendors is " + x_each, end="")
        if x_each not in approved_vendors:
            print(" - NOT AN APPROVED VENDOR!", end="")
    print("\nOur loop has ended.")

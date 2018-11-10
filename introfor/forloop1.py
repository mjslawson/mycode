#!/usr/bin/env python3

"""
Loop intro

Author: mjslawson
"""
def main():
    """ Main Program """
    vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista']
    for x_each in vendors:
        print("The vendor is:" + x_each)
    print("\nOur loop has ended.")

main()

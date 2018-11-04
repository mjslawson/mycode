#!/usr/bin/env python3

"""
Author: mjslawson

This program prints video settings based on user-provided Mbps
"""

def is_number(var):
    """Checks Numbers"""
    try:
        float(var)
        return True
    except ValueError:
        return False

def main():
    """Main Program"""
    message = 'The movie is about to begin, we recommend ' # creates initial message
    print('What is your connection speed in Mbps?') # asks for Mbps
    connection = input() # gets user Mbps input
    if is_number(connection):
        if connection >= 25:
            message = message + 'setting video to 4k.'
        elif connection >= 5:
            message = message + 'setting video to 1080p.'
        elif connection >= 2:
            message = message + 'setting video to 720p.'
        else:
            message = message + 'finding another access network.'
            print(message) # prints message
    else:
        print("Sorry that is not a number") # not a number

main()

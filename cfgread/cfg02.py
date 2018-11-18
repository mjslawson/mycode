#!/usr/bin/env python3
## Ask user for filename ##
filename = input('Please enter the filename:')

## create file object in "r"ead mode
configfile = open(filename, 'r')

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'
print(configlist)

## Count how many lines ##
print(len(configlist))

## Always close your file
configfile.close()

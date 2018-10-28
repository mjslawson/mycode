#!/usr/bin/env python3

#User input
hostname = input('Please enter the hostname:')

if hostname.lower() == 'mtg': # uses lower() for case-insensitive check
	print("The hostname was found to be " + hostname) # displays hostname notification
	print("Hostname matches expected config.") # displays hostname confirmation

print("Exiting the script") # exiting script notification
#!/usr/bin/env python3

"""
Author: mjslawson

This program prompts user to apply an IP address

"""

import socket

def is_valid_ipv4_address(address):
    """ Checks if valid ipv4 """
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    """ Checks if valid ipv6 """
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True

def main():
    """ Main Program """
    ipchk = input('Apply an IP address: ') # this line now prompts the user for input

    if ipchk == '192.168.70.1': # if a match on '192.168.70.1'
        print('Looks like the IP address of the Gateway was set: ' + ipchk + ' Not recommended.')
    elif (is_valid_ipv4_address(ipchk)) or (is_valid_ipv6_address(ipchk)):
        print('Looks like the IP address was set: ' + ipchk)
    elif ipchk:
        print('You did not provide valid IP address input.') # indented under elseif
    else: # if data is NOT provided
        print('You did not provide input.') # indented under else

main()

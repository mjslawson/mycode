#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def get_adapter_ip(adapter_name):
    try:
        ip_address = (netifaces.ifaddresses(adapter_name)[netifaces.AF_INET])[0]['addr']
        return ip_address
    except:
        return False


def get_adapter_mac(adapter_name):
    try:
        mac_address = (netifaces.ifaddresses(adapter_name)[netifaces.AF_LINK])[0]['addr']
        return mac_address
    except:
        return False


adapter_name = input('Please enter the adapter name: ')

adapter_ip = get_adapter_ip(adapter_name)
if (adapter_ip):
    print( 'Adapter IP Address: ' + adapter_ip )

adapter_mac = get_adapter_mac(adapter_name)
if (adapter_mac):
    print( 'Adapter MAC Address: ' + adapter_mac )

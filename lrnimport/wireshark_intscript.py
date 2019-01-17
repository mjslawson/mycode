#!/usr/bin/env python3
import subprocess
#ls_output = subprocess.check_output(['ls'])
#print(ls_output)
subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface for Wireshark, like, ens3: ")
#subprocess.call(["ip", "addr", "show", "dev", interface])
#subprocess.call(["ip", "route", "show", "dev", interface])
subprocess.call(["wireshark", "-i", interface, "-k"])


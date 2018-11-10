#!/usr/bin/env python3
"""
Parsing Log Files

Author: mjslawson
"""

def main():
    """ Main Program """
    import re
    loginfail = 0
    loginsuccess = 0
    ip_list = []
    keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi', 'r')
    keystone_file_lines = keystone_file.readlines()
    for i_each in range(len(keystone_file_lines)):
        if "- - - - -] Authorization failed" in keystone_file_lines[i_each]:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            user_ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', keystone_file_lines[i_each])
            ip_list.extend(user_ip)
        elif " - - - - -] Loaded 2 encryption keys" in keystone_file_lines[i_each]:
            loginsuccess += 1
    print('The number of failed log in attempts is ' + str(loginfail))
    print('Failed login attempts from: ' + str(ip_list))
    print('The number of successful log in attempts is ' + str(loginsuccess))

main()

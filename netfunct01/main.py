#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here
        print('\n', end='') # adds a new line after commands

def devicereboot(device_ips): #deviceip == list
    for each_ip in device_ips:
        print('Connecting to... ' + each_ip ) # prints connecting to message
        print('REBOOTING NOW!') # prints rebooting message
        print('\n', end='')

def getdataset(filename):
    data = {}
    dataset_file = open(filename, 'r')
    dataset_lines = dataset_file.readlines()
    for i_each in range(len(dataset_lines)):
        if i_each % 3 == 0 and i_each < len(dataset_lines):
            # Get ip address, from every 3rd line
            ip_address = dataset_lines[i_each].strip('\n')

            # Get commands subsequent to ip address
            cmd_01 = dataset_lines[i_each+1]
            cmd_02 = dataset_lines[i_each+2]

            # add each key and value (list)
            data[ip_address] = []
            data[ip_address].append(cmd_01.strip('\n'))
            data[ip_address].append(cmd_02.strip('\n'))
        elif i_each == len(dataset_lines):
            # that's all folks
            print('Dataset error. Check dataset file: ' + filename)
    return data

### Start our script
#work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

work2do = getdataset('dataset.cfg')

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found\n") # replace with function call that reads in data from file

## run
commandpush(work2do) # call function to push commands to devices

## run device reboot
devicereboot(work2do.keys()) # call function to reboot devices

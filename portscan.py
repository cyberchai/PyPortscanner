import socket
import subprocess
import sys
import argparse
import time
import random
from datetime import datetime


'''
Chaira Harder
Network Security Port Scanner Project

resources:

1. https://youtu.be/t9EX2RAUoTU
2. https://docs.python.org/3/library/argparse.html
3. https://youtu.be/XGFDXGyd7Uw
4. https://youtu.be/oykmzRXSass
5. https://youtu.be/FbEJN8FsJ9U
'''

# FUNCTIONS

# checks if a port is open
def is_port_open(port, target_ip, scanning_protocol, scanning_option):
    s = scanning_function(scanning_protocol, scanning_option)
    result = s.connect_ex((target_ip, port))
    s.close()
    return result == 0


# PROGRAM

# get operating modes
parser = argparse.ArgumentParser(description='port scanner options')
parser.add_argument('ip', metavar='IP', type=str, help='specify IP address of the target')
parser.add_argument('-m', '--mode', metavar='MODE', type=str, choices=['normal', 'syn', 'fin'], default='normal', help='scanning mode')
parser.add_argument('-o', '--order', metavar='ORDER', type=str, choices=['order', 'random'], default='order', help='scanning order')
parser.add_argument('-p', '--ports', metavar='PORTS', type=str, choices=['all', 'known'], default='all', help='set of ports to scan')
args = parser.parse_args()

# set up arg modes. Known or all ports:
target_ip = args.ip
if args.ports == 'all':
    port_range = range(0, 65536)
else:
    port_range = range(0, 1024)

# define scanning mode based on args:
if args.mode == 'syn':
    scanning_function = socket.SOCK_RAW
    scanning_protocol = socket.IPPROTO_TCP
    scanning_option = socket.TCP_SYN
elif args.mode == 'fin':
    scanning_function = socket.SOCK_RAW
    scanning_protocol = socket.IPPROTO_TCP
    scanning_option = socket.TCP_FIN
else:
    scanning_function = socket.socket
    scanning_protocol = socket.AF_INET
    scanning_option = socket.SOCK_STREAM

# get scanning order based on args:
if args.order == 'random':
    port_range = random.sample(port_range, len(port_range))


# blank screen
subprocess.call('clear', shell=True)

# Get target_ip (original version)
# remoteServer = raw_input("Enter a remote host to scan: ")
# remoteServer = input("Enter a host to scan: ")
# remoteServerIP = socket.gethostbyname(remoteServer)
# numOpenPorts = 0


# print a banner with information on which host we are about to scan
print("_"*60 + "\n")
print("Please wait, scanning remote host", target_ip)
print("Scan started at \t {} EST.".format(datetime.now()))
print("_"*60 + "\n")

# check & record date and time the scan was started
t1 = datetime.now()

print("PORT \t (SERVICE) \t\t STATE")
# scanning
open_ports = []
closed_ports = []

for port in port_range:
    if is_port_open(port, target_ip, scanning_protocol, scanning_option):
        open_ports.append(port)
    else:
        closed_ports.append(port)

# Using range function specify ports
# Also error handling:
# try:
#     for port in range(1, 5000):
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         result = sock.connect_ex((remoteServerIP, port))
#         if result == 0:
#             print("Port {}:\t Open".format(port))
#             numOpenPorts += 1
#         sock.close()

# except KeyboardInterrupt:
#     print("You exited the program. (Ctrl+C in terminal mode)")
#     sys.exit()

# except socket.gaierror:
#     print("Hostname could not be resolved. Exiting.")
#     sys.exit()

# except socket.error:
#     print("Couldn't connect to server.")
#     sys.exit()


# Checking time again
t2 = datetime.now()

# Calculate the difference in time to know how long the scan took
total = t2 - t1


# printing results
for port in open_ports:
    try:
        # print('{} ({}) \t open'.format(port, socket.getservbyport(port)))
        print(port, ' '*(7-len(str(port))), '({})'.format(socket.getservbyport(port)), ' '*(20-len(str(socket.getservbyport(port)))) ,'open')
        # print('{}{}({}) \t open'.format(port, 30-(len(str(port))-len(str(socket.getservbyport(port))))*' ' ,socket.getservbyport(port)))
    except:
        # print('Port {} ({}) is open'.format(port, socket.connect((host, port, socket.SOCK_STREAM))))
        # print('{} ({}) \t open'.format(port, "service not found"))
        print(port, ' '*(7-len(str(port))), '({})'.format("service not found"),  '\t open')

# printing info on the screen
print("\nScan done! Scanning Completed in: ", str(total), "seconds.")
if len(open_ports) == 1:
    print("There was {} open port.".format(len(open_ports)))
else:
    print("There were {} open ports.".format(len(open_ports)))
print("Not shown: {} closed ports.".format(len(closed_ports)))

"""
end of program
"""
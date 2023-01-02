#!/bin/python3
import sys #Allow us to enter command line arguments, among other things
import socket #Allows ip-port connection
from datetime import datetime
def new_line():
	print("\n\n")
	
#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])#Translates a host name to IPV4.
else:
	print("Invalid amount of Arguments.")
	print("Syntax: Python3 scanner.py <ip>")
	sys.exit()
new_line()
#Adding a pretty banner
print("*" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("*" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET is ipV4 and SOCK_STREAM is your port.
		socket.setdefaulttimeout(1) #This is a float(millisecond)
		result = s.connect_ex((target,port))# Returns errokr indicator 
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\Exiting program.")
	sys.exit()
except socket.gaierror:#We cannot connect to the socket.
	print("Hostnamem could not be solved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to the server")
	sys.exit()
	 
		

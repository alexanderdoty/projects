import socket
import subprocess
import sys
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Screen clearing component that adapts to MacOS, as Mac is what I am using.
os.system('cls' if os.name == 'nt' else 'clear')

# subprocess.call('cls', shell=True)

# Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Letting the user choose the port range.
start_port = int(input("Starting port: "))
end_port = int(input("Ending port: "))

# Print a nice banner with information on which host we are about to scan
print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scan all ports
# between 1 and 1024)

# We also put in some error handling for catching errors
try:
	for port in range(start_port, end_port + 1):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print ("Port {}: Open".format(port))
		sock.close()
except KeyboardInterrupt:
		print("You pressed Ctrl+C")
		sys.exit()

except socket.gaierror:
		print ('Hostname could not be resolved. Exiting')
		sys.exit()

except socket.error:
		print("Couldn't connect to server")
		sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to the screen
print ('Scanning Completed in: ', total)


import socket
import sys
from datetime import datetime

# Input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Banner information
print("-" * 60)
print("Scanning remote host, please wait ", remoteServerIP)
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port{}: Open".format(port))
            s.close()
except KeyboardInterrupt:
    print("Interrupted")
    sys.exit()

except socket.error:
    print("Could not connect to server")
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print("Scanning completed in ", total)

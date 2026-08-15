# Basic Workflow
#
# Target Hostname
# Connect to TCP Port
# Send appropriate Probe
# Recieve a response
# Print the service banner


import socket

# Ask the user for the target
target = input("Enter the target IP or hostname: ")

# Ask which port to connect to
port = int(input("Enter port: "))

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Don't let the program hang forever
sock.settimeout(3)

try:
    # Connect to the target
    print(f"\n[*] Connecting to {target}:{port}...")
    sock.connect((target, port))

    print("[+] Connection established!")

    # Try to recieve a banner
    banner = sock.recv(1024)

    # Convert the bytes we recieved into text
    print("\n[+] Banner:")
    print(banner.decode("utf-8", errors="replace"))

except socket.timeout:
    print("[-] Connection timed out.")

except ConnectionRefusedError:
    print("[-] Connection Refused.")

except socket.gaierror:
    print("[-] Could not resolve the hostname.")

except Exception as e:
    printf(f"[-] Error: {e}")

finally:
    # Always close the socket
    sock.close()
    print("\n[*] Connection closed.")

                

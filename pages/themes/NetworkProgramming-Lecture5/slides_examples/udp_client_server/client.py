import socket

# open client socket:
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data to specific address:
client.sendto(b'Hello Server',('127.0.0.1', 9999))

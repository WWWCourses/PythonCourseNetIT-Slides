import socket

# open and bind UDP server socket:
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 9999))
print('Serve is listening on 127.0.0.1:9999')

# receive data from a client, max 1024 bytes:
msg,address = server.recvfrom(1024)
print(f"Received from {address}: {msg.decode('utf-8')}")
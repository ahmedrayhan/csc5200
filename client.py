import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.128.0.2',10005)
print("Connecting to .....", server_address)
sock.connect(server_address)
print("Yay! connected to....", server_address)
data = b"Hell0o server!"
print("Sending message....", data)
sock.sendall(data)
sock.close()

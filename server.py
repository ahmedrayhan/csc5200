import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address_obj = ('10.128.0.2',10005)
print("Address = ", server_address_obj)
sock.bind(server_address_obj)

sock.listen(1)

print("Waiting to hear from a client...........")
connection_object, client_address = sock.accept()

print("Yay! heard from a client, address is: ", client_address)

with connection_object as conn_obj:
    try:
        data_from_client = conn_obj.recv(1024)
        print("Data = ", data_from_client.decode())
    except KeyboardInterrup: #CTRL+^C
        sock.close()

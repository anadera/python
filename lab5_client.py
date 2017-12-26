import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 9090))
client_socket.send(1000)
data = client_socket.recv(1024)
client_socket.close()
print(data)
import socket

server_socket = socket.socket()
server_socket.bind(('', 9090))
server_socket.listen(1)
connection, address = server_socket.accept()
print ('connected', address)
while True:
    data = connection.recv(1024)
    if not data:
        break
    connection.send(data.upper())
connection.close()
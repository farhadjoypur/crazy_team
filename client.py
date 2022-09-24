import socket

HOST = '192.168.110.239'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
client.send('1090'.encode('utf-8'))
message = client.recv(1024).decode('utf-8')
print(f'message from server {message}')
client.close()
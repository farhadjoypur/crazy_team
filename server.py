import socket
import random

HOST = '192.168.120.239'
PORT = 9090
init = 0
ticket_id = 10000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(4)

while True:
    print("bangla bhai")
    comSocket, address = server.accept()
    print(f'Connected to {address}')
    message = comSocket.recv(1024).decode('utf-8')
    numbr = int(message)
    print(numbr)
    result = []
    for i in range(1, numbr):
        if numbr % i == 0:
            result.append(i)
    # print(f'Message from the client was {ticket_id}')
    comSocket.send(f"Got your message {result}".encode('utf-8'))
    ticket_id = ticket_id + random.randint(0,9)
    init = init + 1
    print(f"total number of connection {init}")
    comSocket.close()
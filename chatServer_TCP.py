# server.py
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('Server is ready to receive')

connectionSocket, addr = serverSocket.accept()

while True:
    message = connectionSocket.recv(1024).decode()
    if message == 'bye':
        print("Client đã thoát.")
        break
    print(f"Client: {message}")

    reply = input('Bạn (server): ')
    connectionSocket.send(reply.encode())
    if reply == 'bye':
        print("Đã thoát.")
        break

connectionSocket.close()

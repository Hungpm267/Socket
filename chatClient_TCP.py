# client.py
from socket import *

serverName = 'localhost'  # hoặc IP server nếu khác máy
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = input('Bạn (client): ')
    clientSocket.send(message.encode())
    if message == 'bye':
        print("Đã thoát.")
        break

    reply = clientSocket.recv(1024).decode()
    if reply == 'bye':
        print("Server đã thoát.")
        break
    print(f"Server: {reply}")

clientSocket.close()

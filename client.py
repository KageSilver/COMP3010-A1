#------------------------------------------
# NAME		: Tara Boulanger
# STUDENT NUMBER	: 7922331
# COURSE		: COMP 3010
# INSTRUCTOR	: Robert Guderian
# ASSIGNMENT	: Assignment 1
# 
# REMARKS: This is a basic creation of a multi-threaded
#       client.
#
#------------------------------------------

import socket
import time

serverHost = 'DESKTOP-7US2QRP' #replace aviary with the machine the server is running on
serverPort = 8680

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.bind((socket.gethostname(), 0))


hostname = socket.gethostname()
print("listening on interface " + hostname)
port = clientSocket.getsockname()[1]
print('listening on port:', port)


# send a message, listen for it
try:
    clientSocket.connect((serverHost, serverPort))
    clientSocket.sendall('hello world'.encode())
    data = clientSocket.recv(1024)
    print('Received: ', data.decode('utf-8'))
except Exception as e:
    print(e)

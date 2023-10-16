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
import json

serverHost = 'aviary.cs.umanitoba.ca' #replace aviary with the machine the server is running on
serverPort = 8680

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.bind((socket.gethostname(), 0))


hostname = socket.gethostname()
print("listening on interface " + hostname)
port = clientSocket.getsockname()[1]
print('listening on port:', port)

with clientSocket:
    # send a message, listen for it
    try:
        clientSocket.connect((serverHost, serverPort))
        clientSocket.sendall('hello world'.encode())
        data = clientSocket.recv(2048)
        print('Received', data.decode('utf-8'))
    except:
        print("Could not connect socket")

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

serverHost = 'cs.umanitoba.ca'
serverPort = 8680

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSocket.bind((socket.gethostname(), 0))


hostname = socket.gethostname()
print("listening on interface " + hostname)
port = clientSocket.getsockname()[1]
print('listening on port:', port)

with clientSocket:
    # send a message, listen for it
    clientSocket.sendto("hello".encode(), (serverHost, serverPort))
    data, addr  = clientSocket.recvfrom(2048)
    print(data.decode('utf-8)'))
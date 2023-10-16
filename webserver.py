#!/usr/bin/python3

#------------------------------------------
# NAME		: Tara Boulanger
# STUDENT NUMBER	: 7922331
# COURSE		: COMP 3010
# INSTRUCTOR	: Robert Guderian
# ASSIGNMENT	: Assignment 1
# 
# REMARKS: This is a basic creation of a multi-threaded
#       web server.
#
#------------------------------------------

# Imports
import socket
import sys
import os
import re
import time
import threading
import pytz
import datetime

#Aetting the last updated timestamp
lastUpdatedPattern = "%a, %d %b %Y %H:%M:%S %Z"
modifiedTimestamp = os.path.getmtime("webserver.py")
# hardcoding Winnipeg for simplicity
modifiedTime = datetime.datetime.fromtimestamp(modifiedTimestamp, tz=pytz.timezone("America/Winnipeg"))
forHeader = modifiedTime.strftime(lastUpdatedPattern)


HOST = 'webserver.py'                 # Symbolic name meaning all available interfaces

# parsing the command line arguments
if ( len(sys.argv) == 4 ) :
    PORT = sys.argv[1]
    SITE = open(sys.argv[2], "r")
    ifMulti = sys.argv[3]
elif ( len(sys.argv) == 3 ) :
    PORT = sys.argv[1]
    SITE = open(sys.argv[2], "r")
    ifMulti = False
else :
    raise Exception ( "Invalid number of arguments, please use the format:\n"
                     + " \"python3 webserver.py 8000 files-distribution -m\"\n"
                     + " either with, or without the \"-m\".")

#Will need to contain all of the information passed in by the command line,
#with the appropriate values included
head = """HTTP/1.1 200 OK
Content-Length: {}
Content-Type: text/html
Last-Modified:
Server: Faerun
"""


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
hostname = socket.gethostname()
print("listening on interface " + hostname)
# This accepts a tuple...
serversocket.bind((HOST, PORT))
# become a server socket
serversocket.listen()


# Keep running the server until we decide to kill it
while True:
    conn, addr = serversocket.accept() #client socket
    with conn:
        try:
            conn.settimeout(5) #Giving them a chance to connect before cleaning
            conn.sendall(head) #sending what is contained within the head file
            print('Connected by', addr)
            data = conn.recv(1024)
            #Decoding the message received from the client (would be to decide which site we're displaying)
            print("heard:")
            print(data.decode('UTF-8'))
            strData = data.decode('UTF-8')

            # Do some work with the data that we received from the client
            randomBoolean = True
            try:
                print("yes")
            except:
                # it's fine....
                print("No, it isn't fine" + strData)
                


            # just say something
            if randomBoolean:
                conn.sendall(b'You did it!')
            elif strData.lower().find("please") >= 0:
                conn.sendall(b'You said please')
            else:
                conn.sendall(b'try again')

        except Exception as e:
            print(e)
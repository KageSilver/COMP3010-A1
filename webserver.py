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


HOST = ''                 # Symbolic name meaning all available interfaces

# parsing the command line arguments
if ( len(sys.argv) == 4 ) :
    PORT = int(sys.argv[1])
    SITE = sys.argv[2]
    ifMulti = sys.argv[3]
elif ( len(sys.argv) == 3 ) :
    PORT = int(sys.argv[1])
    SITE = sys.argv[2]
    ifMulti = False
else :
    raise Exception ( "Invalid number of arguments, please use the format:\n"
                     + " \"python3 webserver.py 8680 files-distribution -m\"\n"
                     + " either with, or without the \"-m\".")

#Will need to contain all of the information passed in by the command line,
#with the appropriate values included
head = ("HTTP/1.1 200 OK\n"
"Content-Length: {}\n"
"Content-Type: text/html\n"
"Last-Modified:"+forHeader+
"\nServer: Faerun\n\n")


# Do some work with the SITE constant to actually make it something the
# client can view. Need to go into the directory and open it.
if (SITE == "site1") :
    SITE = "./site1"
elif (SITE == "site2") :
    SITE = "./site2"
elif (SITE == "site3-stretch") :
    SITE = "./site3-stretch"
else :
    print ("invalid file name provided")

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
hostname = socket.gethostname()
print("listening on interface " + hostname)
print('listening on port:', PORT)
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
            conn.sendall(head.encode()) #sending what is contained within the head file (only if they request it)
            print('Connected by', addr)
            data = conn.recv(1024)
            #Decoding the message received from the client (would be to decide which site we're displaying)
            print("heard:")
            print(data.decode('UTF-8'))
            strData = data.decode('UTF-8')

            # Do some work with the data that we received from the client (get and head)
            randomBoolean = True
            try:
                print("yes")
            except:
                # it's fine....
                print("No, it isn't fine" + strData)
                

        except Exception as e:
            print(e)
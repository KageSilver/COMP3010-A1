#!/usr/bin/python3

#------------------------------------------
# NAME		: Tara Boulanger
# STUDENT NUMBER	: 7922331
# COURSE		: COMP 3010
# INSTRUCTOR	: Robert Guderian
# ASSIGNMENT	: Assignment 1 Part 1
# 
# REMARKS: This is a basic creation of a multi-threaded
#       web server.
#
#------------------------------------------

# Imports needed
import socket
import sys
import os
import threading
import pytz
import datetime


HOST = ''                 # Symbolic name meaning all available interfaces
# PORT and SITE also exist, with port being the number, site being the one we'll serve

# HTTP responses
BAD_REQUEST = "400 Bad Request"
PAGE_NOT_FOUND = "404 File Not Found"
OK = "200 OK"
SERVER_MESSED_UP = "500 Internal Server Error"

MIMETYPES = {
    "text/html": ".html",
    "text/plain": ".txt",
    "text/javascript": ".js",
    "image/jpeg": ".jpeg",
    "image/jpg": ".jpg",
    "image/png": ".png",
    "application/json": ".json",
    "image/vnd.microsoft.icon": ".ico",
    "application/xml": ".xml",
}



# Contains the format for a response header to the client's requests
responseHeader = """HTTP/1.1 {0}
Content-Length: {1}
Content-Type: {2}
Last-Modified: {3}
Server: Faerun\n\n"""


# Parsing the command line arguments
if ( len(sys.argv) == 4 ) :
    PORT = int(sys.argv[1])
    SITE = sys.argv[2]
    if ( sys.argv[3=="-m"] ) :
        ifMulti = sys.argv[3]   # Will be multi-threaded if given -m flag
    else :
        # Can only be given the -m flag
        raise Exception ( "Invalid flag given. If you want to run the server in"
                         + "multi-threaded mode, please pass the \"-m\" flag like so: \n"
                         + " \"python3 webserver.py 8680 files-distribution -m\".")
elif ( len(sys.argv) == 3 ) :
    PORT = int(sys.argv[1])
    SITE = sys.argv[2]
    ifMulti = False
else :
    raise Exception ( "Invalid number of arguments, please use the format:\n"
                     + " \"python3 webserver.py 8680 files-distribution -m\"\n"
                     + " either with, or without the \"-m\".")


# Change the SITE constant to be the path pointing to the site
if ( (SITE != "site1") & (SITE !="site2") & (SITE !="site3-stretch") ) :
    raise Exception ("Invalid directory name provided. Please enter site1 or site2.")

# Getting the last updated timestamp
lastUpdatedPattern = "%a, %d %b %Y %H:%M:%S %Z"
modifiedTimestamp = os.path.getmtime("webserver.py")
# hardcoding Winnipeg for simplicity
modifiedTime = datetime.datetime.fromtimestamp(modifiedTimestamp, tz=pytz.timezone("America/Winnipeg"))
lastModified = modifiedTime.strftime(lastUpdatedPattern)

# bind the socket to a public host, and a well-known port
hostName = socket.gethostname()
print("listening on interface " + hostName)
print('listening on port:', PORT)


# Create an INET, STREAMing socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# This accepts a tuple...
serverSocket.bind((HOST, PORT))
# Become a server socket
serverSocket.listen()

# Function to do something with the given client thread and socket
def handleThread(clientConnection:socket) :
    with clientConnection:
        try:
            #print('Connected by', clientAddress) # For debugging
            clientRequest = clientConnection.recv(1024)
            #Decoding the message received from the client
            requestString = clientRequest.decode('utf-8')

            # HTTP requests will always have the same format (design by contract)
            requestTokens = requestString.split()

            requestMethod = requestTokens[0]
            requestPath = "./"+SITE+requestTokens[1]

            # Checking if the client made either a GET or HEAD request, anything else returns
            # a 400 error
            if ( requestMethod == "GET" ) :
                # Make sure that the client sent an actual path, if they didn't, send 404
                if ( os.path.isfile(requestPath) ) :
                    #print("Read Path: " + requestPath) #for debugging
                    # Grabbing the body of what they requested
                    body = open(requestPath, mode="rb").read()
                    # Setting the response header
                    fileSize = os.path.getsize(requestPath)
                    fileType = os.path.splitext(requestPath)
                    # Make sure we can access the type of the file
                    if ( len(fileType)<=2 ) :
                        # Now check if that mimetype is supported
                        print (fileType[1])
                        print(MIMETYPES.values())
                        print(fileType[1] in MIMETYPES.values())
                        if fileType[1] in MIMETYPES.values() :
                            header = responseHeader.format(OK,fileSize,fileType[1],lastModified)
                            clientConnection.sendall(header.encode()) # Send the header
                            # The body is already in bytes
                            clientConnection.sendall(body)  # Then send the body
                        else :
                            header = header = responseHeader.format(SERVER_MESSED_UP,'','',lastModified)
                            clientConnection.sendall(header.encode()) # Send the header
                    else : 
                        header = responseHeader.format(SERVER_MESSED_UP,'','',lastModified)
                        clientConnection.sendall(header.encode()) # Send the header

                else :
                    #print("Did not read path: " + requestPath) # For debugging
                    header = responseHeader.format(PAGE_NOT_FOUND,'','',lastModified)
                    clientConnection.sendall(header.encode())

            elif ( requestMethod == "HEAD" ) :
                responseHeader.format(OK,'','',lastModified)
                clientConnection.sendall(responseHeader.encode())
            else :
                clientConnection.sendall(BAD_REQUEST.encode())

        # Some sort of error occurred, need to catch it
        except Exception as e :
            print("Something happened in client sending. ")
            print(e)


# Used to track amount of threads running at a time
hitCounts = 0

# Keep running the server until we stop running it
while True:
    try :
        clientConnection, clientAddress = serverSocket.accept() # Client socket
        hitCounts += 1
        clientConnection.settimeout(60) # Giving them a chance to do stuff before cleaning
        # Multi-threaded server
        if ( ifMulti ) :
            threading.Thread(target=handleThread,args=(clientConnection,)).start()
        # Single-threaded server
        else :
            threading.Thread(target=handleThread,args=(clientConnection,)).run()

        # Show how many threads are running at a time
        print("Running {} threads.".format(threading.active_count())) 
    except Exception as e :
        print("Something went wrong! ")
        print(e)
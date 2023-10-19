#!/usr/bin/python3

#------------------------------------------
# NAME		: Tara Boulanger
# STUDENT NUMBER	: 7922331
# COURSE		: COMP 3010
# INSTRUCTOR	: Robert Guderian
# ASSIGNMENT	: Assignment 1 Part 2
# FILE NAME     : testingServer.py
# 
# REMARKS: This is a multi-threaded client
#   that is used to test the capabilities of
#   the server created in Part 1.
#
#------------------------------------------

import requests
import threading
import time


def makeRequest(url) :
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")

# Server's url to connect to. Change it for whatever aviary machine it's running on
url = "http://localhost:8680/files-distribution/images.html"

# For all of the threads I'll be making
threads = []

timeStart = time.time()

for i in range(100) :
    thread = threading.Thread(target=makeRequest, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads :
    thread.join()

timeEnd = time.time()

print("Total amount of time: ", timeEnd-timeStart)
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

# imports required to run the program
import requests
import threading
import time
import csv


# URL of the website I'm testing, either tested on aviary or on
# my local machine
url = "http://grouse.cs.umanitoba.ca:8680/files-distribution/images.html"
#url = "http://localhost:8680/files-distribution/images.html"

# For all of the threads I'll be making
threads = []

timeStart = time.time()

# Function to actually make the request for the desired url of the webserver
def makeRequest(url) :
    response = requests.get(url)
    #for debugging
    print(f"Response from {url}: {response.status_code}")

# Make 100 different threads
for i in range(100) :
    thread = threading.Thread(target=makeRequest, args=(url,))
    thread.start()
    threads.append(thread)

# Run all threads concurrently
for thread in threads :
    thread.join()

timeEnd = time.time()

# Write to the specified csv file depending on which server is being run
#csvFile = open("./summarySingle.csv","a",newline='')
csvFile = open("./summaryMulti.csv","a",newline='')
csvWriter = csv.writer(csvFile)
csvWriter.writerow((timeEnd-timeStart,))

# Cleanup time
csvFile.close()
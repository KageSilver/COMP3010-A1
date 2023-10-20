// started with https://www.educative.io/edpresso/how-to-implement-tcp-sockets-in-c
// and the example in https://www.man7.org/linux/man-pages/man3/getaddrinfo.3.html

/*------------------------------------------
# NAME		: Tara Boulanger
# STUDENT NUMBER	: 7922331
# COURSE		: COMP 3010
# INSTRUCTOR	: Robert Guderian
# ASSIGNMENT	: Assignment 1 Part 3
# 
# REMARKS: This is the system test file used for
#   testing the system provided by the company.
#   it will make a new note, then it will view
#   that note, then it will visit it again to
#   find a 404 error.
#
#------------------------------------------*/

//Include statements
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#include <netdb.h> //for getaddrinfo
#include <unistd.h> //for close
#include <stdlib.h> //for exit

#include <assert.h>

//Main, to run the code!
int main(void) {
    //Declaring variables
    int socketDescription;
    struct sockaddr_in serverAddress;
    //Buffers to hold strings, stack-based so no need to malloc
    char serverMessage[2000], clientMessage[2000];
    char address[100];

    struct addrinfo *result;
    
    //Clean buffers (defensive programming):
    memset(serverMessage,'\0',sizeof(serverMessage));
    memset(clientMessage,'\0',sizeof(clientMessage));
    
    //Create socket:
    socketDescription = socket(AF_INET, SOCK_STREAM, 0);
    
    if ( socketDescription < 0 ) {
        printf("Unable to create socket\n");
        return -1;
    }//end if
    
    printf("Socket created successfully\n");

    struct addrinfo hints; //dns lookup
    memset (&hints, 0, sizeof (hints));
    hints.ai_family = PF_UNSPEC; //unspecified
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_flags |= AI_CANONNAME;
    
    malloc(result);

    //Get the ip of the page based on hostname we want to scrape (by doing a dns lookup)
    //hints and result pointers are being passed
    int out = getaddrinfo ("www.cs.umanitoba.ca", NULL, &hints, &result);
    //Fail gracefully
    if (out != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(out));
        exit(EXIT_FAILURE);
    }//end if
    
    //ai_addr is a struct sockaddr
    //So, we can just use that sin_addr
    struct sockaddr_in *serverDetails =  (struct sockaddr_in *)result->ai_addr;
    
    //Set port and IP the same as server-side:
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(80);
    //serverAddress.sin_addr.s_addr = inet_addr("127.0.0.1");
    serverAddress.sin_addr = serverDetails->sin_addr;
    
    //Converts to octets
    printf("Convert...\n");
    //Network to pointer, in string format (octet.octet.octet...) 8 bits, short
    inet_ntop (serverAddress.sin_family, &serverAddress.sin_addr, address, 100);
    printf("Connecting to %s\n", address);
    //Send connection request to server:
    if ( connect(socketDescription, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) < 0 ) {
        printf("Unable to connect\n");
        exit(EXIT_FAILURE);
    }//end if
    printf("Connected with server successfully\n");
    

    
    
    
    //strstr will be nice to parse a string, the reply will have an id which we can find and pull out
    //Compare both notes using assert statements (are they the same) with check printing before
    //Check if the note is gone (GET)

    char theRequestName[] = "Tara";
    char theRequestMessage[] = "blahblah";

    //Grabbing the page itself

    //The string of the request that we're making
    char request[] = "GET http://www-test.cs.umanitoba.ca/~comp3010/cgi-bin/a1/index.cgi HTTP/1.1\r\nHost: www-test.cs.umanitoba.ca\r\n\r\n";
    printf("Sending:\n%s\n", request);
    //Send the message to server:
    printf("Sending request, %lu bytes\n", strlen(request));
    if ( send(socketDescription, request, strlen(request), 0) < 0 ) {
        printf("Unable to send message\n");
        return -1;
    }//end if
    
    //Receive the server's response:
    if ( recv(socketDescription, serverMessage, sizeof(serverMessage), 0) < 0 ) {
        printf("Error while receiving server's msg\n");
        return -1;
    }//end if
    
    printf("Server's response: %s\n",serverMessage);
    

    //Making a post request to the server

    //The string of the request that we're making
    char request[] = "POST http://www-test.cs.umanitoba.ca/~comp3010/cgi-bin/a1/newnote.cgi?name=Tara&message=blahblah HTTP/1.1\r\nHost: www-test.cs.umanitoba.ca\r\n\r\n";
    printf("Sending:\n%s\n", request);
    //Send the message to server:
    printf("Sending request, %lu bytes\n", strlen(request));
    if ( send(socketDescription, request, strlen(request), 0) < 0 ) {
        printf("Unable to send message\n");
        return -1;
    }//end if
    
    //Receive the server's response:
    if ( recv(socketDescription, serverMessage, sizeof(serverMessage), 0) < 0 ) {
        printf("Error while receiving server's msg\n");
        return -1;
    }//end if
    
    printf("Server's response: %s\n",serverMessage);


    //Grabbing the new page from the response (MAY NOT BE NEEDED)
    
    //The string of the request that we're making
    char request[] = "GET http://www-test.cs.umanitoba.ca/~comp3010/cgi-bin/a1/newnote.cgi HTTP/1.1\r\nHost: www-test.cs.umanitoba.ca\r\n\r\n";
    printf("Sending:\n%s\n", request);
    //Send the message to server:
    printf("Sending request, %lu bytes\n", strlen(request));
    if ( send(socketDescription, request, strlen(request), 0) < 0 ) {
        printf("Unable to send message\n");
        return -1;
    }//end if
    
    //Receive the server's response:
    if ( recv(socketDescription, serverMessage, sizeof(serverMessage), 0) < 0 ) {
        printf("Error while receiving server's msg\n");
        return -1;
    }//end if
    
    printf("Server's response: %s\n",serverMessage);


    //Storing the key of the server's response
    char foundKey[] = strstr(serverMessage,"key=");


    //Going back to the main page itself

    //The string of the request that we're making
    char request[] = "GET http://www-test.cs.umanitoba.ca/~comp3010/cgi-bin/a1/index.cgi HTTP/1.1\r\nHost: www-test.cs.umanitoba.ca\r\n\r\n";
    printf("Sending:\n%s\n", request);
    //Send the message to server:
    printf("Sending request, %lu bytes\n", strlen(request));
    if ( send(socketDescription, request, strlen(request), 0) < 0 ) {
        printf("Unable to send message\n");
        return -1;
    }//end if
    
    //Receive the server's response:
    if ( recv(socketDescription, serverMessage, sizeof(serverMessage), 0) < 0 ) {
        printf("Error while receiving server's msg\n");
        return -1;
    }//end if
    
    printf("Server's response: %s\n",serverMessage);


    //Making a get request with the key we got from the server

    //The string of the request that we're making
    char request[] = "GET http://www-test.cs.umanitoba.ca/~comp3010/cgi-bin/a1/getnote.cgi?key=";
    strcat(request,foundKey);
    strcat(request," HTTP/1.1\r\nHost: www-test.cs.umanitoba.ca\r\n\r\n");
    printf("Sending:\n%s\n", request);
    //Send the message to server:
    printf("Sending request, %lu bytes\n", strlen(request));
    if ( send(socketDescription, request, strlen(request), 0) < 0 ) {
        printf("Unable to send message\n");
        return -1;
    }//end if
    
    //Receive the server's response:
    if ( recv(socketDescription, serverMessage, sizeof(serverMessage), 0) < 0 ) {
        printf("Error while receiving server's msg\n");
        return -1;
    }//end if
    
    printf("Server's response: %s\n",serverMessage);



    //Asserts for checking if the server returned the right name and message
    printf("Checking if the returned name is the same as what we passed.\n");
    assert(strcmp(theRequestName,strstr(serverMessage,theRequestName)));
    printf("First assertion passed.");

    printf("Checking if the returned message is the same as what we passed.\n");
    assert(strcmp(theRequestMessage,strstr(serverMessage,theRequestMessage)));
    printf("Second assertion passed.");



    //Going back to the main page itself, again

    //The string of the request that we're making
    char request[] = "GET http://www-test.cs.umanitoba.ca/~comp3010/cgi-bin/a1/index.cgi HTTP/1.1\r\nHost: www-test.cs.umanitoba.ca\r\n\r\n";
    printf("Sending:\n%s\n", request);
    //Send the message to server:
    printf("Sending request, %lu bytes\n", strlen(request));
    if ( send(socketDescription, request, strlen(request), 0) < 0 ) {
        printf("Unable to send message\n");
        return -1;
    }//end if
    
    //Receive the server's response:
    if ( recv(socketDescription, serverMessage, sizeof(serverMessage), 0) < 0 ) {
        printf("Error while receiving server's msg\n");
        return -1;
    }//end if
    
    printf("Server's response: %s\n",serverMessage);

    
    //Making another get request with the key we got from the server

    //The string of the request that we're making
    char request[] = "GET http://www-test.cs.umanitoba.ca/~comp3010/cgi-bin/a1/getnote.cgi?key=";
    strcat(request,foundKey);
    strcat(request," HTTP/1.1\r\nHost: www-test.cs.umanitoba.ca\r\n\r\n");
    printf("Sending:\n%s\n", request);
    //Send the message to server:
    printf("Sending request, %lu bytes\n", strlen(request));
    if ( send(socketDescription, request, strlen(request), 0) < 0 ) {
        printf("Unable to send message\n");
        return -1;
    }//end if
    
    //Receive the server's response:
    if ( recv(socketDescription, serverMessage, sizeof(serverMessage), 0) < 0 ) {
        printf("Error while receiving server's msg\n");
        return -1;
    }//end if
    
    printf("Server's response: %s\n",serverMessage);


    //Asserts for checking if the server "rejected" the request
    printf("Checking if the server gave the right response.\n");
    assert(strcmp("Something bad happened",strstr(serverMessage,"Something bad happened")));
    printf("Final assertion passed.");



    //Close the socket:
    close(socketDescription);
    
    return 0;
}//end main

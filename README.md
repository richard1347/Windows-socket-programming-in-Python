# Windows-socket-programming-in-Python
This program demonstrates how to communicate between a client/server achitecture using Windows Socket Programming techniques. It is written in Python, since Python has already encapsulated C/C++ socket library into a more approachable and easy to use package, we can implement the basic socket communication over a IP network using a few lines of code.
First, we need to know some concepts of the Network Architecture. The universal network architecture model is OSI (Open System Interconnection) reference model, which is widely used in today's Internet.
![network architecture](image/networkarch.png#pic_center)
The 7-layer network architecture is often referred in complex network programs, for example, if we want to use VoIP phones on the Internet. For a socket communication, we only used the first 4 layers starting from the physical layer to the transport layer. TCP and UDP are actually working on the fourth layer, they are tranport layer protocols. And IP works on the third layer, the network layer. So our socket programming is based upon TCP or UDP running on IP networks, and a socket is a simulation of TCP and UDP or other protocols in network communications. Let's see how a typical socket communication flow works, the following diagram bases on this program.
![socket work flow](image/socketflow.png#pic_center)
1. the client initialize a socket, using AF_INET, which means it's over a IPv4 network, and SOCK_STREAM to establish a streaming connection socket. This is a connection oriented TCP.
2. the client connect to the peer server, with its IP address and port.
3. on the other side, the server initialize the same type of socket, and bind itself to its IP address and port.
4. the server begins listening on the socket, if there is any clients's connection requests come, it will accept it and then the client/server connection establishes.
5. the client/server will communicate on the connection, sending and receiving data.
6. data packet using 512 bytes.
7. the client ends the session, and close the socket.

Here we should notice that the server begin listening on the socket, this is a blocking process, it will block until it receives a client's connection request.
This program also uses Win32 API to provide some basic UIs, we import win32api package at the beginning of the program.

## How to install Win32 API for Python
Open your Windows command line prompt, input
### >pip install pywin32
This presumes you have correctly installed Python 3.x on your system.

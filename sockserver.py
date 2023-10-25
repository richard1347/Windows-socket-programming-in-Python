import socket,win32api
from socket import *

class ServerSocket:
    svrIpaddr=''
    svrPort=0
    def __init__(self,ip,port):
        self.svrIpaddr=ip
        self.svrPort=port

    def start_server(self):
        svrSocket=socket(AF_INET,SOCK_STREAM)
        svrSocket.bind((self.svrIpaddr,self.svrPort))
        svrSocket.listen(100)
        win32api.MessageBox(0,'Already started server at '+str(self.svrIpaddr)+':'+str(self.svrPort),'Start Server',0x00|0x40)
        connSocket,peerAddr=svrSocket.accept()
        print('Accept a client\'s connection from ',peerAddr)

        while True:
            recved=connSocket.recv(512)
            if not recved:
                break
            data=recved.decode()
            print(f'Received peer information: {data}')
            reply=input('What do you want to reply?>')
            connSocket.send(reply.encode())
        connSocket.close()
        svrSocket.close()

if __name__=='__main__':
    sock1=ServerSocket('192.168.0.6',23234)                                                #replace IP address and port with yours
    sock1.start_server()

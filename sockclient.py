# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 17:10:19 2023

@author: richard1347
"""

import socket,win32api

class ClientSocket:
    peerIpaddr=''
    peerPort=0
    def __init__(self,ip,port):
        self.peerIpaddr=ip
        self.peerPort=port
    def connect_server(self):
        connSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSocket.connect((self.peerIpaddr,self.peerPort))
        win32api.MessageBox(0,'Already connected server at '+str(self.peerIpaddr)+':'+str(self.peerPort),'Connecting Result',0x00|0x40)
        while True:
            sending=input('Please input your message:>')
            if sending=='q' or sending=='exit':
                break;
            connSocket.send(sending.encode())
            recved=connSocket.recv(512)
            if not recved:
                break
            print(recved.decode())
        connSocket.close()
        
if __name__=='__main__':
    sock1=ClientSocket('192.168.0.5',23234)                                            #replace IP address and port with yours
    sock1.connect_server()

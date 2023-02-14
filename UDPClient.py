from socket import *

address = '127.0.0.1'
port = 12000

clientSock = socket(AF_INET, SOCK_DGRAM)    #creating UDP socket for server
msg = input('Input lowercase sentence:')    #get user input
clientSock.sendto(msg.encode(), (address, port))    #attaching server name and port

modifiedMsg, serverAddress = clientSock.recvfrom(2048)  #read the reply character from socket into a string
print(modifiedMsg.decode())
clientSock.close()



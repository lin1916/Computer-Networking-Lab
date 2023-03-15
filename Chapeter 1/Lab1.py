#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
port = 11111 # 设置一个端口号
serverSocket.bind(('', port)) # 绑定主机和端口
serverSocket.listen(100)  # 等待客户端连接
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    #Fill in start
    connectionSocket, addr = serverSocket.accept() 
    #Fill in end       
    try:   
        message = connectionSocket.recv(4096).decode() 
        filename = message.split()[1] 
        f = open(filename[1:]) 
       
        outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start
        outputdata = "HTTP /1.1 200 OK\r\nConnection: close\r\nServer: localhost\r\nConnect-Tpye: text/html\r\n\r\n"  + outputdata
        print(outputdata)
        #Fill in end 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start 
        responsemessage = "HTTP /1.1 404 Not Found\r\n"
        connectionSocket.send(responsemessage.encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end 
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
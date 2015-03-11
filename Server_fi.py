#import socket module

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Bind the socket to address.
#Fill in start
serverSocket.bind(('localhost',8011))
##Listen for connections made to the socket. 
##The argument specifies the maximum number of queued connections and should be at least 0.
##The maximum value is system-dependent (usually 5).
serverSocket.listen(1)
#Fill in end

while True:
 	#Establish the connection
 	print 'Ready to serve...'
 	
 	#Fill in start
 	##Accept a connection. The socket must be bound to an address and listening for connections. 
 	##The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, 
 	##and address is the address bound to the socket on the other end of the connection.
 	connectionSocket, addr = serverSocket.accept()
 	#Fill in end

 	try:
 		#Fill in start
 		##Receive data from the socket. 
 		##The return value is a string representing the data received. 
 		##The maximum amount of data to be received at once is specified by bufsize.
 		message = connectionSocket.recv(4096) 
 		#Fill in end
 		command = message.split()[0]
 		print command
 		filename = message.split()[1]
 		print filename
 		f = open(filename[1:])
 		if command == "HEAD":
 			connectionSocket.send('TRUE')
 			f.close()
 			connectionSocket.close()
	 	elif command =="GET":
 			#Fill in start
 			outputdata = f.read()  
 			#Fill in end
 			#Send one HTTP header line into socket
 			#Fill in start
 			connectionSocket.send('HTTP/1.1 200 OK\n\n')
 			#Fill in end
 			#Send the content of the requested file to the client
 			for i in range(0, len(outputdata)):
 				connectionSocket.send(outputdata[i])
 			connectionSocket.close()
 	except IOError:
 		#Send response message for file not found
 		#Fill in start
 		connectionSocket.send('HTTP/1.1 404 Not Found\n\n<html><header><title>404 Not Found</title></header><body>404 Not Found</body></html>')
 		#Fill in end
 		#Close client socket
 		#Fill in start
 		connectionSocket.close()
 		#Fill in end 
 	finally:
 		connectionSocket.close()
serverSocket.close() 
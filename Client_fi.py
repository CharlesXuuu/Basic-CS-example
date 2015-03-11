#import socket module
from socket import *
#import sys module
import sys
import time

#read command line argument
host = sys.argv[1] #localhost
port = sys.argv[2] #port number
filename = sys.argv[3] #filename
command = sys.argv[4] #command

#combine the contect to be sent
content = ''+command+' /'+filename+' HTTP/1.1'
print 'Command:\n', content

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, int(port)))
s.sendall(content)

print '\n\nReceived:\n'
content = []
while True:
	buf = s.recv(4096)
	if not buf:
		break
	content.append(buf)
out=''.join(content)
#time.sleep(0.5)
print out
s.close()
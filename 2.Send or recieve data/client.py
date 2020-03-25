import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                          
port = 9999
data = input("Enter your message - ")


s.connect((host, port))  
data = data.encode('utf-8')

#sending data in server
s.send(data)
#reciving data from server 
msg = s.recv(1024)                                     

s.close()
print (msg.decode('utf-8'))
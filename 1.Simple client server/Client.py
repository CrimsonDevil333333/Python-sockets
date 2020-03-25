import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                          
port = 9999


s.connect((host, port))  
#to recieve data if server is sending any...
msg = s.recv(1024)                                     

s.close()
print (msg.decode('utf-8'))
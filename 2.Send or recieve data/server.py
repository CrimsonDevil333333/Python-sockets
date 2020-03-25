import socket                                         
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                            
port = 9999                                           
serversocket.bind((host, port))                                  
serversocket.listen(5)                                           

while True:
   
   clientsocket,addr = serversocket.accept()      
   print("Got a connection from %s" % str(addr))
   data = clientsocket.recv(1024).decode('utf-8')
   print("Recived data from client is ",data)
   sent_data = f"You sent us '{data}'"

   #sending data in client server
   clientsocket.send(sent_data.encode('utf-8'))
   clientsocket.close()
import socket                                         
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                            
port = 9999                                           
serversocket.bind((host, port))                                  
serversocket.listen(5)                                           

#to keep server always on
while True:
   
   clientsocket,addr = serversocket.accept()      
   sent_data = 'Welcome conection is made'
   clientsocket.send(sent_data.encode('utf-8'))
   clientsocket.close()
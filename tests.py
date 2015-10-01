__author__ = 'kyle'

#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = int(input("Please Enter a Port Number") )          # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send('Thank you for connecting'.encode())


   result=c.recv(1024).decode()                          #Stores equation in variable result

   c.send(str(eval(result)).encode())                    #evaluates result variable and sends answer to client




   #c.close()                # Close the connection
